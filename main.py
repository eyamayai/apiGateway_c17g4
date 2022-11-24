from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, verify_jwt_in_request, get_jwt_identity
import requests
from waitress import serve
from datetime import timedelta

import utils
from registraduria_backend.candidato_blueprints import candidato_blueprints
from registraduria_backend.partido_blueprints import partido_blueprints
from registraduria_backend.resultado_blueprints import resultado_blueprints
from security_backend.permission_blueprints import permission_blueprints
from registraduria_backend.reports_blueprints import reports_blueprints
from security_backend.rol_blueprints import rol_blueprints
from registraduria_backend.mesa_blueprints import mesa_blueprints
from security_backend.user_blueprints import user_blueprints


app = Flask(__name__)
app.config['JWT_SECRET_KEY']= 'misionticg4'
cors = CORS(app)
jwt = JWTManager(app)

app.register_blueprint(candidato_blueprints)
app.register_blueprint(partido_blueprints)
app.register_blueprint(resultado_blueprints)
app.register_blueprint(permission_blueprints)
app.register_blueprint(reports_blueprints)
app.register_blueprint(rol_blueprints)
app.register_blueprint(mesa_blueprints)
app.register_blueprint(user_blueprints)


@app.before_request
def before_request_callback() -> tuple:
    endpoint = utils.clean_url(request.path)
    exclude_routes = ["/login", "/"]
    if exclude_routes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        user = get_jwt_identity()
        if user.get('rol'):
            has_grant = utils.validate_grant(endpoint, request.method, user['rol'].get('idRol'))
            if not has_grant:
                return {"message": "Permission denied by revision."}, 401
        else:
            return {"message": "Permission denied by not rol."}, 401


@app.route("/", methods=['GET'])
def home() -> dict:
    response = {"message": "Welcome to the Registraduria API Gateway C17G4..."}
    return response


@app.route('/login', methods=['POST'])
def login() -> tuple:
    user = request.get_json()
    url = f'{data_config.get("url-backend-security")}/user/login'
    request_response = requests.post(url, json=user, headers=utils.HEADERS)
    if request_response.status_code == 200:
        user_logged = request_response.json()
        del user_logged['rol']['permissions']
        expires = timedelta(days=1)
        access_token = create_access_token(identity=user_logged, expires_delta=expires)
        return {"token": access_token, "user_id": user_logged.get("id")}, 200
    else:
        return {"message": "Invalid access"}, 401


if __name__ == '__main__':
    data_config = utils.load_file_config()
    print(f'API Gateway Server running: http://{data_config.get("url-api-gateway")}:{data_config.get("port")}')
    serve(app, host=data_config.get('url-api-gateway'), port=data_config.get('port'))

from flask import request, Blueprint
import requests
from utils import load_file_config, HEADERS

resultado_blueprints = Blueprint("resultado_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-registraduria') + "/resultado"


@resultado_blueprints.route("/resultados", methods=['GET'])
def get_all_resultados() -> dict:
    url = f'{url_base}/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@resultado_blueprints.route("/resultado/<string:id_>", methods=['GET'])
def get_resultado_by_id(id_: str) -> dict:
    url = f'{url_base}/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@resultado_blueprints.route("/resultado/insert", methods=['POST'])
def insert_resultado() -> dict:
    resultado = request.get_json()
    url = f'{url_base}/insert'
    response = requests.post(url, headers=HEADERS, json=resultado)
    return response.json()


@resultado_blueprints.route("/resultado/update/<string:id_>", methods=['PUT'])
def update_resultado(id_: str) -> dict:
    resultado = request.get_json()
    url = f'{url_base}/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=resultado)
    return response.json()


@resultado_blueprints.route("/resultado/delete/<string:id_>", methods=['DELETE'])
def delete_resultado(id_: str) -> dict:
    url = f'{url_base}/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return {"message": "processed"}, response.status_code

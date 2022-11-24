from flask import request, Blueprint
import requests

from utils import load_file_config, HEADERS

mesa_blueprints = Blueprint("mesa_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-registraduria') + "/mesa"


@mesa_blueprints.route("/mesas", methods=['GET'])
def get_all_mesas() -> dict:
    url = f'{url_base}/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@mesa_blueprints.route("/mesa/<string:id_>", methods=['GET'])
def get_mesa_by_id(id_: str) -> dict:
    url = f'{url_base}/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@mesa_blueprints.route("/mesa/insert", methods=['POST'])
def insert_mesa() -> dict:
    mesa = request.get_json()
    url = f'{url_base}/insert'
    response = requests.post(url, headers=HEADERS, json=mesa)
    return response.json()


@mesa_blueprints.route("/mesa/update/<string:id_>", methods=['PUT'])
def update_mesa(id_: str) -> dict:
    mesa = request.get_json()
    url = f'{url_base}/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=mesa)
    return response.json()


@mesa_blueprints.route("/mesa/delete/<string:id_>", methods=['DELETE'])
def delete_mesa(id_: str) -> dict:
    url = f'{url_base}/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return {"message": "processed"}, response.status_code

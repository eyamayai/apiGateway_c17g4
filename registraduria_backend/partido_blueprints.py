from flask import request, Blueprint
import requests

from utils import load_file_config, HEADERS

partido_blueprints = Blueprint("partido_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-registraduria') + "/partido"


@partido_blueprints.route("/partidos", methods=['GET'])
def get_all_partidos() -> dict:
    url = f'{url_base}/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@partido_blueprints.route("/partido/<string:id_>", methods=['GET'])
def get_partido_by_id(id_: str) -> dict:
    url = f'{url_base}/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@partido_blueprints.route("/partido/insert", methods=['POST'])
def insert_partido() -> dict:
    partido = request.get_json()
    url = f'{url_base}/insert'
    response = requests.post(url, headers=HEADERS, json=partido)
    return response.json()


@partido_blueprints.route("/partido/update/<string:id_>", methods=['PUT'])
def update_partido(id_: str) -> dict:
    partido = request.get_json()
    url = f'{url_base}/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=partido)
    return response.json()


@partido_blueprints.route("/partido/delete/<string:id_>", methods=['DELETE'])
def delete_partido(id_: str) -> dict:
    url = f'{url_base}/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return {"message": "processed"}, response.status_code

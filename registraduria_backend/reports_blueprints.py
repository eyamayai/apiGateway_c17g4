from flask import Blueprint
import requests

from utils import load_file_config, HEADERS

reports_blueprints = Blueprint("reports_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-registraduria') + "/reports"


@reports_blueprints.route("/reports/mesa_resultados/all", methods=['GET'])
def report_mesas_resultados() -> dict:
    url = f'{url_base}/mesa_resultados/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/mesa_resultados/<string:id_>", methods=['GET'])
def report_mesa_resultados_by_id(id_: str) -> dict:
    url = f'{url_base}/mesa_resultados/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/candidato_resultados/all", methods=['GET'])
def report_candidato_resultados() -> dict:
    url = f'{url_base}/candidato_resultados/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/candidato_resultados/<string:id_>", methods=['GET'])
def report_candidato_resultados_by_id(id_: str) -> dict:
    url = f'{url_base}/candidato_resultados/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/mesas_top_resultados", methods=['GET'])
def report_mesas_more_resultados() -> dict:
    url = f'{url_base}/mesas_top_resultados'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/partido_resultados", methods=['GET'])
def report_partido_resultados() -> dict:
    url = f'{url_base}/partido_resultados'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/partido_distribution", methods=['GET'])
def report_partido_distribution() -> dict:
    url = f'{url_base}/partido_distribution'
    response = requests.get(url, headers=HEADERS)
    return response.json()

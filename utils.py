import json
import re
import requests

HEADERS = {"Content-Type": "application/json; charset=utf-8"}


def load_file_config() -> dict:
    with open("config.json") as file_:
        data = json.load(file_)
    return data


def clear_url(url: str) -> str:
    segments = url.split("/")
    for segment in segments:
        if re.search('\\d', segment):
            url = url.replace(segment, "?")
    return url


def validate_grant(endpoint: str, method: str, id_rol: int) -> bool:
    data_config = load_file_config()
    url = f'{data_config.get("url-backend-security")}/rol/validate/{id_rol}'
    has_grant = False
    body = {
        "url": endpoint,
        "method": method
    }
    response = requests.get(url, headers=HEADERS, json=body)
    try:
        if response.status_code == 200:
            has_grant = True
    except Exception as e:
        print(e)
    return has_grant

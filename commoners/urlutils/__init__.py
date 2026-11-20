from typing import Optional, Union
from enum import StrEnum, auto

import requests


class ResponseType(StrEnum):
    RAW = auto()
    TEXT = auto()
    JSON = auto()


def get_uri(uri, params=None, response_type: ResponseType = ResponseType.TEXT, is_image: bool = False) -> Union[str, dict, bytes]:
    """
        Makes a simple GET request to the given URL and returns the
        response as text or json. If the request fails it raises
        a HTTPError.

        Args:
            uri (str): URL or the target to send the POST request
            params (dict): key value pair that match the fields
                           in the POST request
            reponse (str): how the response is returned: as a text or
                           json.

        Returns:
            str or json: body of the response in the selected format
    """

    headers = {
        "User-Agent": "Chrome/63.0.3239.84",
    }

    stream = True if is_image else False

    r = requests.get(uri, headers=headers, params=params, stream=stream)
    r.raise_for_status()

    match response_type:
        case ResponseType.TEXT:
            return r.text
        case ResponseType.JSON:
            return r.json()
        case ResponseType.RAW:
            return r.content
        case _:
            raise ValueError(f"type of response {response} not supported")


def get_site(url: str, params: Optional[dict] = None) -> str:
    return get_uri(uri=url, params=params, response_type=ResponseType.TEXT)


def get_json(url: str, params: Optional[dict] = None) -> dict:
    return get_uri(uri=url, params=params, response_type=ResponseType.JSON)


def get_image(url: str, params: Optional[dict] = None) -> bytes:
    return get_uri(uri=url, params=params, response_type=ResponseType.RAW, is_image=True)


def post_uri(uri, params=None, form=True, response: ResponseType = ResponseType.TEXT):
    """
        Makes a simple POST request to the given URL and returns the
        response as text or json. If the request fails it raises
        a HTTPError.

        Args:
            uri (str): URL or the target to send the POST request
            params (dict): key value pair that match the fields
                           in the POST request
            form (bool): how the parameters are codified. When True
                         the request uses a form enconding, when False
                         a json enconding
            reponse (ResponseType): how the response is returned: as a text or
                           json.

        Returns:
            str or json: body of the response in the selected format
    """
    payload = params

    if form:
        r = requests.post(uri, data=payload)
    else:
        r = requests.post(uri, json=payload)

    if r.status_code == 200:
        if response is ResponseType.JSON:
            return r.json()

        return r.text

    r.raise_for_status()

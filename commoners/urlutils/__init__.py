import requests


RAW = "raw"
TEXT = "text"
JSON = "json"


def get_uri(uri, params=None, response=TEXT):
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
    payload = params

    r = requests.get(uri, params=payload)

    if r.status_code == 200:
        if response == JSON:
            return r.json()

        return r.text

    r.raise_for_status()


def post_uri(uri, params=None, form=True, response=TEXT):
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
            reponse (str): how the response is returned: as a text or
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
        if response == JSON:
            return r.json()

        return r.text

    r.raise_for_status()

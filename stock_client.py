import json
from http.client import HTTPConnection
from urllib.parse import urlencode


def fetch_stock(part_code):
    connection = HTTPConnection("127.0.0.1", 8765, timeout=3)
    try:
        query = urlencode({"part": part_code})
        connection.request("GET", "/stock?" + query)
        response = connection.getresponse()
        if response.status == 404:
            return None
        if response.status != 200:
            raise OSError(f"Stock API status: {response.status}")
        return json.loads(response.read())
    finally:
        connection.close()

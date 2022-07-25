from dataclasses import dataclass
from urllib.parse import urlencode
import requests
from pprint import pprint

@dataclass
class Params:
    data_type: str
    endpoint: str
    api_key: str

class GoogleMap(Params):
    def __init__(self):
        self.api_key = ''
        self.data_type = 'json'
        self.endpoint = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}" 

    def get_whole_object(self, address: str) -> dict:
        params = {"placeid": address, "key": self.api_key}
        url_params = urlencode(params)
        url = f"{self.endpoint}?{url_params}"
        response = requests.get(url)
        if response.status_code not in range(200, 299):
            print(self.response.status_code) 
            self.response = {}
        return response.json()["results"][0]

    def get_lat_long(self, address):
        return self.get_whole_object(address)["geometry"]["location"]

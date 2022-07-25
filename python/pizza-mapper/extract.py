from dataclasses import dataclass
import json
from pathlib import Path
import os
from pprint import pprint
import requests

__DEBUG = False

URL="https://onebite.app/restaurant/daves-favorites"
DATA_FILE_LOCATION="daves_favorite_pizza.json"

class ExtractSiteData:
    """Class to grab and store Pizza website data"""
    def __init__(self, URL, **kwargs) -> None:
        self.url = URL

    @staticmethod
    def _validate(input, expected):
        assert(isinstance(input, expected))

    def get_site_data(self) -> dict:
        self._validate(URL, str)
        full_site_text = requests.get(self.url).text
        data_start = full_site_text.find('{"')
        data_end = full_site_text.rfind('</script')
        json_data = json.loads(full_site_text[data_start:data_end])
        return json_data

    def to_file(self, file_location: Path) -> None:
        data = self.get_site_data()
        with open(file_location, 'w') as f:
            f.write(json.dumps(data))
        print(f"Successfully wrote to:\t{file_location}")

if __name__=='__main__':
    ExtractSiteData(URL).to_file(DATA_FILE_LOCATION)

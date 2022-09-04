from dataclasses import dataclass
import json
from pathlib import Path
import os
from pprint import pprint
from typing import List
import requests

__DEBUG = False

URL="https://onebite.app/restaurant/daves-favorites?page="
DATA_FILE_LOCATION="daves_favorite_pizza.json"

class ExtractSiteData:
    """Class to grab and store Pizza website data"""
    def __init__(self, URL, **kwargs) -> None:
        self.url = URL

    @staticmethod
    def _validate(input, expected):
        assert(isinstance(input, expected))

    def has_next_page(self, text: str) -> bool:
        return 'next' in text

    def get_site_data(self) -> List[dict]:
        pages = []
        self._validate(URL, str)
        iterations = 5
        for page in range(1, iterations):
            url = self.url + str(page)
            print(url)
            full_site_text = requests.get(url).text
            print(full_site_text)
            data_start = full_site_text.find('{"')
            data_end = full_site_text.rfind('</script')
            print(data_start, data_end)
            pages.append(json.loads(full_site_text[data_start:data_end]))
            if not self.has_next_page(full_site_text):
                break
        return pages

    def to_file(self, file_location: Path) -> None:
        sites = self.get_site_data()
        with open(file_location, 'w') as f:
            for site in sites:
                f.write(site)
        print(f"Successfully wrote to:\t{file_location}")

if __name__=='__main__':
    ExtractSiteData(URL).to_file(DATA_FILE_LOCATION)

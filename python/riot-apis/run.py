import os
import requests
from valorant.endpoints import *

class Valorant:
    def __init__(self):
        self.api_key = os.environ.get('RIOT_API_KEY')
    
    def headers(self) -> str:
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": f"{self.api_key}"
        }

    def request(self, url) -> requests.Response:
        response = requests.get(url,  headers=self.headers())
        return response
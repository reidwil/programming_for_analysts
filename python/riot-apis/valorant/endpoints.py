from collections import abc
import dataclasses

@dataclasses.dataclass
class BaseEndpoints:
    base_url:str = 'https://na.api.riotgames.com'
    valorant: str = 'val'
    league: str = 'lol'
    runeterra: str = 'lor'
    tft: str = 'tft'
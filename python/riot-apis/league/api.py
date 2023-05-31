import requests
from helpers.key import require_api_key

class RiotAPI:
    @require_api_key
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.summoner_base_url = "https://na1.api.riotgames.com/lol/"
        self.match_base_url = "https://americas.api.riotgames.com/lol/"


    def get_summoner_by_name(self, name):
        endpoint = f"summoner/v4/summoners/by-name/{name}"
        headers = {
            "X-Riot-Token": self.api_key
        }
        response = requests.get(self.summoner_base_url + endpoint, headers=headers)
        return response.json()

    def get_match_history(self, puuid):
        endpoint = f"match/v5/matches/by-puuid/{puuid}/ids"
        headers = {
            "X-Riot-Token": self.api_key
        }
        response = requests.get(self.match_base_url + endpoint, headers=headers)
        return response.json()
    
    def get_match_info(self, match_id):
        endpoint = f"match/v5/matches/{match_id}"
        headers = {
            "X-Riot-Token": self.api_key
        }
        response = requests.get(self.match_base_url + endpoint, headers=headers)
        response.raise_for_status()
        return response.json()

    def aggregate_match_data(self, match_id):
        match_info = self.get_match_info(match_id)
        aggregated_data = {"team_1": {}, "team_2": {}}

        participants = match_info['info']['participants']
        
        for participant in participants:
            player_data = {
                'puuid': participant['puuid'],
                'championId': participant['championId'],
                'kills': participant['kills'],
                'deaths': participant['deaths'],
                'assists': participant['assists'],
                'goldEarned': participant['goldEarned'],
                'champLevel': participant['champLevel'],
                'totalMinionsKilled': participant['totalMinionsKilled'],
                # More stats can be added here as needed.
            }

            if participant['teamId'] == 100:
                aggregated_data['team_1'][participant['summonerName']] = player_data
            else:
                aggregated_data['team_2'][participant['summonerName']] = player_data
        return aggregated_data


def get_summoner_data():
    summoner_name = input("Enter Summoner Name: ")

    api = RiotAPI()

    match_results = []
    try:
        summoner = api.get_summoner_by_name(summoner_name)
        print(summoner)
        if 'puuid' in summoner:
            try:
                matches = api.get_match_history(summoner['puuid'])
                if matches:
                    for match in matches:
                        print(f"Getting results for match: {match}")
                        match_results.append(api.aggregate_match_data(match))
                else:
                    print('No matches found for this account.')
            except requests.HTTPError as e:
                print(f'An error occurred while fetching match history: {e}')
        else:
            print('No such summoner found')
    except requests.HTTPError as e:
        print(f'An error occurred while fetching summoner information: {e}')

    return match_results

if __name__ == "__main__":
    print(get_summoner_data())
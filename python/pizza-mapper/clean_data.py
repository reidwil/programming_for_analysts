import json
from pprint import pprint

DATA_FILE_LOCATION="daves_favorite_pizza.json"


def get_reviews(file_name):
    with open(file_name) as f:
        data = f.read()
    json_data = json.loads(data)
    return [review for review in json_data["props"]["reviews"]]

def get_all_ratings():
    output = []
    reviews = get_reviews(DATA_FILE_LOCATION)
    for review in reviews:
        data_object = {}
        venue_data = review["venue"]
        data_object["lat"] = venue_data["loc"]["coordinates"][0]
        data_object["long"] = venue_data["loc"]["coordinates"][1]
        data_object["daves_review"] = venue_data["reviewStats"]["dave"]["averageScore"]
        data_object["community_review"] = venue_data["reviewStats"]["community"]["averageScore"]
        data_object["name"] = venue_data["name"]
        output.append(data_object)
    return output

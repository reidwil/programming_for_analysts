import json
from pprint import pprint

DATA_FILE_LOCATION="daves_favorite_pizza.json"


def get_reviews(file_name):
    with open(file_name) as f:
        data = f.read()
    json_data = json.loads(data)
    return [review for review in json_data["props"]["pageProps"]["venues"]]

def get_all_ratings():
    output = []
    reviews = get_reviews(DATA_FILE_LOCATION)
    for review in reviews:
        data_object = {}
        data_object["lat"] = review["loc"]["coordinates"][0]
        data_object["long"] = review["loc"]["coordinates"][1]
        data_object["daves_review"] = review["reviewStats"]["dave"]["averageScore"]
        data_object["community_review"] = review["reviewStats"]["community"]["averageScore"]
        data_object["name"] = review["name"]
        output.append(data_object)
    return output


print(get_reviews(DATA_FILE_LOCATION))
# all_ratings = get_all_ratings()
# for rating in all_ratings:
#     print('\n')
#     print('-'*40) 
#     pprint(rating)
#     print('-'*40)
#     print('\n')
import requests
from datetime import datetime

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = "PIXELA_USERNAME"
TOKEN = "PIXELA_TOKEN"

today = datetime.now().strftime("%Y%m%d")
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params) POST REQUEST TO CREATE AN ACCOUNT
# print(response.text)

GRAPH_ENDPOINT = "https://pixe.la/v1/users/{}/graphs".format(USERNAME)

graph_config = {
    "id": "testgraph1",
    "name": "Coding Tracker",
    "unit": "minute",
    "type": "int",
    "color": "ajisai",
}

headers = {  # Provide sensitive info as a header so that it isnt visible and is more secure
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)  Create the graph
# print(response.text)

POST_GRAPH_ENDPOINT = GRAPH_ENDPOINT + "/{}".format(graph_config['id'])
add_to_graph = {
    "date": today,
    "quantity": "120",
}
# response = requests.post(url=POST_GRAPH_ENDPOINT, json=add_to_graph, headers=headers)
# print(response.text)

PUT_DELETE_GRAPH_ENDPOINT = POST_GRAPH_ENDPOINT + "/{}".format(today)

update_graph = {
    "quantity": "270"
}
# response = requests.put(url=PUT_DELETE_GRAPH_ENDPOINT, json=update_graph, headers=headers)  PUT REQUEST
# print(response.text)

# response = requests.delete(url=PUT_DELETE_GRAPH_ENDPOINT, headers=headers)  DELETE REQUEST
# print(response.text)

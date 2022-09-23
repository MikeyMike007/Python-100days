# Program illustrates how you can work with the PIXELA API

import requests
from datetime import datetime
import os

TOKEN_PIXELA = os.environ.get("PIXELA_TOKEN")
USER_NAME_PIXELA = os.environ.get("PIXELA_USER_NAME")
ENDPOINT_PIXELA = "https://pixe.la/v1/users"
ENDPOINT_GRAPH = f"{ENDPOINT_PIXELA}/{USER_NAME_PIXELA}/graphs"
ENDPOINT_POST_PIXEL = f"{ENDPOINT_PIXELA}/{USER_NAME_PIXELA}/graphs/graph1"
headers = {"X-USER-TOKEN": TOKEN_PIXELA}

user_params = {
    "token": TOKEN_PIXELA,
    "username": USER_NAME_PIXELA,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# From API documentation
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

today = datetime.now()

post_pixel_params = {"date": today.strftime("%Y%m%d"), "quantity": "15.0"}
ENDPOINT_CHANGE_PIXEL = f"{ENDPOINT_PIXELA}/{USER_NAME_PIXELA}/graphs/graph1/{today.strftime('%Y%m%d')}"  # Date of posting pixel
new_pixel_data = {"quantity": "1.0"}


# Create Account
# response = requests.post(url=ENDPOINT_PIXELA, json=user_params, headers=header)

# Create Graph
# response = requests.post(url=ENDPOINT_GRAPH, json=graph_config, headers=headers)

# Add Value to Graph
# response = requests.post(
#     url=ENDPOINT_POST_PIXEL, json=post_pixel_params, headers=headers
# )
# print(response.text)


# Change Pixel Data
# response = requests.put(url=ENDPOINT_CHANGE_PIXEL, json=new_pixel_data, headers=headers)
# print(response.text)

# Delete Endpoint

ENDPOINT_DELETE = f"{ENDPOINT_PIXELA}/{USER_NAME_PIXELA}/graphs/graph1/{today.strftime('%Y%m%d')}"
response = requests.delete(url=ENDPOINT_DELETE, headers=headers)

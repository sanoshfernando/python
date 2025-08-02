import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "sanosh"
TOKEN = ""
GRAPH_ID = "graph1"

params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

user_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id" : GRAPH_ID,
    "name" : "Walking Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "shibafu"
}
headers  =  {
    "X-USER-TOKEN": TOKEN
}
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
today_ = today.strftime("%Y%m%d")

data = {
    "date": "20250802",
    "quantity": "10"
}

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_}"

new_pixel_data = {
    "quantity":"5"
}

response = requests.put(url=update_endpoint,json=new_pixel_data, headers = headers)
print(response.text)

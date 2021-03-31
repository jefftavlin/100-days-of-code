import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
username = ""
token = ''

params = {
    "token": "uwefhwejfhwejfhejfeh",
    "username": "jeffrey",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url = pixela_endpoint, json=params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

# graph_config = {
#     "id": "graph1",
#     "name": "Reading",
#     "unit": "Pages",
#     "type": "int",
#     "color": "momiji"
# }

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now().strftime('%Y%m%d')

pixel_endpoint = f'{graph_endpoint}/graph1'
pixel_config = {
    "date":today,
    "quantity":'500',
}
# response = requests.post(url = pixel_endpoint, json = pixel_config, headers = headers)
# print(response.text)

# update_endpoint = f'{pixel_endpoint}/{today}'
# update_config = {
#     "quantity":"50"
# }
# response = requests.put(url = update_endpoint, json = update_config, headers=headers)
# print(response.text)

delete_endpoint = f'{pixel_endpoint}/{today}'
response = requests.delete(url = delete_endpoint, headers = headers)
print(response.text)

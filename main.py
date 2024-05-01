import requests
from config import env_vars
import datetime as dt

GRAPH_ID = "graph1"

# Creating a user
# pxie_parameters = {
#     "token": env_vars['TOKEN'],
#     "username": env_vars['USERNAME'],
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# resp = requests.post(url=f"{env_vars['PIXE_ENDPOINT']}/users", json=pxie_parameters)
# print(resp.text)

# Creating a graph
# graph_config = {
#     "id": "graph1",
#     "name": "cycling",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
headers = {
    "X-USER-TOKEN": env_vars['TOKEN']
}
# resp = requests.post(url=f"{env_vars['PIXE_ENDPOINT']}/users/{env_vars['USERNAME']}/graphs", json=graph_config, headers=headers)
# print(resp.text)
# Creating a pixel
date = dt.datetime(year=2024, month=5, day=1)
date = date.strftime("%Y%m%d")
# data_config = {
#     "date": "20240501",
#     "quantity": "20.02"
# }
# resp = requests.post(url=f"{env_vars['PIXE_ENDPOINT']}/users/{env_vars['USERNAME']}/graphs/{GRAPH_ID}",
#                      json=data_config,
#                      headers=headers)
# print(resp.text)

# Updating a pixel
# data_config = {
#     "quantity": "5"
# }
# resp = requests.put(url=f"{env_vars['PIXE_ENDPOINT']}/users/{env_vars['USERNAME']}/graphs/{GRAPH_ID}/{date}",
#                     json=data_config,
#                     headers=headers)
# print(resp.text)

# Deleting a pixel

resp = requests.delete(url=f"{env_vars['PIXE_ENDPOINT']}/users/{env_vars['USERNAME']}/graphs/{GRAPH_ID}/{date}",
                       headers=headers)
print(resp.text)

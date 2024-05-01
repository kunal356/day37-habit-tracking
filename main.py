import requests
from config import env_vars
GRAPH_ID = "graph1"
# pxie_parameters = {
#     "token": env_vars['TOKEN'],
#     "username": env_vars['USERNAME'],
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# # creating user
# resp = requests.post(url=f"{env_vars['PIXE_ENDPOINT']}/users", json=pxie_parameters)
# print(resp.text)

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
data_config = {
    "date": "20240501",
    "quantity": "20.02"
}
resp = requests.post(url=f"{env_vars['PIXE_ENDPOINT']}/users/{env_vars['USERNAME']}/graphs/{GRAPH_ID}", json=data_config,
                     headers=headers)

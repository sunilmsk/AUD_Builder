import requests
from configurations.config import dhs_base_url  # Import the base URL from your config module

class APIClient:
    def __init__(self):
        self.base_url = dhs_base_url  # Set the base URL from your config

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        return response

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data, headers=headers)
        return response

    def put(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=data, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url, headers=headers)
        return response

    def patch(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.patch(url, headers=headers)
        return response

#-------------------------------------------------------------


    # def send_request(self, method, endpoint, data=None, params=None, headers=None):
    #     url = f"{self.base_url}/{endpoint}"
    #
    #     if method == 'GET':
    #         response = requests.get(url, params=params, headers=headers)
    #     elif method == 'POST':
    #         response = requests.post(url, json=data, headers=headers)
    #     elif method == 'PUT':
    #         response = requests.put(url, json=data, headers=headers)
    #     elif method == 'DELETE':
    #         response = requests.delete(url, headers=headers)
    #     elif method == 'PATCH':
    #         response = requests.patch(url, headers=headers)
    #     else:
    #         raise ValueError(f"Unsupported HTTP method: {method}")
    #
    #     return response

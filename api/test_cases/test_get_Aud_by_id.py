import unittest
from urllib import response

from api.api_client import APIClient
from api.configurations.config import Auth
from api.configurations import config as con

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.api_client = APIClient()

    def test_get_Audiences_by_ID_success_200(self):
        endpoint = con.Audience_id
        header = {"Authorization": Auth}

        try:
            response = self.api_client.get(endpoint, headers=header)
            status = response.status_code
            body = response.json()
            print(body)
            print(status)
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            print("An error occurred:", e)
            print("Response content:", response.content)  # Printing the response content for debugging




    def test_get_Audiences_by_Invalid_ID_204(self):
        valid_endpoint = con.Audience_id
        invalid_endpoint = valid_endpoint+ str(1)

        header = {"Authorization": Auth}

        try:
            # get a valid audience by ID
            response_valid = self.api_client.get(valid_endpoint, headers=header)
            status_valid = response_valid.status_code
            body_valid = response_valid.json()
            print("Valid response:", status_valid)
            print(body_valid)
            self.assertEqual(status_valid, 204)

            # Now, try to get an audience with an invalid ID
            response_invalid = self.api_client.get(invalid_endpoint, headers=header)
            status_invalid = response_invalid.status_code

            # Check if the status code is 204 for the invalid ID
            print("Invalid response:",status_invalid )
            self.assertEqual(status_invalid, 204)

        except Exception as e:
            print("An error occurred:", e)
            print("Response content:", response.content)  # Printing the response content for debugging

    def test_Audiences_by_Invalid_Auth_401(self):
        valid_endpoint = con.Audience_id
        header = {"Authorization": "InvalidAuth"}  # Set the header to an invalid value

        try:
            # Now, try to get an audience with an invalid Authorization
            api_response = self.api_client.get(valid_endpoint, headers=header)
            status_code = api_response.status_code

            # Check if the status code is 401 for the invalid Authorization
            print("Invalid Authorization:", header["Authorization"])
            self.assertEqual(status_code, 401)

        except Exception as e:
            print("An error occurred:", e)
            print("Response content:", api_response.content)  # Print the response content for debugging


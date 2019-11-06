import requests
import json
import jsonpath
from resources.API_resources import APIResources

api = APIResources()
response = requests.get(api.uri + api.resource)
print(response)
print("hello")
print("hello")

def test_print():
    assert response == "Response [200]"

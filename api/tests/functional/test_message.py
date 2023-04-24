import json
from resources.payloads import *
from flask_app.services.resources.responses import *
from flask_app import API_KEY

message_endpoint = '/message'

# TODO: Add test for valid add message once auto delete is possible

def test_valid_help_message(client):
    payload = VALID_HELP_MESSAGE
    response = client.post(message_endpoint, data=json.dumps(payload), content_type='application/json', headers={'API_KEY':API_KEY})
    assert response.status_code == 200
    response_body = json.loads(response.get_data())
    assert HELP_RESPONSE in response_body['message']

def test_valid_categories_message(client):
    payload = VALID_CATEGORIES_MESSAGE
    response = client.post(message_endpoint, data=json.dumps(payload), content_type='application/json', headers={'API_KEY':API_KEY})
    assert response.status_code == 200
    response_body = json.loads(response.get_data())
    assert "Here's a list of valid categories:" in response_body['message']

def test_unknown_message(client):
    payload = UNKNOWN_MESSAGE
    response = client.post(message_endpoint, data=json.dumps(payload), content_type='application/json', headers={'API_KEY':API_KEY})
    assert response.status_code == 200
    response_body = json.loads(response.get_data())
    assert UNKNOWN_COMMAND in response_body['message']

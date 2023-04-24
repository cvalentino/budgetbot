import json
from resources.payloads import *
from flask_app import API_KEY

lineitem_from_json_endpoint = '/lineitem'

# def test_valid_lineitem(client):
#     payload = VALID_LINEITEM_PAYLOAD
#     response = client.post(lineitem_from_json_endpoint, data=json.dumps(payload), content_type='application/json', headers={'API_KEY':API_KEY})
#     # TODO: DELETE lineitem from spreadsheet
#     assert response.status_code == 201
#     assert response.headers.get('Updated-Range') is not None

def test_invalid_lineitem_bad_month(client):
    payload = INVALID_LINEITEM_PAYLOAD_BAD_MONTH
    response = client.post(lineitem_from_json_endpoint, data=json.dumps(payload), content_type='application/json', headers={'API_KEY':API_KEY})
    assert response.status_code == 400
    response_body = json.loads(response.get_data())
    assert 'Invalid month provided' in response_body['message']

def test_invalid_lineitem_bad_day(client):
    payload = INVALID_LINEITEM_PAYLOAD_BAD_DAY
    response = client.post(lineitem_from_json_endpoint, data=json.dumps(payload), content_type='application/json', headers={'API_KEY':API_KEY})
    assert response.status_code == 400
    response_body = json.loads(response.get_data())
    assert 'Invalid day provided' in response_body['message']

def test_invalid_lineitem_bad_category(client):
    payload = INVALID_LINEITEM_PAYLOAD_BAD_CATEGORY
    response = client.post(lineitem_from_json_endpoint, data=json.dumps(payload), content_type='application/json', headers={'API_KEY':API_KEY})
    assert response.status_code == 400
    response_body = json.loads(response.get_data())
    assert 'Invalid category provided' in response_body['message']
    
def test_invalid_lineitem_missing_field(client):
    payload = INVALID_LINEITEM_PAYLOAD_MISSING_FIELD
    response = client.post(lineitem_from_json_endpoint, data=json.dumps(payload), content_type='application/json', headers={'API_KEY':API_KEY})
    assert response.status_code == 400
    response_body = json.loads(response.get_data())
    assert 'missing one or more required keys' in response_body['message']

def test_invalid_lineitem_string_day(client):
    payload = INVALID_LINEITEM_PAYLOAD_STRING_DAY
    response = client.post(lineitem_from_json_endpoint, data=json.dumps(payload), content_type='application/json', headers={'API_KEY':API_KEY})
    assert response.status_code == 400
    response_body = json.loads(response.get_data())
    assert 'Invalid day type provided' in response_body['message']

def test_invalid_lineitem_string_day(client):
    payload = INVALID_LINEITEM_PAYLOAD_STRING_COST
    response = client.post(lineitem_from_json_endpoint, data=json.dumps(payload), content_type='application/json', headers={'API_KEY':API_KEY})
    assert response.status_code == 400
    response_body = json.loads(response.get_data())
    assert 'Invalid cost type provided' in response_body['message']
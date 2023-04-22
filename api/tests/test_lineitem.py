import json

def test_heartbeat(client):
    # Test with valid lineitem
    response = client.get('/heartbeat')
    assert response.status_code == 200


def test_valid_lineitem(client):
    # Test with valid lineitem
    payload = {"month": "APR", "day": 21, "description": "TEST", "category": "groceries", "cost": 25.2}
    response = client.post('/lineitem', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 201

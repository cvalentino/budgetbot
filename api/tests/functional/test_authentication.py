import json

# All other endpoints test "passed auth"
def test_failed_auth(client):
    response = client.get('/heartbeat', headers={'API_KEY':'not-the-key'})
    assert response.status_code == 401
    response_body = json.loads(response.get_data())
    assert "Invalid API key provided" in response_body['message']

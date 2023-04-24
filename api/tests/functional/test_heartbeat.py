from flask_app import API_KEY

def test_heartbeat(client):
    response = client.get('/heartbeat', headers={'API_KEY':API_KEY})
    assert response.status_code == 200

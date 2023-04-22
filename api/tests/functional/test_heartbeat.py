def test_heartbeat(client):
    response = client.get('/heartbeat')
    assert response.status_code == 200

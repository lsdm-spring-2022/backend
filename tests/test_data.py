def test_hello_data(test_client):
    response = test_client.get('/api/data')

    assert response.status_code == 200
    assert response.data == b'{"message":"Hello there"}\n'

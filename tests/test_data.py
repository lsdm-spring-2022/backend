def test_data_endpoint(test_client):
    response = test_client.get(
        '/api/data?country=US&date=2020-01-01&source=twitter')

    assert response.status_code == 200
    assert response.data == b'{"country":"US","date":"2020-01-01","source":"twitter"}\n'

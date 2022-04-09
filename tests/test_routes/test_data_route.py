def test_data_endpoint(test_client):
    response = test_client.get(
        '/api/data?region=Mexico&startDate=2016-03-05&endDate=2016-03-08&reddit=true&twitter=false')

    assert response.status_code == 200
    assert response.data == b'{"reddit":[],"twitter":[]}\n'

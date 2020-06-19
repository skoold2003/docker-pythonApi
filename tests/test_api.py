def test_main(client):
    with client.get('/') as response:
        assert response.status_code == 200
        assert 'Welcome to the Police Data Accessibility Project' in str(response.data)
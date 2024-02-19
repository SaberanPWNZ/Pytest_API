import requests


url = "https://favqs.com/api/qotd"


def test_response_status():
    response = requests.get(url=url)
    print(response.json())
    assert response.status_code == 200, "Error, status code not 200"

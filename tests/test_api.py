import requests

def test_root_live():
    url = "http://localhost:32670/"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Kubernetes POC" in response.json()["message"]

def test_predict_live():
    url = "http://localhost:32670/predict?value=5"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["prediction"] == 10

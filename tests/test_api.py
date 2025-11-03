import requests

def test_root_live():
    url = "http://localhost:32592/"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Kubernetes POC" in response.json()["message"]

def test_predict_live():
    url = "http://localhost:32592/predict?value=5"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["prediction"] == 10

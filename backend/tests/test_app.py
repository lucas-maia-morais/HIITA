from flask import session
import os


def test_hiita_ping(client):
    print("Should return pong with status code 200")
    response = client.get("/HIITA/ping")
    assert response.status_code == 200
    data = response.get_json()
    
    assert data['message'] == "pong"

def test_index(client):
    print("Should return list of users with status code 200")
    response = client.get("/")
    print(response)
    assert response.status_code == 200



def test_hiita_login(client):
    print("Should return token with status code 200")
    response = client.post("/HIITA/login", json={"username": 10, "password": "hexa"})
    assert response.status_code == 200
    data = response.get_json()
    print(data)


def test_login_bad_request(client):
    """Should return BAD_REQUEST with status code 400"""
    response = client.post("/HIITA/login", json={"username": "1", "password": "a"})
    assert response.status_code == 400
    data = response.get_json()
    print(data)

def test_error_token_loggedin(client):
    """Should return BAD_REQUEST with status code 400"""
    response = client.post("/HIITA/loggedin")
    assert response.status_code == 400
    data = response.get_json()
    print(data)


def test_error_token_fichas(client):
    """Should return BAD_REQUEST with status code 400"""
    response = client.post("/HIITA/fichas")
    assert response.status_code == 400
    data = response.get_json()
    print(data)
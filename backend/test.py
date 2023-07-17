from a import client

def a_test_login():
    body = {
        "username": 10,
        "password": "hexa"
    }

    response = client.post("/login", json=body)
    assert(response.status_code == 200)
    assert(response.data.message == "SUCCESS")
    assert("token" in response.data)

def a_test_error_login_400():
    body = {
        "username": "",
        "password": ""
    }
    response = client.post("/login", json=body)
    assert(response.status_code == 400)
    assert(response.data == "BAD_REQUEST")

def a_test_error_login_404():
    body = {
        "username": "10",
        "password": "hexa"
    }
    response = client.post("/delete", json=body)
    assert(response.status_code == 200)
    response = client.post("/login", json=body)
    assert(response.status_code == 404)
    assert(response.data == "NOT_FOUND")
from fastapi import testclient


def test_register_email(rest_client: testclient.TestClient):
    response = rest_client.post(
        "/register_email",
        json={
            "email": "em@a.il",
            "password": "123456",
            "re_password": "123456",
        },
    )

    assert response.status_code == 201


def test_register_phone_number(rest_client: testclient.TestClient):
    response = rest_client.post(
        "/register_phone_number",
        json={
            "phone_number": "0123456789",
            "password": "123456",
            "re_password": "123456",
        },
    )

    assert response.status_code == 201

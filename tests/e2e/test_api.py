import pytest
from fastapi import testclient


def test_index_md(rest_client: testclient.TestClient):
    response = rest_client.get("/")

    assert response.status_code == 200


# def test_register_email(rest_client: testclient.TestClient):
#     response = rest_client.post(
#         "/register_email",
#         json={
#             "email": "em@a.il",
#             "password": "123456",
#             "re_password": "123456",
#         },
#     )

#     assert response.status_code == 201


# def test_register_phone_number(rest_client: testclient.TestClient):
#     response = rest_client.post(
#         "/register_phone_number",
#         json={
#             "phone_number": "0123456789",
#             "password": "123456",
#             "re_password": "123456",
#         },
#     )

#     assert response.status_code == 201


# @pytest.fixture
# def register_body(rest_client: testclient.TestClient):

#     rest_client.post(
#         "/register_email",
#         json={
#             "email": "re@gis.ter",
#             "password": "123456",
#             "re_password": "123456",
#         },
#     )

#     return {
#         "email": "re@gis.ter",
#         "password": "123456",
#         "re_password": "123456",
#     }


# def test_login(register_body: dict[str, str], rest_client: testclient.TestClient):
#     response = rest_client.post(
#         "/login",
#         json={
#             "email": register_body["email"],
#             "password": register_body["password"],
#         },
#     )

#     assert response.status_code == 200
#     assert "token" in response.json()
#     assert isinstance(response.json()["token"], str)

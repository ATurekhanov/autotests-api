import httpx

from tools.fakers import get_random_email


create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)

user = create_user_response.json()['user']

login_payload = {
    "email": user['email'],
    "password": "string"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

access_token = login_response.json()['token']['accessToken']

update_user_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{user['id']}",
    headers={"Authorization": f"Bearer {access_token}"},
    json=update_user_payload
)

import httpx


login_payload = {
  "email": "user@example.com",
  "password": "string"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

access_token = login_response.json()['token']['accessToken']

users_me_headers = {"Authorization": f"Bearer {access_token}"}
users_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=users_me_headers)

print(users_me_response.status_code)
print(users_me_response.json())
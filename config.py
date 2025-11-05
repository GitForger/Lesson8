import requests
BASE_URL = "https://ru.yougile.com/api-v2"


YOUGILE_LOGIN = "имейл@имейл.com"
YOUGILE_PASSWORD = "пароль"


auth_response = requests.post(
    f"{BASE_URL}/auth/login",
    json={"login": YOUGILE_LOGIN, "password": YOUGILE_PASSWORD}
)


if auth_response.status_code == 200:
    TOKEN = auth_response.json()["access_token"]
else:
    print(f"Auth failed: {auth_response.status_code}")
    TOKEN = None


HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token"
}


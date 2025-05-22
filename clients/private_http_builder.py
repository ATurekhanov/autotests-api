from httpx import Client

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema


def get_private_http_client(user: LoginRequestSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Схема с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentication_client = get_authentication_client()

    login_response = authentication_client.login(user)

    return Client(
        timeout=60,
        base_url="http://0.0.0.0:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
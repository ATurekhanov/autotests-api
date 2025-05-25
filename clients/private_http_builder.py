from functools import lru_cache

import allure
from httpx import Client

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from config import settings


@lru_cache(maxsize=None)
@allure.step('Get client with JWT token')
def get_private_http_client(user: LoginRequestSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Схема с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentication_client = get_authentication_client()

    login_response = authentication_client.login(user)

    return Client(
        base_url=settings.http_client.client_url,
        timeout=settings.http_client.timeout,
        headers={"Authorization": f"Bearer {login_response.token.access_token}",},
        event_hooks={
            'request': [curl_event_hook, log_request_event_hook],
            'response': [log_response_event_hook]
        }
    )
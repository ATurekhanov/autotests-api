import allure
import httpx
from httpx import Client

from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from config import settings


@allure.step('Get client without JWT token')
def get_public_http_client() -> Client:
    """
    Создает экземпляр httpx.Client с базовыми настройками.
    :return: Готовый к использованию объект httpx.Client.
    """
    return httpx.Client(
        base_url=settings.http_client.client_url,
        timeout=settings.http_client.timeout,
        event_hooks={
            'request': [curl_event_hook, log_request_event_hook],
            'response': [log_response_event_hook]
        }
    )
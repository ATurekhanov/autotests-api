import allure
import httpx
from httpx import Client

from clients.event_hooks import curl_event_hook


@allure.step('Get client without JWT token')
def get_public_http_client() -> Client:
    """
    Создает экземпляр httpx.Client с базовыми настройками.
    :return: Готовый к использованию объект httpx.Client.
    """
    return httpx.Client(
        base_url="http://localhost:8000",
        timeout=60,
        event_hooks={'request': [curl_event_hook]}
    )
import httpx
from httpx import Client


def get_public_http_client() -> Client:
    """
    Создает экземпляр httpx.Client с базовыми настройками.
    :return: Готовый к использованию объект httpx.Client.
    """
    return httpx.Client(base_url="http://localhost:8000", timeout=60)
import allure
from httpx import Request, Response

from tools.http.curl import make_curl_from_request
from tools.logger import get_logger

logger = get_logger("HTTP_CLIENT")


def curl_event_hook(request: Request):
    """
    Event hook для автоматического прикрепления cURL команды к Allure отчету.

    :param request: HTTP-запрос, переданный в `httpx` клиент.
    """

    curl_command = make_curl_from_request(request)

    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)

def log_request_event_hook(request: Request):
    """
    Event hook для логирования HTTP запроса.
    :param request: Объект HTTP запроса.
    """
    logger.info(f'Make {request.method} request to {request.url}')

def log_response_event_hook(response: Response):
    """
    Event hook для логирования HTTP ответа.
    :param response: Объект HTTP ответа.
    """
    logger.info(
        f'Got response {response.status_code} {response.reason_phrase} from {response.request.method} {response.url}'
    )
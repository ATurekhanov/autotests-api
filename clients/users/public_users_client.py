from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str
    lastName: str  # Название ключа совпадает с API
    firstName: str  # Название ключа совпадает с API
    middleName: str  # Название ключа совпадает с API


class PublicUsersClient(APIClient):
    """
    Клиент для публичных методов не требующих авторизации для работы с /api/v1/users.
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с данными пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post("/api/v1/users", json=request)

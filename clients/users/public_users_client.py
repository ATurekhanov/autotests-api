from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users.
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод создания пользователя.

        :param request: Схема с данными пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Получения схемы ответа на создание пользователя.
        :param request: Схема с данными пользователя.
        :return: Схема ответа создания пользователя.
        """
        response = self.create_user_api(request.model_dump(by_alias=True))
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Создает экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())

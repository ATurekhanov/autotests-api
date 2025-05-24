import pytest
from pydantic import BaseModel, EmailStr

from clients.authentication.authentication_schema import LoginRequestSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def id(self) -> str:
        return self.response.user.id

    @property
    def email(self) -> EmailStr:
        return self.response.user.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> LoginRequestSchema:
        return LoginRequestSchema(email=self.email, password=self.password)


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture
def func_user(public_users_client) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)

    return UserFixture(request=request, response=response)


@pytest.fixture
def private_users_client(func_user) -> PrivateUsersClient:
    return get_private_users_client(func_user.authentication_user)

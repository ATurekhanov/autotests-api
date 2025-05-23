from pydantic import BaseModel, EmailStr, Field

from tools.fakers import fake


class Token(BaseModel):
    """
    Структура данных токена авторизации.
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginRequestSchema(BaseModel):
    """
    Схема запроса для авторизации.
    """
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):
    """
    Схема ответа на аутентификации.
    """
    token: Token


class RefreshRequestSchema(BaseModel):
    """
    Схема запроса для обновления токена.
    """
    refresh_token: str = Field(alias='refreshToken', default_factory=fake.sentence)

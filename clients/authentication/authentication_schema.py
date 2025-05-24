from pydantic import BaseModel, EmailStr, Field, ConfigDict

from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Структура токена авторизации.
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginRequestSchema(BaseModel):
    """
    Схема запроса для авторизации.
    """
    model_config = ConfigDict(frozen=True)

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):
    """
    Схема ответа для авторизации.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Схема запроса для обновления токена.
    """
    refresh_token: str = Field(alias='refreshToken', default_factory=fake.sentence)


class RefreshResponseSchema(BaseModel):
    """
    Схема ответа для обновления токена.
    """
    token: TokenSchema
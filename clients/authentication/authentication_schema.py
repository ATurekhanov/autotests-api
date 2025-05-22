from pydantic import BaseModel, EmailStr, Field


class Token(BaseModel):
    """
    Структура данных токена авторизации.
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginRequestSchema(BaseModel):
    """
    Структура данных пользователя для авторизации.
    """
    email: EmailStr
    password: str


class LoginResponseSchema(BaseModel):
    """
    Структура ответа на аутентификации.
    """
    token: Token


class RefreshRequestSchema(BaseModel):
    """
    Структура данных для обновления токена.
    """
    refresh_token: str = Field(alias='refreshToken')

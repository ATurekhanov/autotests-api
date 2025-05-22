from pydantic import BaseModel, EmailStr, Field, ConfigDict


class User(BaseModel):
    """
    Структура пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа создания пользователя.
    """
    user: User


class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса на создание пользователя.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры тела запроса на обновление данных пользователя.
    """
    email: EmailStr | None
    last_name: str | None = Field(alias='lastName')
    first_name: str | None = Field(alias='firstName')
    middle_name: str | None = Field(alias='middleName')

from pydantic import BaseModel, EmailStr, Field, ConfigDict

from tools.fakers import fake


class UserSchema(BaseModel):
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
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """
    Схема ответа получения пользователя.
    """
    user: UserSchema

class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса на создание пользователя.
    """
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str = Field(alias='middleName', default_factory=fake.middle_name)


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры тела запроса на обновление данных пользователя.
    """
    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str | None = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str | None = Field(alias='middleName', default_factory=fake.middle_name)
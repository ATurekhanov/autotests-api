from pydantic import BaseModel, EmailStr, Field

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


class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса для создания пользователя.
    """
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str = Field(alias='middleName', default_factory=fake.middle_name)


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа для создания пользователя.
    """
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """
    Схема ответа для получения пользователя.
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Схема запроса для обновления пользователя.
    """
    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias='lastName', default_factory=fake.last_name)
    first_name: str | None = Field(alias='firstName', default_factory=fake.first_name)
    middle_name: str | None = Field(alias='middleName', default_factory=fake.middle_name)


class UpdateUserResponseSchema(BaseModel):
    """
    Схема ответа для обновления пользователя.
    """
    user: UserSchema
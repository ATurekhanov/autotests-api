from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


class User(BaseModel):
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
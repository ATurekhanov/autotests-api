import uuid

from pydantic import BaseModel, EmailStr, Field, ConfigDict
from pydantic.alias_generators import to_camel

from tools.fakers import fake


'''
{
  "id": "string",
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
'''


class UserSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(alias='lastName', default='Doe')
    first_name: str = Field(alias='firstName', default='John')
    middle_name: str = Field(alias='middleName', default='Test')


class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str
    first_name: str
    middle_name: str


class CreateUserResponseSchema(BaseModel):
    user: UserSchema


test_user_schema = UserSchema()
print(test_user_schema)

test_create_user_request_schema = CreateUserRequestSchema.model_validate_json(
    '''
    {
      "email": "user@example.com",
      "password": "string",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
    '''
)
print(test_create_user_request_schema)

test_create_user_response_schema = CreateUserResponseSchema.model_validate_json(
    '''
    {
      "user": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
      }
    }
    '''
)
print(test_create_user_response_schema)

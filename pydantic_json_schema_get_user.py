from clients.authentication.authentication_schema import LoginRequestSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password='string',
    lastName='string',
    firstName='string',
    middleName='string'
)
create_user_response = public_users_client.create_user(create_user_request)

user = LoginRequestSchema(email=create_user_request.email, password=create_user_request.password)
private_users_client = get_private_users_client(user)

get_user_response = private_users_client.get_user_api(create_user_response.user.id)

validate_json_schema(instance=get_user_response.json(), schema=GetUserResponseSchema.model_json_schema())





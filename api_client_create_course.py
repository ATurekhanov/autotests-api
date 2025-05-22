from clients.authentication.authentication_schema import LoginRequestSchema
from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
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

authentication_user = LoginRequestSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename="example.png",
    directory="exercises",
    upload_file="./testdata/files/example.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCourseRequestSchema(
    title="QA",
    maxScore=100,
    minScore=0,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = course_client.create_course(create_course_request)
print('Create course data:', create_course_response)
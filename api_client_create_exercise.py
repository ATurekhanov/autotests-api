from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
files_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename="example.png",
    directory="exercises",
    upload_file="./testdata/files/example.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCourseRequestDict(
    title="QA",
    maxScore=100,
    minScore=0,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = course_client.create_course(create_course_request)
print('Create course data', create_course_response)

create_exercise_request = CreateExerciseRequestDict(
    title="test exercise",
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=0,  # Если передать значение None, то ошибка возникает,
                 # хотя в CreateExerciseRequestDict указано int | None
                 # Ошибка возникает внутри библиотеки httpx, ниже текст ошибки
                 # raise JSONDecodeError("Expecting value", s, err.value) from None
    orderIndex=9,
    description="description for test exercise",
    estimatedTime="1 day"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data', create_exercise_response)

import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(func_user: UserFixture) -> CoursesClient:
    return get_courses_client(func_user.authentication_user)


@pytest.fixture
def func_course(courses_client: CoursesClient, func_user: UserFixture, func_file: FileFixture) -> CourseFixture:
    request = CreateCourseRequestSchema(previewFileId=func_file.id, createdByUserId=func_user.id)
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)
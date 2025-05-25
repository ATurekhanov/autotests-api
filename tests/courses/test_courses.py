from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema, \
    UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, GetCoursesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_create_course_response, assert_update_course_response, \
    assert_get_courses_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
class TestCourse:
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create course")
    @allure.severity(Severity.BLOCKER)
    def test_create_course(
            self,
            courses_client: CoursesClient,
            func_user: UserFixture,
            func_file: FileFixture
    ):
        request = CreateCourseRequestSchema(
            previewFileId=func_file.id,
            createdByUserId=func_user.id
        )
        response = courses_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Update course")
    @allure.severity(Severity.CRITICAL)
    def test_update_course(self, courses_client: CoursesClient, func_course: CourseFixture):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(func_course.id, request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Get courses")
    @allure.severity(Severity.BLOCKER)
    def test_get_courses(self, courses_client: CoursesClient, func_course: CourseFixture):
        query = GetCoursesQuerySchema(user_id=func_course.response.course.created_by_user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [func_course.response])

        validate_json_schema(response.json(), response_data.model_json_schema())

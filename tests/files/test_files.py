from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from config import settings
from fixtures.files import FileFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.errors import assert_create_file_with_empty_filename_response, \
    assert_create_file_with_empty_directory_response, assert_create_file_with_empty_filename_and_directory_response, \
    assert_file_not_found_response, assert_get_file_with_incorrect_file_id_response
from tools.assertions.files import assert_create_file_response, assert_get_file_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.files
@allure.tag(AllureTag.REGRESSION, AllureTag.FILES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.FILES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.FILES)
class TestFiles:
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.title("Create file")
    @allure.severity(Severity.BLOCKER)
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file=settings.test_data.png_file)
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.title("Get file")
    @allure.severity(Severity.BLOCKER)
    def test_get_file(self, files_client: FilesClient, func_file: FileFixture):
        response = files_client.get_file_api(func_file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, func_file.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.title("Create file with empty filename")
    @allure.severity(Severity.NORMAL)
    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            filename="",
            upload_file=settings.test_data.png_file
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.title("Create file with empty directory")
    @allure.severity(Severity.NORMAL)
    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            directory="",
            upload_file=settings.test_data.png_file
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.title("Create file with empty filename and directory")
    @allure.severity(Severity.NORMAL)
    def test_create_file_with_empty_filename_and_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            filename="",
            directory="",
            upload_file=settings.test_data.png_file
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_and_directory_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    @allure.title("Delete file")
    @allure.severity(Severity.NORMAL)
    def test_delete_file(self, files_client: FilesClient, func_file: FileFixture):
        delete_response = files_client.delete_file_api(func_file.id)

        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = files_client.get_file_api(func_file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_file_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.title("Create file with incorrect file id")
    @allure.severity(Severity.NORMAL)
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient):
        incorrect_file_id = "incorrect-file-id"
        response = files_client.get_file_api(incorrect_file_id)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id_response(response_data, incorrect_file_id)

        validate_json_schema(response.json(), response_data.model_json_schema())
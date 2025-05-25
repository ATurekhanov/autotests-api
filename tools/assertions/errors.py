import allure

from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length


@allure.step("Check validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемому значению.

    :param actual: Фактическая ошибка.
    :param expected: Ожидаемая ошибка.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equal(actual.type, expected.type, 'type')
    assert_equal(actual.input, expected.input, 'input')
    assert_equal(actual.context, expected.context, 'context')
    assert_equal(actual.message, expected.message, 'message')
    assert_equal(actual.location, expected.location, 'location')

@allure.step("Check validation error response")
def assert_validation_error_response(actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema):
    """
    Проверяет, что объект ответа API с ошибками валидации (`ValidationErrorResponseSchema`)
    соответствует ожидаемому значению.

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_length(actual.details, expected.details, 'details')

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)

def assert_create_file_with_empty_fields(actual: ValidationErrorResponseSchema, names: list[str]):
    """
    Проверяет, что ответ на создание файла с пустыми значениями соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :param names: Список полей, у которых должны быть пустые значения.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=
        [
            ValidationErrorSchema(
                type="string_too_short",
                input='',
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", name]
            ) for name in names
        ]
    )
    assert_validation_error_response(actual, expected)

def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    assert_create_file_with_empty_fields(actual, ['filename'])

def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    assert_create_file_with_empty_fields(actual, ['directory'])

def assert_create_file_with_empty_filename_and_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла
    и с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    assert_create_file_with_empty_fields(actual, ['filename', 'directory'])

@allure.step("Check internal error response")
def assert_internal_error_response(
        actual: InternalErrorResponseSchema,
        expected: InternalErrorResponseSchema
):
    """
    Функция для проверки внутренней ошибки. Например, ошибки 404 (File not found).

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equal(actual.detail, expected.detail, "detail")

def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    expected = InternalErrorResponseSchema(detail='File not found')

    assert_equal(actual, expected, 'detail')

def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema, file_id: str):
    """
    Проверяет, что ответ на получение файла с невалидным значением file_id соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :param file_id: Невалидный идентификатор файла.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=
        [
            ValidationErrorSchema(
                type="uuid_parsing",
                input=file_id,
                context={"error": "invalid character: expected an optional \
prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"},
                message="Input should be a valid UUID, invalid character: expected an optional \
prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                location=["path", "file_id"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)

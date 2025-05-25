import allure

from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger

logger = get_logger("ERRORS_ASSERTIONS")


@allure.step("Check validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемому значению.

    :param actual: Фактическая ошибка.
    :param expected: Ожидаемая ошибка.
    :raises AssertionError: Если значения полей не совпадают.
    """
    logger.info('Check validation error')

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
    logger.info('Check validation error response')

    assert_length(actual.details, expected.details, 'details')

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)


@allure.step("Check create file with empty fields")
def assert_create_file_with_empty_fields(actual: ValidationErrorResponseSchema, names: list[str]):
    """
    Проверяет, что ответ на создание файла с пустыми значениями соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :param names: Список полей, у которых должны быть пустые значения.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info('Check create file with empty fields')

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


@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info('Check create file with empty filename response')

    assert_create_file_with_empty_fields(actual, ['filename'])


@allure.step("Check create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info('Check create file with empty directory response')

    assert_create_file_with_empty_fields(actual, ['directory'])


@allure.step("Check create file with empty filename and directory response")
def assert_create_file_with_empty_filename_and_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла
    и с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info('Check create file with empty filename and directory response')

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
    logger.info('Check internal error response')

    assert_equal(actual.detail, expected.detail, "detail")


@allure.step("Check file not found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    logger.info('Check file not found response')

    expected = InternalErrorResponseSchema(detail='File not found')

    assert_equal(actual, expected, 'detail')


@allure.step("Check get file with incorrect file id response")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema, file_id: str):
    """
    Проверяет, что ответ на получение файла с невалидным значением file_id соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :param file_id: Невалидный идентификатор файла.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info('Check get file with incorrect file id response')

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

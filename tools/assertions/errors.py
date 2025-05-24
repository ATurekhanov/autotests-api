from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length


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

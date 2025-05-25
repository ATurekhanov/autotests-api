from http import HTTPStatus
from typing import Any, Sized

import allure
import httpx
from tools.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")


@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    logger.info(f'Check that response status code equals to {expected}')

    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )


@allure.step("Check that {name} equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    logger.info(f'Check that "{name}" equals to {expected}')

    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}'
    )


@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    logger.info(f'Check that "{name}" is true')

    assert actual, (
        f'Incorrect value: {name}'
        f'Expected true value but got: {actual}'
    )


@allure.step("Check that file {url} is accessible")
def assert_file_is_accessible(url: str):
    """
    Проверяет, что файл доступен по указанному URL.

    :param url: Ссылка на файл.
    :raises AssertionError: Если файл не доступен.
    """
    logger.info(f'Check that file {url} is accessible')

    response = httpx.get(url)
    assert response.status_code == HTTPStatus.OK, f"Файл недоступен по URL: {url}"


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что фактическая длина равна ожидаемой.

    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :param name: Название проверяемого значения.
    :raises AssertionError: Если длина не совпадает.
    """

    with allure.step(f'Check that length of {name} equals to {len(expected)}'):
        logger.info(f'Check that length of "{name}" equals to {len(expected)}')

        assert len(actual) == len(expected), (
            f'Incorrect object length: "{name}". '
            f'Expected length: {len(expected)}. '
            f'Actual length: {len(actual)}'
        )

from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator


@allure.step("Check JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema).

    :param instance: JSON-данные, которые нужно проверить.
    :param schema: Ожидаемая JSON-schema.
    :raises jsonschema.exceptions.ValidationError: Если instance не соответствует schema.
    """
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )
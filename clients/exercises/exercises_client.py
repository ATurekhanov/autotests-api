import allure
from httpx import Response

from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
    CreateExerciseRequestSchema,
    UpdateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
    UpdateExerciseResponseSchema
)
from clients.private_http_builder import get_private_http_client
from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises.
    """

    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения упражнений по идентификатору курса.
        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(url=APIRoutes.EXERCISES, params=query.model_dump(by_alias=True))

    @allure.step("Get exercise by {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения по идентификатору упражнения.
        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post(url=APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by {exercise_id}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения по идентификатору упражнения.
        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.patch(
            f"{APIRoutes.EXERCISES}/{exercise_id}",
            json=request.model_dump(by_alias=True, exclude_none=True)
        )

    @allure.step("Delete exercise by {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения по идентификатору упражнения.
        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: LoginRequestSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))

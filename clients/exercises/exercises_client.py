from typing import TypedDict, NotRequired, Required

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class ExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения/создания/обновления упражнения.
    """
    exercise: Exercise
    # Могу ли я использовать один ExerciseResponseDict для get/post/put запросов?
    # По сваггеру у них одна схема в ответах и чтоб не создавать одинаковые словари
    # GetExerciseResponseDict, CreateExerciseResponseDict, UpdateExerciseResponseDict
    # Можно ли создать 1 словарь ExerciseResponseDict? Аналогичный вопрос и касательно других клиентов


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры query параметров запроса на получение списка курсов.
    """
    courseId: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка упражнений.
    """
    exercises: list[Exercise]


class CreateExerciseRequestDict(TypedDict, total=False):
    """
    Описание структуры тела запроса на создание упражнения.
    """
    title: Required[str]
    courseId: Required[str]
    maxScore: Required[int | None]
    minScore: Required[int | None]
    orderIndex: NotRequired[int]
    description: Required[str]
    estimatedTime: Required[str | None]


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры тела запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises.
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения упражнений по идентификатору курса.
        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения по идентификатору упражнения.
        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения по идентификатору упражнения.
        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения по идентификатору упражнения.
        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> ExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> ExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> ExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))

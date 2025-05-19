from typing import TypedDict, NotRequired, Required

from httpx import Response

from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры query параметров запроса на получение списка курсов.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры тела запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: Required[int | None]  # По сваггеру это поле принимает int или None и обязательное
    # Указал Required/NotRequired, но вроде это не работает. Если подскажете как в таких
    # случаях нужно делать в условиях когда обязательно нужен TypedDict буду очень признателен.
    minScore: Required[int | None]  # По сваггеру это поле принимает int или None и обязательное
    orderIndex: NotRequired[int]  # По сваггеру это поле принимает только int и опциональное
    description: str
    estimatedTime: Required[str | None]  # По сваггеру это поле принимает str или None и обязательное


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

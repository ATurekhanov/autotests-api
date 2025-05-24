import pytest
from pydantic import BaseModel, ConfigDict

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    model_config = ConfigDict(populate_by_name=True)


    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

    @property
    def id(self):
        return self.response.exercise.id

    @property
    def course_id(self):
        return self.response.exercise.course_id


@pytest.fixture
def exercises_client(func_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(func_user.authentication_user)


@pytest.fixture
def func_exercise(exercises_client: ExercisesClient, func_course: FileFixture) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(courseId=func_course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)

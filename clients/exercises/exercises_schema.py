from pydantic import BaseModel, Field

from tools.fakers import fake


class ExerciseSchema(BaseModel):
    """
    Структура упражнения.
    """
    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str | None = Field(alias='estimatedTime')


class CreateExerciseRequestSchema(BaseModel):
    """
    Схема запроса для создания упражнения.
    """
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias='courseId', default_factory=fake.uuid4)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int = Field(alias='orderIndex', default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


class CreateExerciseResponseSchema(BaseModel):
    """
    Схема ответа для создания упражнения.
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """
    Схема query-параметров запроса для получения списка упражнений.
    """
    course_id: str = Field(alias='courseId')


class GetExercisesResponseSchema(BaseModel):
    """
    Схема ответа для получения списка упражнений.
    """
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Схема ответа для получения упражнения.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Схема запроса для обновления упражнения.
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int | None = Field(alias='orderIndex', default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


class UpdateExerciseResponseSchema(BaseModel):
    """
    Схема ответа для обновления упражнения.
    """
    exercise: ExerciseSchema
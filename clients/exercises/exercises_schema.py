from pydantic import BaseModel, Field


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str | None = Field(alias='estimatedTime')


class ExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения/создания/обновления упражнения.
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры query параметров запроса на получение списка курсов.
    """
    course_id: str = Field(alias='courseId')


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка упражнений.
    """
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры тела запроса на создание упражнения.
    """
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str | None = Field(alias='estimatedTime')


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры тела запроса на обновление упражнения.
    """
    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int | None = Field(alias='orderIndex')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')

from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
    """
    Структура курса.
    """
    id: str
    title: str
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    description: str
    preview_file: FileSchema = Field(alias='previewFile')
    estimated_time: str | None = Field(alias='estimatedTime')
    created_by_user: UserSchema = Field(alias='createdByUser')


class CreateCourseRequestSchema(BaseModel):
    """
    Схема запроса для создания курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    preview_file_id: str = Field(alias='previewFileId', default_factory=fake.uuid4)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)
    created_by_user_id: str = Field(alias='createdByUserId', default_factory=fake.uuid4)


class CreateCourseResponseSchema(BaseModel):
    """
    Схема ответа для создания курса.
    """
    course: CourseSchema


class GetCoursesQuerySchema(BaseModel):
    """
    Схема query-параметров запроса для получения списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')


class GetCoursesResponseSchema(BaseModel):
    """
    Схема ответа для получения списка курсов.
    """
    courses: list[CourseSchema]


class GetCourseResponseSchema(BaseModel):
    """
    Схема ответа для получения курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Схема запроса для обновления курса.
    """

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


class UpdateCourseResponseSchema(BaseModel):
    """
    Схема ответа для обновления курса.
    """
    course: CourseSchema
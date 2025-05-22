from pydantic import BaseModel, Field

from clients.files.files_schema import File
from clients.users.users_schema import User


class Course(BaseModel):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    description: str
    preview_file: File = Field(alias='previewFile')
    estimated_time: str | None = Field(alias='estimatedTime')
    created_by_user: User = Field(alias='createdByUser')


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры query параметров запроса на получение списка курсов.
    """
    user_id: str = Field(alias='userId')


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    description: str
    preview_file_id: str = Field(alias='previewFileId')
    estimated_time: str | None = Field(alias='estimatedTime')
    created_by_user_id: str = Field(alias='createdByUserId')


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: Course


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """

    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')
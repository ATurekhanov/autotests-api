from pydantic import BaseModel, HttpUrl, Field

from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Структура файла.
    """
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileRequestSchema(BaseModel):
    """
    Схема запроса для создания файла.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    Схема ответа для создания файла.
    """
    file: FileSchema


class GetFileResponseSchema(BaseModel):
    """
    Схема ответа для получения файла.
    """
    file: FileSchema

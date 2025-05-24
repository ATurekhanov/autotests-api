import pytest
from pydantic import BaseModel

from clients.files.files_client import FilesClient, get_files_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture


class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

    @property
    def id(self) -> str:
        return self.response.file.id


@pytest.fixture
def files_client(func_user: UserFixture) -> FilesClient:
    return get_files_client(func_user.authentication_user)



@pytest.fixture
def func_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file='./testdata/files/example.png')
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)
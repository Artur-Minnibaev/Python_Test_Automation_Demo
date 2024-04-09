from pydantic import BaseModel, field_validator


class Books(BaseModel):
    isbn: str
    title: str
    subTitle: str
    author: str
    publisher: str
    description: str
    website: str


class AccountModel(BaseModel):
    userID: str
    username: str
    books: list[Books]


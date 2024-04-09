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

    @field_validator("userID", "username", "books")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

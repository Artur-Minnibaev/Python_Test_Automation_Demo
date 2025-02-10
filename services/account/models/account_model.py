from pydantic import BaseModel, field_validator, Field


class Books(BaseModel):
    isbn: str
    title: str
    subTitle: str
    author: str
    publisher: str
    description: str
    website: str


class AccountModel(BaseModel):
    userID: str = Field(None, alias='userID')
    userId: str = Field(None, alias="userId")
    username: str
    books: list[Books]

    @field_validator("userID", "username", "books")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

    @property
    def normalized_user_id(self):
        return self.userID or self.userId

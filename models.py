from sqlmodel import Field, Session, SQLModel, select


class User(SQLModel):
    name: str
    age: int | None
    isDisabled: bool


class UserInDB(User, table=True):
    id: int | None = Field(default=None, primary_key=True)

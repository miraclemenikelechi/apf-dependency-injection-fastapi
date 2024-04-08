from sqlmodel import Field, SQLModel, select


class User(SQLModel):
    name: str
    age: int | None
    isDisabled: bool


class UserInDB(User, table=True):
    id: int | None = Field(default=None, primary_key=True)


# class Car(SQLModel):
#     name: str
#     color: str
#     year: int


# class DB_Car(Car, table=True):
#     id: int | None = Field(default=None, primary_key=True)

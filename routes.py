from typing import Annotated

from fastapi import APIRouter, Depends

from controllers import create_new_user
from dependencies import get_session
from models import Session, User

user = APIRouter(prefix="/users", tags=["users"])


@user.post("/new")
async def create_user(user: User, session: Annotated[Session, Depends(get_session)]):
    data = await create_new_user(user, session)

    return data


# @user.get("/all")
# async def get_all_users(session: Annotated[Session, Depends(get_session)]):
#     data = await get_all_users(session)

#     return data

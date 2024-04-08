from models import User, UserInDB, select


async def create_new_user(user, session):

    new_user_in_db = UserInDB(name=user.name, age=user.age, isDisabled=user.isDisabled)

    session.add(new_user_in_db)
    session.commit()

    new_user: User = {
        "name": user.name,
        "age": user.age,
        "isDisabled": user.isDisabled,
    }

    return new_user


async def get_all_users(session):
    
    all_users = session.exec(select(UserInDB)).all()

    return all_users

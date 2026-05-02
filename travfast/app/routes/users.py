import uuid
from fastapi import APIRouter
from app.storage import load_data, save_data
from app.schemas import User, UserAuth

router = APIRouter(prefix="/api/v1/users", tags=["users"])

# Get All users
@router.get("/")
def get_users():
    users = load_data("users.json")
    return users

# create user
@router.post("/")
async def create_user(payload: User):
    users = load_data("users.json")
    new_user = {
        "id": str(uuid.uuid4()),
        "name": payload.name,
        "email": payload.email,
        "password": payload.password,
        "username": payload.username,
        "user_type": payload.user_type,
    }
    users.append(new_user)
    save_data(users, "users.json")
    return new_user


# user auth
@router.post("/auth")
async def user_auth(payload:UserAuth):
    users = load_data("users.json")
    for index, user in enumerate(users):
        if payload.username is not None or payload.email is not None:
            if user["username"] == payload.username or user["email"] == payload.email:
                current_user = users[index]
                if current_user["password"] == payload.password:
                    print("Authenticated")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
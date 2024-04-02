# Multiple Models
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None=None


class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass
class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User Saved! Not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    print(user_saved.dict())
    return user_saved


user_in = UserIn(username="john", password="johnsecret", email="john.doe@example.com")
print(user_in.dict())
# print(fake_password_hasher(user_in.password))
#
# print(fake_save_user(user_in))




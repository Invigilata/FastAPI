from fastapi import FastAPI

app = FastAPI()

# Главная страница
@app.get("/")
async def get_main_page():
    return {"message": "Главная страница"}

# Страница администратора
@app.get("/user/admin")
async def get_admin_page():
    return {"message": "Вы вошли как администратор"}

# Страница пользователя с параметром user_id
@app.get("/user/{user_id}")
async def get_user_page(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Страница пользователя с именем и возрастом в адресной строке
@app.get("/user")
async def get_user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
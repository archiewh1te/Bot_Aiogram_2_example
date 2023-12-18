from  asyncpg import UniqueViolationError

from utils.db_api.schemas.users import create_users



# Быстрые команды создания пользователя в БД
async def add_users(user_id: int, first_name: str, last_name: str, user_name: str, status: str):
    try:
        add_user = create_users(user_id=user_id, first_name=first_name, last_name=last_name, user_name=user_name, status=status)
        await add_user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


# Функция которая получает всех админов которые есть в БД
async def select_all_users():
    users = await create_users.query.gino.all()
    return users


# Функция которая выбирает пользователя из БД по user_id
async def select_user(user_id):
    user = await create_users.query.where(create_users.user_id == user_id).gino.first()
    return user


# Функция которая обновляет юзернейм
async def update_user_name(user_id, new_name):
    user = await select_user(user_id)
    await user.update(update_name=new_name).apply()


# Функция которая удаляет Пользователя из БД
async def delete_user(user_id):
    user = await select_user(user_id)
    await user.delete()
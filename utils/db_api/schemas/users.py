from utils.db_api.db_base import TimedBaseModel

from sqlalchemy import Column, BigInteger, String, sql


# Создание таблицы юзеров
class create_users(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    user_name = Column(String(100))
    status = Column(String(30))

    query: sql.select
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.String)
    speciality = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, default='')

    # были проблемы в задачах из-за него, и в основном его не используют:
    # modified_date = sqlalchemy.Column(sqlalchemy.DateTime)

    def __init__(self, surname, name, age, position, speciality, address, email, hashed_password):
        self.surname = surname
        self.name = name
        self.age = age
        self.position = position
        self.speciality = speciality
        self.address = address
        self.email = email
        self.hashed_password = hashed_password

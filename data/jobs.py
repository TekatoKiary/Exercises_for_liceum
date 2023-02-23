import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.Date, default=None)
    end_date = sqlalchemy.Column(sqlalchemy.Date, default=None)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)
    user = orm.relationship('User')

    def __init__(self, team_leader, job, work_size, collaborators, start_date, end_date, is_finished):
        self.team_leader = team_leader
        self.job = job
        self.work_size = work_size
        self.collaborators = collaborators
        if start_date:
            self.start_date = start_date
        if end_date:
            self.end_date = end_date
        self.is_finished = is_finished

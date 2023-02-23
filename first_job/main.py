import datetime

import sqlalchemy
from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("data/db/mars_explorer.sqlite")

    db_sess = db_session.create_session()

    add_user(db_sess, 'Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org', '')
    add_user(db_sess, 'Rick', 'Cooper', 35, 'assistant', 'middle engineer', 'module_1', 'Mister_Cooper@mars.org', '156')
    add_user(db_sess, 'Sara', 'Schmidt', 27, 'chief', 'design engineer', 'module_1', 'SaraConor@mars.org', 'I’llBeBack')
    add_user(db_sess, 'Jack', 'Parrot', 15, 'assistant', 'researcher', 'module_1', 'JackSparrow@mars.org', 'Savvy')

    add_jobs(db_sess, 1, 'deployment of residential modules 1 and 2', 15, '2, 3', datetime.date.today(), '', False)

    db_sess.commit()

    app.run()


def add_user(db_sess, surname, name, age, position, speciality, address, email, hashed_password):
    user = User(surname, name, age, position, speciality, address, email, hashed_password)
    db_sess.add(user)


def add_jobs(db_sess, team_leader, job, work_size, collaborators, start_date, end_date, is_finished):
    job = Jobs(team_leader, job, work_size, collaborators, start_date, end_date, is_finished)
    db_sess.add(job)


if __name__ == '__main__':
    main()

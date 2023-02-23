import datetime
from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("data/db/mars_explorer.sqlite")
    if not os.access('data/db/mars_explorer.sqlite', os.F_OK):
        db_sess = db_session.create_session()
        add_user(db_sess, 'Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org', '')
        add_user(db_sess, 'Rick', 'Cooper', 35, 'assistant', 'middle engineer', 'module_1', 'Mister_Cooper@mars.org',
                 '156')
        add_user(db_sess, 'Sara', 'Schmidt', 27, 'chief', 'design engineer', 'module_1', 'SaraConor@mars.org',
                 'I’llBeBack')
        add_user(db_sess, 'Jack', 'Parrot', 15, 'assistant', 'researcher', 'module_1', 'JackSparrow@mars.org', 'Savvy')

        add_jobs(db_sess, 1, 'deployment of residential modules 1 and 2', 15, '2, 3', datetime.date.today(), False)
        add_jobs(db_sess, 4, 'deployment of residential modules 2 and 3', 55, '2', datetime.date.today(), True)
        db_sess.commit()
    app.run(port=8080, host='127.0.0.1')


def add_user(db_sess, surname, name, age, position, speciality, address, email, hashed_password):
    user = User(surname, name, age, position, speciality, address, email, hashed_password)
    db_sess.add(user)


def add_jobs(db_sess, team_leader, job, work_size, collaborators, start_date, is_finished):
    job = Jobs(team_leader, job, work_size, collaborators, start_date, is_finished)
    db_sess.add(job)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("works_log.html", jobs=jobs)


if __name__ == '__main__':
    main()

import datetime

from flask import Flask, render_template, redirect
from data import db_session, users_resources
from data.__all_models import User, Jobs
import os
from flask_login import LoginManager, login_user, login_required, logout_user
from forms.user import UserRegisterForm
from forms.job import JobRegisterForm
from forms.login import LoginForm
from flask_restful import Api

is_create_sql_flie = os.access('data/db/mars_explorer.sqlite', os.F_OK)


def add_user(db_sess, surname, name, age, position, speciality, address, email, password):
    user = User(surname, name, age, position, speciality, address, email)
    user.set_password(password)
    db_sess.add(user)


def add_jobs(db_sess, team_leader, job, work_size, collaborators, start_date, is_finished):
    job = Jobs(team_leader, job, work_size, collaborators, start_date, is_finished)
    db_sess.add(job)


db_session.global_init("data/db/mars_explorer.sqlite")

# if not is_create_sql_flie:
#     db_sess = db_session.create_session()
#     add_user(db_sess, 'Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org', '')
#     add_user(db_sess, 'Rick', 'Cooper', 35, 'assistant', 'middle engineer', 'module_1', 'Mister_Cooper@mars.org',
#              '156')
#     add_user(db_sess, 'Sara', 'Schmidt', 27, 'chief', 'design engineer', 'module_1', 'SaraConor@mars.org',
#              'I’llBeBack')
#     add_user(db_sess, 'Jack', 'Parrot', 15, 'assistant', 'researcher', 'module_1', 'JackSparrow@mars.org', 'Savvy')
#
#     add_jobs(db_sess, 1, 'deployment of residential modules 1 and 2', 15, '2, 3', datetime.date.today(), False)
#     add_jobs(db_sess, 4, 'deployment of residential modules 2 and 3', 55, '2', datetime.date.today(), True)
#     db_sess.commit()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
api = Api(app)
api.add_resource(users_resources.UsersListResource, '/api/v2/user')
api.add_resource(users_resources.UserResource, '/api/v2/user/<int:user_id>')


def main():
    app.run(port=8080, host='127.0.0.1')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    return render_template("main_page.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = UserRegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            address=form.address.data,
            speciality=form.speciality.data,
            position=form.position.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/addjob', methods=['GET', 'POST'])
def add_job():
    form = JobRegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(team_leader=form.id_teamlead.data,
                   job=form.job_title.data,
                   work_size=form.work_size.data,
                   collaborators=form.collaborators.data,
                   start_date=datetime.date.today(),
                   is_finished=form.is_finished.data)
        db_sess.add(job)
        db_sess.commit()
        return redirect('/works_log')
    return render_template('add_job.html', title='Добавление Работы', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/works_log")
def works_log():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("works_log.html", jobs=jobs)


if __name__ == '__main__':
    main()

from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
import os
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired
from forms.user import RegisterForm

is_create_sql_flie = os.access('data/db/mars_explorer.sqlite', os.F_OK)


def add_user(db_sess, surname, name, age, position, speciality, address, email, password):
    user = User(surname, name, age, position, speciality, address, email)
    user.set_password(password)
    db_sess.add(user)


db_session.global_init("data/db/mars_explorer.sqlite")

if not is_create_sql_flie:
    db_sess = db_session.create_session()
    add_user(db_sess, 'Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org', '')
    add_user(db_sess, 'Rick', 'Cooper', 35, 'assistant', 'middle engineer', 'module_1', 'Mister_Cooper@mars.org',
             '156')
    add_user(db_sess, 'Sara', 'Schmidt', 27, 'chief', 'design engineer', 'module_1', 'SaraConor@mars.org',
             'I’llBeBack')
    add_user(db_sess, 'Jack', 'Parrot', 15, 'assistant', 'researcher', 'module_1', 'JackSparrow@mars.org', 'Savvy')

    db_sess.commit()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    app.run(port=8080, host='127.0.0.1')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route("/")
def index():
    return render_template("base.html")


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
    form = RegisterForm()
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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()

import os.path
import random
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__, static_folder=os.path.abspath('static'))

PROFESSIONS = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, климатолог, ' \
              'специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, ' \
              'оператор марсохода, киберинженер, штурман, пилот дронов'.split(', ')
MALE_NAMES = 'Anthony Bryan Carl Daniel Ethan Francis Mark'.split()
FEMALE_NAMES = 'Ava Barbara Catherine Deborah Elizabeth Florence'.split()

SURNAMES = 'Gerald Harrison Jones MacAlister Carroll Fitzgerald Ferguson Simpson Turner Murphy Dickinson'.split()
EDUCATIONS = 'Среднее Высшее Начальное Профессиональное'.split()
SEX = 'Мужчина Женщина Робот Ламинат'.split()  # ламинат добавил по просьбе друга
MOTIVATIONS = [
    'Всегда мечтал застрять на Марсе!', 'Хочу убежать от земных проблем',
    'Мне сказали, что во время экспедиции будут бесплатные конфеты',
    'Я люблю огород, но места для участка на земле заканчиваются, вследствие дорожают цены на них. '
    'А на Марсе полно места и при этом бесплатно', 'Я хочу участвовать в терраформирование брата Земли, Марса',
    'Моя главная мечта - протянуть провод от Земли до Марса, что поможет колонизации не только '
    'разговаривать с родственниками, но и искать ответы в интернете'
]

COLORS = {'pink': '#FFC0CB',
          'purple': '#800080',
          'blue': ' #0000ff',
          'lightblue': '#add8e6'}

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_astronaut = StringField('Id астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_captain = StringField('Id капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/list_prof/<type_list>')
def list_prof(type_list):
    if type_list in ['ul', 'ol']:
        return render_template('list_prof.html', type_list=type_list)
    else:
        return render_template('base.html', error='Неправильный адрес')


@app.route('/auto_answer')
@app.route('/answer')
def auto_answer():
    param = dict()
    param['title'] = 'Анкета'
    param['surname'] = random.choice(SURNAMES)
    param['name'] = random.choice(MALE_NAMES + FEMALE_NAMES)
    param['education'] = random.choice(EDUCATIONS)
    param['profession'] = random.choice(PROFESSIONS)
    param['sex'] = random.choice(SEX)
    if param['sex'] in 'Мужчина Женщина'.split():
        param['sex'] = 'Женщина' if param['name'] in FEMALE_NAMES else 'Мужчина'
    param['motivation'] = random.choice(MOTIVATIONS)
    param['ready'] = random.choice([True, False])

    return render_template('auto_answer.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/distribution')
def distribution():
    person_list = []
    for i in range(random.randint(5, 15)):
        name = random.choice(MALE_NAMES + FEMALE_NAMES) + ' ' + random.choice(SURNAMES)
        person_list.append(name)
    return render_template('distribution.html', people_list=person_list)


@app.route('/table/<sex>/<age>')
def cabin_decoration(sex, age):
    age = int(age)
    image = url_for('static', filename='img/Martian-adult.jpg') if age > 21 else \
        url_for('static', filename='img/Martian-child.jpg')
    if sex == 'male':
        color = COLORS['blue'] if age > 21 else COLORS['lightblue']
    else:
        color = COLORS['purple'] if age > 21 else COLORS['pink']
    return render_template('cabin_decoration.html', image=image, color=color)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

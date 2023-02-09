import random

from flask import Flask, render_template

app = Flask(__name__)

PROFESSIONS = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, климатолог, ' \
              'специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, ' \
              'оператор марсохода, киберинженер, штурман, пилот дронов'.split(', ')
MALE_NAMES = 'Anthony Bryan Carl Daniel  Ethan Francis Mark'.split()
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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

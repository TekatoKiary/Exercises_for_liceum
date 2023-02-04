import random

from flask import Flask, url_for, request

app = Flask(__name__)

PLANETS = {
    'Марс': 'Эта планета близка к Земле;\nНа ней много необходимых ресурсов;\nНа ней есть вода и атмосфера;\n'
            'На ней есть небольшое магнитное поле;\nНаконец, она просто красива!',
    'Титан': 'Спутник Сатурна;\nАтмосфера преимущественно состоит из азота;\nНизкая температура(-170;-180);\n'
             'Давление у поверхности примерно в 1,5 раза превышает давление земной атмосферы;\n'
             'Возможно существование простейших форм жизни',
    'Луна': 'Спутник Земли;\nМы уже бывали там;\nНет воды и атмосферыж\nОтличное место для создания космической базы'
}

ALERTS = ['primary', 'dismissible', 'heading', 'link', 'success', 'secondary', 'danger', 'dark']


@app.route('/')
def main_menu():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    text = """Человечество вырастает из детства.

    Человечеству мала одна планета.

    Мы сделаем обитаемыми безжизненные пока планеты.

    И начнем с Марса!

    Присоединяйся!""".split('\n')
    return '</br>'.join(text)


@app.route('/image_mars')
def image_mars():
    return f'''<title>Привет, Марс!</title>
    <h1>Жди нас, Марс</h1>
    <img src="{url_for('static', filename='img/mars.jpeg')}" alt="здесь должна была быть картинка, но не нашлась"/>
    <br>Придет время и Мы тебя колонизируем.'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс</h1>
                    <img src="{url_for('static', filename='img/mars.jpeg')}" alt="здесь должна быть картинка, 
                    но не нашлась"/>
                    <div class="alert alert-info" role="alert">
                        Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-dark" role="root">
                        Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-warning" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="root">
                        И начнем с Марса!
                    </div>
                    <div class="alert alert-primary" role="root">
                        Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        professions = create_professions()
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"
                            />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="lastname" class="form-control" id="lastname" 
                                    aria-describedby="lastnameHelp" placeholder="Введите фамилию" name="lastname">
                                    <input type="name" class="form-control" id="name" 
                                    aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" 
                                    placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="educationSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Профессиональное</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <br>
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                        {professions}
                                    </div>
                                    <div class="form-group">
                                        <br>    
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" 
                                          value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" 
                                          value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-check">
                                        <br>
                                          <input class="form-check-input" type="checkbox" name="is_ready" id="is_ready" 
                                          value="True">
                                          <label class="form-check-label" for="female">
                                            Готовы ли Вы остаться на Марсе?
                                          </label>
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        name = request.form['lastname'] + ' ' + request.form['name']
        rating = 0
        for i in ['profession', 'about', 'is_ready']:
            try:
                if request.form[i]:
                    rating += 1
            except Exception:
                rating += 0
        education = request.form['education']
        if education == 'Начальное':
            rating += 1
        elif education == 'Среднее':
            rating += 2
        else:
            rating += 3
        app.redirect('http://localhost:8080/results/<nickname>/<level>/<rating>')
        return results(name, random.randint(1, 3), rating / 6 * 100)


def create_professions():
    text_list = []
    english_professions = 'research engineer, pilot, builder, exobiologist, doctor, terraforming engineer, ' \
                          'climatologist, radiation protection specialist, astrogeologist, glaciologist, ' \
                          'life support engineer, meteorologist, rover operator, cyber engineer, navigator, ' \
                          'drone pilot'.split(', ')
    russian_professions = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, ' \
                          'климатолог, специалист по радиационной защите, астрогеолог, гляциолог, ' \
                          'инженер жизнеобеспечения, метеоролог, оператор марсохода, киберинженер, штурман, ' \
                          'пилот дронов'.split(', ')  # русский перевод. Если развивать список, то лучше сделать словарь
    for i in range(len(english_professions)):
        text_list.append(f'''<div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id={english_professions[i]}" 
                                        name="profession", value="{english_professions[i]}">
                                        <label class="form-check-label" for="{english_professions[i]}">
                                    {russian_professions[i].capitalize()}</label>
                                    </div>''')
    return '\n'.join(text_list)


@app.route('/choice/<username>')
def choice(username):
    text = ''
    for i in PLANETS[username].split('\n'):
        level = random.randint(0, 7)
        text += f'<h{level} class="alert alert-{random.choice(ALERTS)}" role="alert">' + i + f'</h{level}>\n'

    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {username}</h1>
                    {text}
                  </body>
                </html>'''


@app.route('/results/<nickname>/<level>/<rating>')
def results(nickname='null', level=1, rating=50.0):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Пример формы</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h3>Претендента на участие в миссии {nickname}</h3>
                        {f'<h3 class="alert alert-success" role="alert">Поздравляем! '
                         f'Ваш рейтинг после {level} этапа отбора' if rating > 25 else
    f'<h3 class="alert alert-danger" role="alert">К сожалению, Вы не прошли отбор, ваш рейтинг'}</h3>
                        <h3>составляет {rating}!</h3>
                        <h3 class="alert alert-warning" role="alert">Желаем удачи!</h3>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

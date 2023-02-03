from flask import Flask, url_for

app = Flask(__name__)


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
    <img src="{url_for('static', filename='img/mars.jpeg')}" alt="здесь должна была быть картинка, но не нашлась"\>
    <br>Придет время и Мы тебя колонизируем.'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

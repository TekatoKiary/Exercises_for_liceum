from flask import Flask, render_template

app = Flask(__name__)

PROFESSIONS = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, климатолог, ' \
              'специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, ' \
              'оператор марсохода, киберинженер, штурман, пилот дронов'.split(', ')


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

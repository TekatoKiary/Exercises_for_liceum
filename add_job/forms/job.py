from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class JobRegisterForm(FlaskForm):
    job_title = StringField('Название работы', validators=[DataRequired()])
    id_teamlead = StringField('Id Лидера команды', validators=[DataRequired()])
    work_size = IntegerField('Количество часов работы', validators=[DataRequired()])
    collaborators = StringField('Коллабораторы', validators=[DataRequired()])
    is_finished = BooleanField('Работа завершена?')
    submit = SubmitField('Добавить')

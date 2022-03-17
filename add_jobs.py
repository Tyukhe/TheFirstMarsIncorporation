from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired


class AddJob(FlaskForm):
    team_leader = IntegerField('Лидер', validators=[DataRequired()])
    job = StringField('Имя работы', validators=[DataRequired()])
    work_size = IntegerField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Сотрудники', validators=[DataRequired()])
    start_date = DateField('Начало работ', validators=[DataRequired()])
    end_date = DateField('Окончание работ', validators=[DataRequired()])
    submit = SubmitField('Добавить', validators=[DataRequired()])

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired


class EditJob(FlaskForm):
    job = StringField('Имя работы', validators=[DataRequired()])
    work_size = IntegerField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Сотрудники', validators=[DataRequired()])
    start_date = DateField('Начало работ', validators=[DataRequired()])
    end_date = DateField('Окончание работ', validators=[DataRequired()])
    submit = SubmitField('Изменить', validators=[DataRequired()])
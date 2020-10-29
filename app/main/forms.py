from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import Required

class TodoForm(FlaskForm):
    category = SelectField('Category', choices=[ ('Personal', 'Personal'), ('Work', 'Work')],validators=[Required()])
    description = TextAreaField('Description', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself!', validators=[Required()])
    submit = SubmitField('Submit')

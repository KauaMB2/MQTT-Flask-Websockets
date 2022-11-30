from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    searched=StringField(label='Search here...', validators=[DataRequired()])
    submit=SubmitField(label='Search!')

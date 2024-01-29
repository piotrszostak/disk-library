from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import NumberRange

class RecordForm(FlaskForm):
    name = StringField("name")
    author = StringField("author")
    year = IntegerField("year", validators=[NumberRange(min=0, max=2025, message="Year must be positive.")])
    
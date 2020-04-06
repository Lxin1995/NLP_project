from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class FeatureForm(FlaskForm):
    review_text = StringField('Review Text')   ##This field is the base for most of the more complicated fields, and represents an <input type="text">.
    go = SubmitField('Submit')     ##Represents an <input type="submit">. This allows checking if a given submit button has been pressed.

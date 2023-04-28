from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating out of 10 e.g. 7.4', validators=[DataRequired()])
    review = StringField('Your Review')
    submit = SubmitField('Submit')


class AddMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')
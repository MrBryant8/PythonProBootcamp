from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
Bootstrap(app)

wifi = ['✘']
wifi.extend(['{}'.format("⭐" * i) for i in range(1, 6)])

power = ['✘']
power.extend(['{}'.format("🔌" * i) for i in range(1, 6)])


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])

    location = StringField('Cafe location on Google Maps',
                           validators=[DataRequired(), URL()])

    opening_time = StringField('Opening time e.g. 9AM',
                               validators=[DataRequired()])

    closing_time = StringField('Closing  time e.g. 7PM',
                               validators=[DataRequired()])

    coffee_rating = SelectField('Coffee rating',
                                choices=['{}'.format("☕"*i) for i in range(1, 6)],
                                validators=[DataRequired()])

    wifi_rating = SelectField('Wifi Strength Rating',
                              choices=wifi,
                              validators=[DataRequired()])

    power_socket = SelectField('Power Socket Availability',
                               choices=power,
                               validators=[DataRequired()])

    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", 'a', encoding="UTF-8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.opening_time.data},"
                           f"{form.closing_time.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_socket.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='UTF-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

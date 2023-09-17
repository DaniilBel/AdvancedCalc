import datetime
import re

from flask import Flask, request, render_template, redirect, url_for, flash

from database.model.calc_history import History
from database.repository.history_repository import HistoryRepository

app = Flask(__name__)
app.secret_key = "KADadbjhaOW&^*FTYG*WGXjskBSJLHBasnk"
app.debug = True


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


@app.route('/')
def index():
    return render_template('index.html', history=history.get_history())


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['display']

    if re.fullmatch(r"\A[()0-9+*/^%.-]*\Z", expression) is None:
        flash("There is unsupported symbols in request!")
    if len(re.findall(r"(?:[+*/^%-]--)|(?:\+\+\+)|(?://)|(?:\*\*)", expression)) != 0:
        flash("There is unsupported combination of symbols in request!")
    try:
        result = eval(expression.replace("^", "**"))
        history.add_history(History(expression, result, str(datetime.datetime.now())))
    except ZeroDivisionError:
        result = ""
        flash("Division by zero found!")

    return render_template('index.html', history=history.get_history(), result=result)


@app.route('/clear', methods=['POST'])
def history_clear():
    history.clear_history()
    return redirect(url_for("index"), 301)


if __name__ == '__main__':
    history = HistoryRepository()
    app.run()

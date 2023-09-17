import datetime
import re

from flask import Flask, request, render_template, redirect, url_for

from database.model.calc_history import History
from database.repository.history_repository import HistoryRepository

app = Flask(__name__)
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

    # потом нормально обработать исключения с выводом сообщения в окне
    if re.fullmatch(r"\A[()0-9+*/^%.-]*\Z", expression) is None:
        print("There is unsupported symbols in request!")
        return render_template(
            'index.html',
            result="",
            history=history.get_history()
        )
    if len(re.findall(r"(?:[+*/^%-]--)|(?:\+\+\+)|(?://)|(?:\*\*)", expression)) != 0:
        print("There is unsupported combination of symbols in request!")
        return render_template(
            'index.html',
            result="",
            history=history.get_history()
        )
    try:
        result = eval(expression.replace("^", "**"))
        entity = History(expression, result, str(datetime.datetime.now()))
        history.add_history(entity)
    except ZeroDivisionError:
        print("Division by zero found!")
        return render_template('index.html', result="", history=history.get_history())

    return render_template('index.html', result=result, history=history.get_history())


@app.route('/clear', methods=['POST'])
def history_clear():
    history.clear_history()
    return redirect(url_for("index"), 301)


if __name__ == '__main__':
    history = HistoryRepository()
    app.run()

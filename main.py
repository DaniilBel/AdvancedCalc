import sys

from flask import Flask, request, render_template
import re
from database.model.calc_history import History, History_get
from database.repository.history_repository import HistoryRepository

app = Flask(__name__)
app.debug = True


class ParseError(ValueError):
    pass


def inform_user(msg: str):
    print(msg)  # add code to inform user


def is_number(str):
    try:
        float(str)
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
        inform_user("There is unsupported symbols in request!")
        return render_template(
            'index.html',
            result="",
            history=history.get_history()
        )
    if len(re.findall(r"(?:[+*/^%-]--)|(?:\+\+\+)|(?://)|(?:\*\*)", expression)) != 0:
        inform_user("There is unsupported combination of symbols in request!")
        return render_template(
            'index.html',
            result="",
            history=history.get_history()
        )
    try:
        # если будет поддержка ^ - заменить здесь на ** TODO
        result = eval(expression)
        print(expression, result)
        entity = History()
        entity.line = expression
        entity.answer = result
        history.add_history(entity)
    except ZeroDivisionError:
        inform_user("Division by zero found!")
        history.clear_history()
        return render_template('index.html', result="", history=history.get_history())

    return render_template('index.html', result=result, history=history.get_history())


    """if not is_number(expression):
        result = eval(expression)
        history.append({"expression": str(expression), "result": str(result)})
        return render_template('index.html', result=result, history=history)

    return render_template('index.html', history=history)"""


@app.route('/history', methods=['POST'])
def history_moment():
    # history.clear()

    return render_template('index.html', history=[])


if __name__ == '__main__':
    history = HistoryRepository()
    app.run()

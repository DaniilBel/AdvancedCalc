import datetime
import re

from flask import Flask, request, render_template, redirect, url_for, flash

from database.model.calc_history import History
from database.repository.history_repository import HistoryRepository

app = Flask(__name__)
app.secret_key = "KADadbjhaOW&^*FTYG*WGXjskBSJLHBasnk"


def expression_check(expression) -> (bool, str):
    if re.fullmatch(r"\A[\s()0-9+*/^%.-]*\Z", expression) is None:
        return False, "There are unsupported symbols in request!"
    if len(re.findall(r"[+*/^%-]\s*-\s*-|\+\s*\+\s*\+|/\s*/|\*\s*\*|\.\s*\.", expression)) != 0:
        return False, "There are unsupported combinations of symbols in request!"
    try:
        eval(expression.replace("^", "**"))
    except SyntaxError:
        return False, "There is syntax error in request!"
    return True,


@app.route('/')
def index():
    return render_template('index.html', history=history.get_history())


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['display'].replace("^", "**")
    result = ""
    is_valid = expression_check(expression)
    if not is_valid[0]:
        flash(is_valid[1])
    else:
        try:
            result = eval(expression)
            history.add_history(History(expression, result, str(datetime.datetime.now())))
        except ZeroDivisionError:
            flash("Division by zero found!")

    return render_template('index.html', history=history.get_history(), result=result)


@app.route('/clear', methods=['POST'])
def history_clear():
    history.clear_history()
    return redirect(url_for("index"), 301)


if __name__ == '__main__':
    history = HistoryRepository()
    app.run(host="0.0.0.0", debug=True)

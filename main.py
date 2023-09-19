import datetime
import re

from flask import Flask, request, render_template, redirect, url_for, flash

from database.model.calc_history import History
from database.repository.history_repository import HistoryRepository

app = Flask(__name__)
app.secret_key = "KADadbjhaOW&^*FTYG*WGXjskBSJLHBasnk"


def expression_check(expression) -> (bool, str):
    if re.fullmatch(r"\A[\se()0-9+*/^%.-]*\Z", expression) is None:
        return False, "There are unsupported symbols in request!"
    if len(re.findall(r"[+*/^%-]\s*-\s*-|\+\s*\+\s*\+|/\s*/|\*\s*\*|\.\s*\.|\(\)|\)\(|\d\(", expression)) != 0:
        return False, "There are unsupported combinations of symbols in request!"
    return True,


@app.route('/')
def index():
    print(history.get_history())
    return render_template('index.html', history=history.get_history())


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['display']
    result = ""
    is_valid = expression_check(expression)
    if not is_valid[0]:
        flash(is_valid[1])
    else:
        try:
            result = eval(expression.replace("^", "**").replace("%", "*0.01*"))
            result = float(result) if result >= 1e+12    else result

            history.add_history(History(expression, result, type(result) == int, str(datetime.datetime.now())))
        except ZeroDivisionError:
            flash("Division by zero found!")
        except (SyntaxError, ValueError, NameError):
            flash("Invalid expression!")

    return render_template('index.html', history=history.get_history(), result=result)


@app.route('/clear', methods=['POST'])
def history_clear():
    history.clear_history()
    return redirect(url_for("index"), 301)


if __name__ == '__main__':
    history = HistoryRepository()
    app.run(host="0.0.0.0", debug=True)

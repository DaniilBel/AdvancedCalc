import datetime
import re

from flask import Flask, request, render_template, redirect, url_for, flash

from database.model.calc_history import History
from database.repository.history_repository import HistoryRepository

app = Flask(__name__)
app.secret_key = "KADadbjhaOW&^*FTYG*WGXjskBSJLHBasnk"
MAX_DOUBLE = 1.7976931348623157E+308


def expression_check(expression) -> (bool, str):
    if re.fullmatch(r"\A[\seE()0-9+*/^%.-]*\Z", expression) is None:
        return False, "There are unsupported symbols in request!"
    if len(re.findall(r"[+*/^%-]\s*-\s*-|\+\s*\+\s*\+|/\s*/|\*\s*\*|\.\s*\.|\(\)|\)\(|\d\(", expression)) != 0:
        return False, "There are unsupported combinations of symbols in request!"
    return True,


@app.route('/')
def index():
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
            expression_str = expression.replace("^", "**").replace("%", "*0.01*")
            if eval(f"{expression_str} > {MAX_DOUBLE}"):
                raise OverflowError
            result = eval(expression_str)
            history.add_history(History(expression, result, type(result) == int, str(datetime.datetime.now())))
        except ZeroDivisionError:
            flash("Division by zero found!")
        except (SyntaxError, ValueError, NameError):
            flash("Invalid expression!")
        except OverflowError:
            flash("Number overflow occurred!")

    return render_template('index.html', history=history.get_history(), result=result)


@app.route('/clear', methods=['POST'])
def history_clear():
    history.clear_history()
    return redirect(url_for("index"), 301)


if __name__ == '__main__':
    history = HistoryRepository()
    app.run(host="0.0.0.0", debug=True)

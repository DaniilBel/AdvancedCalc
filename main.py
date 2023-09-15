import sys

from flask import Flask, request, render_template
import re
from database.model.connector import create_connection

app = Flask(__name__)
app.debug = True


class ParseError(ValueError):
    pass


def inform_user(msg: str):
    print(msg)  # add code to inform user


@app.route('/')
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM calc_history")
    return render_template('index.html', history=cursor.fetchall())


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['display']
    cursor = connection.cursor()
    # потом нормально обработать исключения с выводом сообщения в окне
    if re.fullmatch(r"\A[()0-9+*/^%.-]*\Z", expression) is None:
        inform_user("There is unsupported symbols in request!")
        return render_template(
            'index.html',
            result="",
            history=cursor.fetchall()
        )
    if len(re.findall(r"(?:[+*/^%-]--)|(?:\+\+\+)|(?://)|(?:\*\*)", expression)) != 0:
        inform_user("There is unsupported combination of symbols in request!")
        return render_template(
            'index.html',
            result="",
            history=cursor.fetchall()
        )
    try:
        # если будет поддержка ^ - заменить здесь на **
        result = eval(expression)
        sql = "INSERT INTO calc_history (line, answer) VALUES (%s, %s)"
        val = (expression, result)
        cursor.execute(sql, val)
    except ZeroDivisionError:
        inform_user("Division by zero found!")
        return render_template('index.html', result="", history=cursor.fetchall())

    cursor.execute("SELECT * FROM calc_history")
    return render_template('index.html', result=result, history=cursor.fetchall())


if __name__ == '__main__':
    connection = create_connection()
    app.run()

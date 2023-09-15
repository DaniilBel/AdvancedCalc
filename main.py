from flask import Flask, request, render_template
import re
from database.model.connector import create_connection

app = Flask(__name__)
app.debug = True


class ParseError(ValueError):
    pass


@app.route('/')
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM calc_history")
    return render_template('index.html', history=cursor.fetchall())


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['display']
    # потом нормально обработать исключения с выводом сообщения в окне
    if re.fullmatch(r"\A[()0-9+*/^%-]*\Z", expression) is None:
        raise ParseError("There is unsupported symbols in request!")
    if len(re.findall(r"(?:[+*/^%-]--)|(?:\+\+\+)|(?://)|(?:\*\*)", expression)) != 0:
        raise ParseError("There is unsupported combination of symbols in request!")
    try:
        # если будет поддержка ^ - заменить здесь на ** : result = eval(expression.replace("^", "**"))
        result = eval(expression)
        cursor = connection.cursor()
        sql = "INSERT INTO calc_history (line, answer) VALUES (%s, %s)"
        val = (expression, result)
        cursor.execute(sql, val)

    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero found!")

    cursor.execute("SELECT * FROM calc_history")
    return render_template('index.html', result=result, history=cursor.fetchall())


if __name__ == '__main__':
    connection = create_connection()
    app.run()

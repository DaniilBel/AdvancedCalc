from flask import Flask, request, render_template
import re

app = Flask(__name__)
app.debug = True

history = []


class ParseError(ValueError):
    pass


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['display']
    # потом нормально обработать исключения с выводом сообщения в окне
    if re.fullmatch(r"\A[()0-9+*/^%-]*\Z", expression) is None:
        raise ParseError("There is unsupported symbols in request!")
    if len(re.findall(r"(?:[+*/^%-]--)|(?:\+\+\+)|(?://)|(?:\*\*)", expression)) != 0:
        raise ParseError("There is unsupported combination of symbols in request!")
    try:
        # если будет поддержка ^ - заменить здесь на **
        result = eval(expression)
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero found!")

    history.append({"expression": str(expression), "result": str(result)})

    return render_template('index.html', result=result, history=history)


if __name__ == '__main__':
    app.run()

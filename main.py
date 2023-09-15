from flask import Flask, request, render_template
import re

app = Flask(__name__)
app.debug = True

history = []


class ParseError(ValueError):
    pass


def inform_user(msg: str):
    app.logger.info("Calculation problem: %s", msg)
    print(msg)  # add code to inform user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['display']
    # потом нормально обработать исключения с выводом сообщения в окне
    if re.fullmatch(r"\A[()0-9+*/^%-]*\Z", expression) is None:
        inform_user("There is unsupported symbols in request!")
        return render_template(
            'index.html',
            result="",
            history=history
        )
    if len(re.findall(r"(?:[+*/^%-]--)|(?:\+\+\+)|(?://)|(?:\*\*)", expression)) != 0:
        inform_user("There is unsupported combination of symbols in request!")
        return render_template(
            'index.html',
            result="",
            history=history
        )
    try:
        # если будет поддержка ^ - заменить здесь на **
        result = eval(expression)
    except ZeroDivisionError:
        inform_user("Division by zero found!")
        return render_template('index.html', result="", history=history)
    history.append({"expression": str(expression), "result": str(result)})

    return render_template('index.html', result=result, history=history)


if __name__ == '__main__':
    app.run()

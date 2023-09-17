from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

history = []


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['display']

    if not is_number(expression):
        result = eval(expression)
        history.append({"expression": str(expression), "result": str(result)})
        return render_template('index.html', result=result, history=history)

    return render_template('index.html', history=history)


@app.route('/history', methods=['POST'])
def history_moment():
    history.clear()

    return render_template('index.html', history=history)


if __name__ == '__main__':
    app.run()


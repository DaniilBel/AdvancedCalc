from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

history = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['display']

    result = eval(expression)

    history.append({"expression": str(expression), "result": str(result)})

    return render_template('index.html', result=result, history=history)


@app.route('/history', methods=['POST'])
def historyMoment():
    history.clear()

    return render_template('index.html', history=history)


if __name__ == '__main__':
    app.run()


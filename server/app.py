from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)  # Print to console
    return parameter  # Display in browser


@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = ''
    for i in range(parameter):
        numbers += f"{i}\n"
        print(i)
    return numbers


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':  # ✅ Handle modulo (remainder)
        result = num1 % num2
    else:
        result = 'Invalid operation'

    print(result)  # ✅ Output to console for testing
    return str(result)  # ✅ Display result in browser

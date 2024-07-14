from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    binary_result = ''
    hex_result = ''
    error_message = ''
    if request.method == 'POST':
        number = request.form['number']
        if number.isdigit():
            if number.startswith('0') and len(number) > 1:
                error_message = 'Invalid input: Numbers should not begin with Zero.'
            else:
                number = int(number)
                binary_result = bin(number)[2:] 
                hex_result = hex(number)[2:].upper()  
        else:
            error_message = 'Invalid input: Please enter a valid number.'
    return render_template('index.html', binary_result=binary_result, hex_result=hex_result, error_message=error_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

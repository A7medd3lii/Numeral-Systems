from flask import Flask, render_template, request

app = Flask(__name__)

def convert_number(input_number, from_base, to_base):
    try:
        decimal_number = int(input_number, from_base)
    except ValueError:
        return None, None, None, "Invalid number for the selected base."
    
    if to_base == 2:
        return bin(decimal_number)[2:], "Binary", None, None
    elif to_base == 8:
        return oct(decimal_number)[2:], "Octal", None, None
    elif to_base == 16:
        return hex(decimal_number)[2:], "Hexadecimal", None, None
    else:
        return str(decimal_number), "Decimal", None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    result, result_type, error_message = None, None, None
    
    if request.method == 'POST':
        input_number = request.form['number']
        from_base = int(request.form['from_base'])
        to_base = int(request.form['to_base'])
        result, result_type, _, error_message = convert_number(input_number, from_base, to_base)
    
    return render_template('index.html', result=result, result_type=result_type, error_message=error_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

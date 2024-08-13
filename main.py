from flask import Flask, render_template, request

app = Flask(__name__)

def convert_number(number, from_base, to_base):
    try:
        # Convert the number from the source base to decimal
        decimal_number = int(number, from_base)
        # Convert the decimal number to the target base
        if to_base == 10:
            return str(decimal_number)
        elif to_base == 16:
            return hex(decimal_number)[2:].upper()
        elif to_base == 2:
            return bin(decimal_number)[2:]
        elif to_base == 8:
            return oct(decimal_number)[2:]
    except ValueError:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    result_type = None
    error_message = None

    if request.method == 'POST':
        number = request.form.get('number')
        from_base = int(request.form.get('from_base'))
        to_base = int(request.form.get('to_base'))

        # Validate input
        if not number:
            error_message = "Number is required."
        elif from_base not in [2, 8, 10, 16] or to_base not in [2, 8, 10, 16]:
            error_message = "Invalid base provided."
        elif from_base == to_base:
            result = number
            result_type = "Result"
        else:
            result = convert_number(number, from_base, to_base)
            if result is None:
                error_message = "Invalid number or base conversion error."
            else:
                result_type = "Converted Number"

    return render_template('index.html', result=result, result_type=result_type, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from convert import convert_number  # Import from the new module

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result, result_type, error_message = None, None, None
    
    if request.method == 'POST':
        input_number = request.form.get('number', '')
        from_base = int(request.form.get('from_base', 10))  # Default to base 10
        to_base = int(request.form.get('to_base', 10))  # Default to base 10
        result, result_type, error_message, _ = convert_number(input_number, from_base, to_base)
    
    return render_template('index.html', result=result, result_type=result_type, error_message=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

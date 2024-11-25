from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length, include_uppercase, include_digits, include_special):
    chars = string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_special:
        chars += string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    length = data.get('length', 12)
    include_uppercase = data.get('include_uppercase', True)
    include_digits = data.get('include_digits', True)
    include_special = data.get('include_special', True)
    
    password = generate_password(length, include_uppercase, include_digits, include_special)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
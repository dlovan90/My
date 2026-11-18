import os
from flask import Flask, render_template, request, session, jsonify

app = Flask(__name__)
app.secret_key = "my_super_secret_key_123"
ADMIN_PASSWORD = "MySecret123!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    if data.get('password') == ADMIN_PASSWORD:
        session['is_admin'] = True
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 401

@app.route('/api/check_auth')
def check_auth():
    return jsonify({"is_admin": session.get('is_admin', False)})

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('is_admin', None)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    'gayu': '12@gd',
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if users.get(username) == password:
            return redirect(url_for('dashboard', username=username))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    username = request.args.get('username')

    if username:
        return f'Welcome, {username}!'
    else:
        return 'Unauthorized. Please log in first.'

if __name__ == '__main__':
    app.run(debug=True)

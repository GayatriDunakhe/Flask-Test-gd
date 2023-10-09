from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/input', methods=['GET','POST'])
def input():

    if request.method == 'POST':

        username = request.form['username']
        greet = f"Hello, {username}! Welcome to the flask world!"

        return render_template('greet.html', greet=greet)
        
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)

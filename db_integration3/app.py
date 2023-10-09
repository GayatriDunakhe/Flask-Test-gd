from flask import Flask, render_template
import sqlite3data

app = Flask(__name__)

@app.route('/')
def hello():
    create_table()
    data = show_data()

@app.route('/items')
def display():
    return render_template('show.html', data=data)


def create_table():
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items(
                   id INTEGER,
                   name TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route('/insert', methods=['POST'])
def insert():
    id = request.form['id']
    name = request.form['username']
    return "Data Added!"

if __name__ == '__main__':
    app.run(debug=True)
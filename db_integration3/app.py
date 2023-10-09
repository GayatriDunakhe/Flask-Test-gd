from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello():
    create_table()
    return "Table created!"

@app.route('/items')
def display():
    data = show_data()
    return render_template('show.html', data=data)

def create_table():
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)
    conn.commit()
    conn.close()

@app.route('/insert', methods=['GET','POST'])
def insert():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        insert_data(id, name)
        # return render_template('show.html')
    return render_template('add.html')

def insert_data(id, name):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO items (id, name) VALUES (?,?)", (id, name,))
    conn.commit()
    conn.close()

def show_data():
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items")

    data = cursor.fetchall()

    conn.close()
    return data  

if __name__ == '__main__':
    app.run(debug=True)

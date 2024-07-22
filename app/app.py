from flask import Flask, request, redirect, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='postgres', dbname='mydb', user='user', password='password')
    return conn

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name) VALUES (%s)', (name,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', users=users)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

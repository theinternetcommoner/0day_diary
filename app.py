import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from waitress import serve

app = Flask(__name__)
app.secret_key = os.urandom(24) # For secure flash messages
# DB_NAME = "diary.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "data")
DB_NAME = os.path.join(DB_DIR, "diary.db")

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

def init_db():
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                content TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get('content', '').strip()
        
        if not content:
            flash("An empty day is still a day, but a diary needs words.", "warning")
        else:
            # Format date as YYYY-MM-DD
            today_str = datetime.now().strftime('%Y-%m-%d')
            
            with get_db_connection() as conn:
                conn.execute(
                    'INSERT INTO entries (date, content) VALUES (?, ?)',
                    (today_str, content)
                )
                conn.commit()
            flash("Thought captured.", "success")
            return redirect(url_for('index'))

    # Fetch all entries, newest first
    with get_db_connection() as conn:
        entries = conn.execute('SELECT date, content FROM entries ORDER BY id DESC').fetchall()
    
    # Format dates beautifully for the template
    formatted_entries = []
    for entry in entries:
        dt = datetime.strptime(entry['date'], '%Y-%m-%d')
        formatted_entries.append({
            'date_display': dt.strftime('%B %d, %Y'),
            'content': entry['content']
        })

    return render_template('index.html', entries=formatted_entries)

if __name__ == '__main__':
    init_db()
    # app.run(debug=True)

    HOST = "0.0.0.0"
    PORT = 4500
    print(f"App running at {HOST}:{PORT}")
    serve(app, host=HOST, port=PORT, threads=6)
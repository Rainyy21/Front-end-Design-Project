from flask import Flask , render_template
import sqlite3

app = Flask(__name__)

def get_db_connect():
    conn = sqlite3.connection("./db/my_library.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = sqlite3.connection("./db/my_library.db")
    query = """
    SELECT m.title, m.type, m.release_year, m.rating,
            b.author, s.network
    FROM media m
    LEFT JOIN books b on m.id = b.books_id
    LEFT JOIN shows s on m.id = s.shows_id
    """
    items = conn.execute(query).fetchall()
    conn.close()

if __name__ == '__main__':
    app.run(debug = True)

    

import sqlite3

def init_db():
    conn = sqlite3.connect('my_library.db')
    cursor = conn.cursor()

    cursor.executescript('''
        CREATE A TABLE IF NOT EXISTS media(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            type TEXT CHECK(type IN ('Book', 'Show')),
            release_year INTEGER
            );
        
        CREATE A TABLE IF NOT EXISTS books(
            book_id INTEGER PRIMARY KEY,
            author TEXT,
            page INTEGER,
            FOREIGN KEY (book_id) REFERENCES media (id)
        );

        CREATE A TABLE IF NOT EXISTS shows(
            show_id INTEGER PRIMARY KEY,
            network TEXT,
            episodes INTEGER,
            FOREIGN KEY (show_id) REFERENCES media (id)
        );
                         ''')
    conn.commit()
    conn.close()

def add_book(title , year, author, page):
    conn = sqlite3.connect('my_library.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO media (title, type, release_year) VALUES (?, 'Book', ?)", (title, year))
    last_id = cursor.lastrowid
    cursor.execute("INSERT INTO books (book_id, author, pages) VALUES (?, ?, ?)", (last_id, author, pages))

    conn.commit()
    conn.close()
    print(f"Added {title} successfully!")

def add_shows(title , year, network, episodes):
    conn = sqlite3.connect('my_library')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO media(title, type, release_year) VALUES (?, 'Show',?)" , (title, year))
    last_id = cursor.lastrowid
    cursor.execute("INSERT INTO shows(show_id , network , episodes) VALUES (?,?,?)" , (last_id,network,episodes))
    conn.commit()
    conn.close()
    print(f"Added {title} successfully!")

#fetch 
def get_all_media():
    conn = sqlite3.connect('my_library.db')
    # This line makes results behave like dictionaries (e.g., row['title'])
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()

    query = """
    SELECT m.title, m.type, b.author, s.network
    FROM media m
    LEFT JOIN books b ON m.id = b.book_id
    LEFT JOIN shows s ON m.id = s.show_id
    """
    
    rows = cursor.execute(query).fetchall()
    conn.close()
    return rows

# Print the results
for item in get_all_media():
    print(f"{item['title']} ({item['type']})")


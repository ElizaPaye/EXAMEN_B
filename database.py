import sqlite3

def conectar():
    return sqlite3.connect("citas.db")

def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mascota TEXT NOT NULL,
        propietario TEXT NOT NULL,
        especie TEXT,
        fecha TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

crear_tabla()
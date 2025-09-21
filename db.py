import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "neurolearn.db"

def get_conn():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(        """        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        """    )
    cur.execute(        """        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
        );
        """    )
    conn.commit()
    conn.close()

def create_user(name, email, password_hash):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email, password_hash, created_at) VALUES (?, ?, ?, ?)",                (name, email, password_hash, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, password_hash FROM users WHERE email = ?", (email,))
    row = cur.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "name": row[1], "email": row[2], "password_hash": row[3]}
    return None

def save_quiz_result(user_id, score, total):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO quiz_results (user_id, score, total, created_at) VALUES (?, ?, ?, ?)",                (user_id, score, total, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def get_quiz_history(user_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT score, total, created_at FROM quiz_results WHERE user_id = ? ORDER BY created_at ASC",                (user_id,))
    rows = cur.fetchall()
    conn.close()
    return rows

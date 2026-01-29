import psycopg2
import hashlib
import pycountry

# utils.py

def country_to_iso3(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None
    
    
def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="imports",
        user="postgres",
        password="gassa"
    )


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_user(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT password_hash FROM users WHERE username=%s", (username,))
    row = cur.fetchone()
    conn.close()

    if row:
        return row[0] == hash_password(password)
    return False

from psycopg2.errors import UniqueViolation

def register_user(username, email, password):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, hash_password(password))
        )
        conn.commit()

    except UniqueViolation:
        conn.rollback()
        raise Exception("Benutzername oder E-Mail existiert bereits.")

    finally:
        conn.close()
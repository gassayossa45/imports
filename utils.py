# utils.py
# ---------------------------------------------------------
# Zentrale Hilfsfunktionen für:
# - Datenbankverbindung
# - Passwort-Hashing
# - User-Login / Registrierung
# - Sprachübersetzung (t())
# ---------------------------------------------------------

import psycopg2
import hashlib
import pycountry
from psycopg2.errors import UniqueViolation
import os
from supabase import create_client
import streamlit as st
from translations import translations




# ---------------------------------------------------------
# Sprachsystem: Übersetzungsfunktion
# ---------------------------------------------------------
# Die Datei translations.py enthält ein Dictionary:
# translations = {
#     "login_title": {"de": "Login", "en": "Login"},
#     "welcome_msg": {"de": "Willkommen", "en": "Welcome"},
#     ...
# }
#
# Die Funktion t(key) liefert automatisch die richtige Sprache
# basierend auf st.session_state["lang"].
# ---------------------------------------------------------

def t(key):
    """
    Gibt den übersetzten Text für den angegebenen Key zurück.
    Fällt zurück auf Deutsch, falls Sprache oder Key fehlt.
    """

    lang = st.session_state.get("lang", "de")

    # Falls Key fehlt → deutschen Text zurückgeben
    if key not in translations:
        return f"[{key}]"

    return translations[key].get(lang, translations[key]["de"])


# ---------------------------------------------------------
# Länder-Konvertierung (Name → ISO3)
# ---------------------------------------------------------
def country_to_iso3(name):
    """
    Konvertiert einen Ländernamen in den ISO3-Code.
    Beispiel: 'Germany' → 'DEU'
    """
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None


# ---------------------------------------------------------
# Datenbankverbindung
# ---------------------------------------------------------
def get_connection():
    """
    Stellt eine Verbindung zur PostgreSQL-Datenbank her.
    """
    return psycopg2.connect(
        host="db.xxdveopyipxzclzmhfde.supabase.co",
        database="postgres",
        user="postgres",
        password="Gael2012!&237",
        port=5432,
        sslmode="require"
    )


# ---------------------------------------------------------
# Passwort-Hashing
# ---------------------------------------------------------
def hash_password(password):
    """
    Erstellt einen SHA256-Hash eines Passworts.
    """
    return hashlib.sha256(password.encode()).hexdigest()


# ---------------------------------------------------------
# Benutzerprüfung (Login)
# ---------------------------------------------------------
def check_user(username, password):
    """
    Prüft, ob Benutzername + Passwort korrekt sind.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT password_hash FROM users WHERE username=%s", (username,))
    row = cur.fetchone()
    conn.close()

    if row:
        return row[0] == hash_password(password)
    return False


# ---------------------------------------------------------
# Benutzerregistrierung
# ---------------------------------------------------------
def register_user(username, email, password):
    """
    Registriert einen neuen Benutzer.
    Wirft eine Exception, wenn Username oder E-Mail bereits existieren.
    """
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
        # Diese Exception wird im UI abgefangen und übersetzt
        raise Exception("user_exists")

    finally:
        conn.close()
import sqlite3




def create_connection(dbpath):
    return sqlite3.connect(dbpath)


connection = sqlite3.connect("chinook.db")


def create_artist(conn, artist_name):
    cur = conn.cursor()
    cur.excetute('INSERT INTO artists (Name) VALUES (?)', artist_name)


create_artist(conn, "?")


def read_artists(conn):
    cur = conn.cursor()
    cur.excetute('SELECT * FROM artists ORDER BY name ASC')
    return cur.fetchall()


print(read_artists())



import sqlite3


def create_connection(dbpath):
    return sqlite3.connect(dbpath)


connection = sqlite3.connect("chinook.db")


def create_artist(id, artist_name):
    cur = connection.cursor()
    cur.excetute('INSERT INTO artists (Name) VALUES (?)', artist_name)


create_artist(2, "Justin Bieber")


def read_artists(conn):
    cur = conn.cursor()
    cur.excetute('SELECT * FROM artists ORDER BY name ASC')
    return cur.fetchall()


print(read_artists())


def update_artist(id, new_name):
    cur = connection.cursor()
    cur.excetute('UPDATE artists SET Name = ? WHERE ArtistId = ?', (id, new_name))


update_artist(3, "Justin Bieber")


def delete_artist(id=None, name=""):
    cur = connection.cursor()
    cur.execute('DELETE FROM artists WHERE ArtistId = ? OR Name = ?', (id, name))


delete_artist(3, "Justin Bieber")


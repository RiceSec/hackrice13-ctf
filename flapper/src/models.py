import sqlite3 as sql

def retrieveUsers():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()
    con.close()
    return users

def loginUser(username, password) -> bool:
    con = sql.connect("database.db")
    cur = con.cursor()
    query = f"SELECT password FROM users WHERE username = '{username}' AND password = '{password}'"
    print(query)
    cur.execute(query)
    users = cur.fetchall()
    con.close()

    if len(users) > 0:
        return True
    else:
        return False
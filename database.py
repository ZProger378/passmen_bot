import json
import sqlite3
from hash import *


def reset_database(user_id, master_password, salt_1, salt_2):
    user = hash_data(str(user_id))
    os.system(f"mkdir Databases/{user}/")
    json_data = {
        'master_password': hash_data(master_password, salt=[salt_1, salt_2]),
        'salt_1': salt_1,
        'salt_2': salt_2
    }
    with open(f"Databases/{user}/config.json", "w") as f:
        f.write(json.dumps(json_data))
    con = sqlite3.connect(f"Databases/{user}/passwords.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE Passwords ("
                "id INTEGER, user TEXT, "
                "url TEXT, login TEXT, password TEXT, comment TEXT"
                ")")
    encrypt(f"Databases/{user}/passwords.db", master_password)
    encrypt(f"Databases/{user}/config.json", master_password)


def get_passwords(user_id):
    user = hash_data(str(user_id))
    con = sqlite3.connect(f"Databases/{user}/passwords.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Passwords")
    unsorted = cur.fetchall()
    passwords = []
    for i in unsorted:
        passwords.append({
            'id': i[0],
            'user': i[1],
            'url': i[2],
            'login': i[3],
            'password': i[4],
            'comment': i[5]
        })

    return passwords


def add_password(user_id, url, login, password, comment):
    user = hash_data(str(user_id))
    pwd_id = randint(1000, 9999)
    con = sqlite3.connect(f"Databases/{user}/passwords.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Passwords (id, user, url, login, password, comment) "
                "VALUES (?, ?, ?, ?, ?, ?)", (pwd_id, user, url, login, password, comment))
    con.commit()


def delete_password(user_id, pwd_id):
    user = hash_data(str(user_id))
    con = sqlite3.connect(f"Databases/{user}/passwords.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Passwords WHERE id = ?", (pwd_id,))
    con.commit()


def get_password(pwd_id, user_id):
    user = hash_data(str(user_id))
    con = sqlite3.connect(f"Databases/{user}/passwords.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Passwords WHERE id = ?", (pwd_id,))
    unsorted = cur.fetchone()
    pwd_info = {
        'id': unsorted[0],
        'user': unsorted[1],
        'url': unsorted[2],
        'login': unsorted[3],
        'password': unsorted[4],
        'comment': unsorted[5]
    }

    return pwd_info


def get_salt(user_id):
    user = hash_data(str(user_id))
    with open(f"Databases/{user}/config.json", "r") as f:
        config = json.load(f)
        salt_1, salt_2 = config['salt_1'], config['salt_2']

    return salt_1, salt_2


def get_master_password_hash(user_id):
    user = hash_data(str(user_id))
    with open(f"Databases/{user}/config.json", "r") as f:
        config = json.load(f)
        master_password_hash = config['master_password']

    return master_password_hash

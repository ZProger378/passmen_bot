import hashlib
import os
from random import randint, choice
import cryptocode
import pyAesCrypt


def hash_data(data, salt=None):
    if salt is not None:
        data = f"{salt[0]}{data}{salt[1]}"
    hash_object = hashlib.sha512(data.encode("utf-8"))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def encrypt_data(data, password):
    return cryptocode.encrypt(data, password)


def decrypt_data(data, password):
    return cryptocode.decrypt(data, password)


def gen_salt():
    chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+-=[]{};:'\",.<>/?|\\/*`~"
    salt_len1, salt_len2 = randint(10, 30), randint(10, 30)
    salt_1 = ""
    salt_2 = ""
    for i in range(salt_len1):
        salt_1 += choice(chars)
    for i in range(salt_len2):
        salt_2 += choice(chars)

    return salt_1, salt_2


def gen_strong_password():
    chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
    pass_len = randint(10, 20)
    password = ""
    for i in range(pass_len):
        password += choice(chars)

    return password


def encrypt(file, password):
    pyAesCrypt.encryptFile(f"{file}", f"{file}.crypt", password, 64 * 1024)
    os.system(f"shred -u -z {file}")


def decrypt(file, password):
    pyAesCrypt.decryptFile(f"{file}", f"{file.split('.crypt')[0]}", password, 64 * 1024)
    os.system(f"shred -u -z {file}")

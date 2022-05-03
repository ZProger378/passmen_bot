from random import *

chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
pass_len = 10
password = ""
for i in range(pass_len):
    password += choice(chars)

print(password)

from config import *
from markup import *
from database import *


def configure_database_1(message):
    password = message.text
    if password != "Сгенерировать надёжный пароль 🔐":
        bot.send_message(message.chat.id, f"Отлично, а теперь повторите мастер-пароль...")
        bot.register_next_step_handler(message, configure_database_2, password)
    else:
        password = gen_strong_password()
        salt_1, salt_2 = gen_salt()
        reset_database(message.chat.id, password, salt_1, salt_2)
        bot.send_message(message.chat.id, f"Ваша личная база данных создана!", reply_markup=new_session_markup())
        bot.send_message(message.chat.id, f"<b>Ваш автоматически-сгенерированный мастер-пароль:</b> <code>{password}</code>")


def configure_database_2(message, password):
    repeated_password = message.text
    if repeated_password == password:
        salt_1, salt_2 = gen_salt()
        reset_database(message.chat.id, password, salt_1, salt_2)
        bot.send_message(message.chat.id, f"Ваша личная база данных создана!", reply_markup=new_session_markup())
    else:
        bot.send_message(message.chat.id, f"Пароли не совпадают!")
        bot.send_message(message.chat.id, f"Придумайте мастер-пароль...")
        bot.register_next_step_handler(message, configure_database_1)


def new_session_handler_1(message):
    password = message.text
    user = hash_data(str(message.chat.id))
    try:
        decrypt(f"Databases/{user}/config.json.crypt", password)
        decrypt(f"Databases/{user}/passwords.db.crypt", password)
    except:
        bot.send_message(message.chat.id, f"Пароль неверный ❌")
    else:
        bot.send_message(message.chat.id, f"‼️ ВНИМАНИЕ ‼️\n\n"
                                          f"На время сессии ваша база данных расшифровывается, "
                                          f"поэтому постарайтесь по-скорее закрыть сессию!!!")
        bot.send_message(message.chat.id, f"Сессия открыта!", reply_markup=main_markup())


def close_session_handler(message):
    password = message.text
    user = hash_data(str(message.chat.id))
    salt_1, salt_2 = get_salt(message.chat.id)
    pass_hash = hash_data(password, salt=[salt_1, salt_2])
    master_password = get_master_password_hash(message.chat.id)
    if pass_hash == master_password:
        encrypt(f"Databases/{user}/config.json", password=password)
        encrypt(f"Databases/{user}/passwords.db", password=password)
        bot.send_message(message.chat.id, f"Сессия закрыта. База данных данных зашифрована!",
                         reply_markup=new_session_markup())
    else:
        bot.send_message(message.chat.id, f"Мастер-пароль неверный ❌")


def addpassword_handler_1(message):
    url = message.text
    if url != "Отменить 🔘":
        bot.send_message(message.chat.id, f"Введите логин...")
        bot.register_next_step_handler(message, addpassword_handler_2, url)
    else:
        passwords = get_passwords(message.chat.id)
        bot.send_message(message.chat.id, f"Все ваши записи:",
                         reply_markup=passwords_markup(passwords))


def addpassword_handler_2(message, url):
    login = message.text
    if login != "Отменить 🔘":
        bot.send_message(message.chat.id, f"Введите пароль...", reply_markup=gen_strong_password_markup())
        bot.register_next_step_handler(message, addpassword_handler_3, url, login)
    else:
        passwords = get_passwords(message.chat.id)
        bot.send_message(message.chat.id, f"Все ваши записи:",
                         reply_markup=passwords_markup(passwords))


def addpassword_handler_3(message, url, login):
    password = message.text
    if password != "Отменить 🔘":
        if password != "Сгенерировать надёжный пароль 🔐":
            bot.send_message(message.chat.id, f"Введите комментарий к записи...", reply_markup=set_empty_comment())
            bot.register_next_step_handler(message, addpassword_handler_4, url, login, password)
        else:
            password = gen_strong_password()
            bot.send_message(message.chat.id, f"<b>Ваш автоматически-сгенерированный пароль:</b> <code>{password}</code>")
            bot.send_message(message.chat.id, f"Введите комментарий к записи...", reply_markup=set_empty_comment())
            bot.register_next_step_handler(message, addpassword_handler_4, url, login, password)
    else:
        passwords = get_passwords(message.chat.id)
        bot.send_message(message.chat.id, f"Все ваши записи:",
                         reply_markup=passwords_markup(passwords))


def addpassword_handler_4(message, url, login, password):
    comment = message.text
    if comment != "Отменить 🔘":
        if comment == "Оставить комментарий пустым 🔘":
            comment = ""
        master_password = get_master_password_hash(message.chat.id)
        add_password(message.chat.id, url, encrypt_data(login, password),
                     encrypt_data(password, master_password), comment)
        passwords = get_passwords(message.chat.id)
        bot.send_message(message.chat.id, f"Запись успешно добавлена ✅",
                         reply_markup=main_markup())
        bot.send_message(message.chat.id, f"Все ваши записи:",
                         reply_markup=passwords_markup(passwords))
    else:
        passwords = get_passwords(message.chat.id)
        bot.send_message(message.chat.id, f"Все ваши записи:",
                         reply_markup=passwords_markup(passwords))

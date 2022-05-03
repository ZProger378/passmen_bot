from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def new_session_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton("Открыть новую сессию ➕")
    btn2 = KeyboardButton("Сгенерировать надёжный пароль 🔐")
    markup.add(btn1, btn2)

    return markup


def main_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton("Просмотреть пароли 🔒")
    btn2 = KeyboardButton("Сгенерировать надёжный пароль 🔐")
    btn3 = KeyboardButton("Закрыть сессию ❌")
    markup.add(btn1, btn2, btn3)

    return markup


def passwords_markup(passwords):
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton("Добавить запись ➕", callback_data=f"addpassword")
    markup.add(btn1)
    if passwords:
        for pwd in passwords:
            btn = InlineKeyboardButton(f"🔒 {pwd['url']}", callback_data=f"pwd_{pwd['id']}")
            markup.add(btn)
    else:
        btn = InlineKeyboardButton("Пусто", callback_data="empty")
        markup.add(btn)

    return markup


def cancel_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Отменить 🔘")
    markup.add(btn)

    return markup


def set_empty_comment():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton("Оставить комментарий пустым 🔘")
    btn2 = KeyboardButton("Отменить 🔘")
    markup.add(btn1, btn2)

    return markup


def password_markup(pwd_id):
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton("Удалить запись 🗑", callback_data=f"remove_{pwd_id}")
    back = InlineKeyboardButton("Назад ↩️", callback_data="back_to_passwords")
    markup.add(btn1, back)

    return markup


def to_passwords():
    markup = InlineKeyboardMarkup()
    back = InlineKeyboardButton("Назад ↩️", callback_data="back_to_passwords")
    markup.add(back)

    return markup


def strong_password_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("Сгенерировать надёжный пароль 🔐")
    markup.add(btn1)

    return markup


def gen_strong_password_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton("Сгенерировать надёжный пароль 🔐")
    btn2 = KeyboardButton("Отменить 🔘")
    markup.add(btn1, btn2)

    return markup

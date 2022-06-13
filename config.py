from telebot import TeleBot
from env import env

bot_token = env.telegram_token
bot = TeleBot(bot_token, parse_mode="html")

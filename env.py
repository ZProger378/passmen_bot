import os
from dotenv import load_dotenv

class Environment:
    def __init__(self):
        self.telegram_token = os.getenv('TELEGRAM_TOKEN')

load_dotenv()
env = Environment()
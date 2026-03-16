# logger.py - модуль для логирования
from datetime import datetime
from colorama import init, Fore

init()

class Logger:
    def __init__(self, app_name):
        self.app_name = app_name
    
    def info(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.GREEN}[INFO]{Fore.RESET} {timestamp} - {message}")
    
    def warning(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.YELLOW}[WARNING]{Fore.RESET} {timestamp} - {message}")
    
    def error(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.RED}[ERROR]{Fore.RESET} {timestamp} - {message}")

# main.py - главный файл приложения
from utils import greet, farewell
from config import APP_NAME, DEBUG, VERSION, AUTHORS
from calculator import add, subtract, multiply, divide
from logger import Logger
from colorama import init, Fore, Style

init()
logger = Logger(APP_NAME)

def main():
    logger.info(f"Запуск {APP_NAME} v{VERSION}")
    logger.info(f"Авторы: {', '.join(AUTHORS)}")
    
    print(f"\n{Fore.CYAN}{greet('мир')}{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}--- Калькулятор ---{Style.RESET_ALL}")
    print(f"5 + 3 = {Fore.GREEN}{add(5, 3)}{Style.RESET_ALL}")
    print(f"10 - 4 = {Fore.GREEN}{subtract(10, 4)}{Style.RESET_ALL}")
    print(f"6 * 7 = {Fore.GREEN}{multiply(6, 7)}{Style.RESET_ALL}")
    print(f"15 / 3 = {Fore.GREEN}{divide(15, 3)}{Style.RESET_ALL}")
    
    logger.warning("Это пример предупреждения")
    logger.error("Это пример ошибки")
    
    print(f"\n{Fore.MAGENTA}{farewell('мир')}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()

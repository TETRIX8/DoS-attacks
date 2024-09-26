import time
from colorama import Fore, Style

# Функция для анимации текста
def animated_print(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Логотип
logo = rf"""{Fore.MAGENTA}
████████╗███████╗████████╗██████╗░██╗██╗░░██╗
╚══██╔══╝██╔════╝╚══██╔══╝██╔══██╗██║╚██╗██╔╝
░░░██║░░░█████╗░░░░░██║░░░██████╔╝██║░╚███╔╝░
░░░██║░░░██╔══╝░░░░░██║░░░██╔══██╗██║░██╔██╗░
░░░██║░░░███████╗░░░██║░░░██║░░██║██║██╔╝╚██╗
░░░╚═╝░░░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░   Created by TETRIX8
git hub : https://github.com/TETRIX8/DoS-attacks.git
{Fore.RESET}"""

# Вывод логотипа с анимацией
animated_print(logo)

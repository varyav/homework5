import colorama
print("Атрибути та методи модуля colorama:")
print(dir(colorama))
help(colorama)
from colorama import init, Fore, Back, Style
init()
print(Fore.RED + "Це червоний текст")
print(Back.YELLOW + "Це текст з жовтим фоном")
print(Style.BRIGHT + "Це яскравий текст")
print(Fore.GREEN + Back.BLACK + "Зелений текст на чорному фоні")
print(Style.RESET_ALL + "Це стандартний текст")
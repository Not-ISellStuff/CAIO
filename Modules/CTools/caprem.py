import re, os, time, json
from tkinter import filedialog
from colorama import Fore

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW

# ----------------------------------------- #

class CapRem:
    def __init__(self, file):
        self.file = file
    

    def clear(self):
        with open('Modules/Util/output.txt', 'w') as f:
            pass

    def cls(self):
        os.system('cls')

    def lines(self):
        f = open(self.file, 'r', encoding='utf-8').readlines()
        return len(f)

    def start(self):
        with open(self.file, 'r', encoding='utf-8') as file:
            content = file.read()

        pattern = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|[a-zA-Z0-9._-]+):([^\s|]+)'
        c = re.findall(pattern, content)

        for e, p in c:
            with open('Modules/Util/output.txt', 'a', encoding='utf-8') as f:
                f.write(f"{e}:{p}\n")

        os.startfile('Modules\\Util\\output.txt')

# ----------------------------------------- #

def caprem():
    rem = CapRem("")
    rem.clear()
    rem.cls()

    try:
        os.startfile("Modules\\Util\\filedialog.pyw")
        input(cyan + "Press Enter When You Have Selected A File > ")
            
        with open('Modules/Util/file.json', 'r') as f:
            data = json.load(f)
            
        rem.file = data['path']
        rem.start()
        rem.cls()
        print(green + f"[+] Removed Capture From {rem.lines()}")
        input(cyan + "Press Enter To Continue > ")

    except:
        rem.cls()
        print(red + "[!] Error")
        time.sleep(1.5)
        caprem()

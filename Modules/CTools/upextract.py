import re, os, time, json
from tkinter import filedialog
from colorama import Fore

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW

# ----------------------------------------- #

class CapRem:
    def __init__(self, file, list: list, extracted: int):
        self.file = file
        self.list = list
        self.extracted = extracted
    
    def clear(self):
        with open('Modules/Util/output.txt', 'w') as f:
            pass

    def cls(self):
        os.system('cls')

    def load_list(self):
        f = open(str(self.file), 'r', encoding='utf-8').readlines()
        self.list = f

    def ulp(self):
        for i in self.list:
            try:
                ln = str(i).strip().split(':')
                u = ln[0]
                p = ln[3]

                with open('Modules/Util/output.txt', 'a') as f:
                    f.write(f"{u}:{p}\n")
                self.extracted += 1

            except:
                print("[!] Line is not in User:Login:Password Format.")

    def lup(self):
        for i in self.list:
            try:
                ln = str(i).strip().split(':')
                u = ln[2]
                p = ln[3]

                with open('Modules/Util/output.txt', 'a') as f:
                    f.write(f"{u}:{p}\n")
                self.extracted += 1

            except Exception as e:
                print("[!] Line is not in Login:User:Password Format.")

    def uep(self):
        for i in self.list:
            try:
                ln = str(i).strip().split(':')
                u = ln[0]
                p = ln[2]

                with open('Modules/Util/output.txt', 'a') as f:
                    f.write(f"{u}:{p}\n")
                self.extracted += 1

            except:
                print("[!] Line is not in Using:Email:Password Format.")

    def eup(self):
        for i in self.list:
            try:
                ln = str(i).strip().split(':')
                u = ln[1]
                p = ln[2]

                with open('Modules/Util/output.txt', 'a') as f:
                    f.write(f"{u}:{p}\n")
                self.extracted += 1

            except:
                print("[!] Line is not in Email:User:Password Format.")

    # ----------------------------------------- #

    def start(self, op):
        if op == '1':
            self.ulp()
        elif self == '2':
            self.lup()
        elif op == '3':
            self.uep()
        elif op == '4':
            self.eup()

        os.startfile('Modules\\Util\\output.txt')

# ----------------------------------------- #

def upextract():
    up = CapRem("" ,[] ,0)
    up.clear()
    up.cls()

    try:
        os.startfile("Modules\\Util\\filedialog.pyw")
        input(cyan + "Press Enter When You Have Selected A File > ")
        with open('Modules/Util/file.json', 'r') as f:
            data = json.load(f)
        up.file = data['path']
        up.load_list()

        up.cls()
        op = input("What format is your file in?\n\n[1] User:Login:Password\n[2] Login:User:Password\n[3] User:Email:Password\n[4] Email:User:Password\n[x] exit\n\n> ")
        options = ['1', '2', '3', '4', 'x']

        if op in options:
            if op == 'x':
                exit()
        else:
            print("[!] Invalid Option")
            time.sleep(1.5)
            upextract()

        up.start(op)
        up.cls()
        print(green + f"[+] Extracted {up.extracted} Accounts.")
        input(cyan + "Press Enter To Continue > ")

    except:
        up.cls()
        print(red + "[!] Error")
        time.sleep(1.5)
        upextract()
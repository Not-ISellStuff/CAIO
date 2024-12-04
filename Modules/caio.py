#
#   CAIO Menu
#

import time, os
from colorama import Fore

from Modules.settings import Settings
from Modules.Checkers.bww import bww
from Modules.Checkers.plutotv import pluto
from Modules.Checkers.disney import disney
from Modules.Checkers.wwe import wwe

from Modules.CTools.caprem import caprem
from Modules.CTools.upextract import upextract

# -------------------------#

cyan = Fore.CYAN
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN

# -------------------------#

settings = Settings()

class CAIO:
    def __init__(self):
        pass

    def cls(self):
        os.system('cls')

    # ----------------------------------------- #

    def main(self):
        self.cls()
        print(cyan + r"""
         ___    __    ____  _____  [Menu]
        / __)  /__\  (_  _)(  _  ) 
       ( (__  /(__)\  _)(_  )(_)(  [Dev] - > ISellStuff
        \___)(__)(__)(____)(_____) [x] -> Exit
              
        [1] Modules
        [2] Settings
        """)
        op = input(cyan + "> ")
        options = ['1', '2', 'x']

        if op in options:
            if op == 'x':
                print(yellow + "\n[*] Closing.")
                time.sleep(1)
                exit()
        else:
            print(red + "\n[!] Invalid Option")
            time.sleep(1.5)
            self.main()

        if op == '1':
            self.menu()
        elif op == '2':
            self.settings()

    def menu(self):
        self.cls()
        print(cyan + r"""
         ___    __    ____  _____  [Main Menu]
        / __)  /__\  (_  _)(  _  ) 
       ( (__  /(__)\  _)(_  )(_)(  [Dev] - > ISellStuff
        \___)(__)(__)(____)(_____) [x] -> Exit
              
        [1] Checkers
        [2] Tools 
        
        [w] Go Back
        """)
        op = input(cyan + "> ")
        options = ['1', '2', 'x', 'w']

        if op in options:
            if op == 'x':
                print(yellow + "\n[*] Closing.")
                time.sleep(1)
                exit()
        else:
            print(red + "\n[!] Invalid Option")
            time.sleep(1.5)
            self.menu()

        if op == '1':
            self.checkers()
        elif op == '2':
            self.tools()
        elif op == 'w':
            self.main()

    # -------------- Modules ------------------ #

    def checkers(self):
        self.cls()
        print(cyan + r"""
         ___    __    ____  _____  [Checkers]
        / __)  /__\  (_  _)(  _  ) 
       ( (__  /(__)\  _)(_  )(_)(  [w] -> Go Back
        \___)(__)(__)(____)(_____) [x] -> Exit
              
        [1] Buffalo Wild Wings | Proxyless  
        [2] PlutoTV | Proxyless
        [3] Disney+ | Proxyless
        [4] WWE | Proxyless
        """)
        op = input(cyan + "> ")
        options = ['x', 'w', '1', '2', '3', '4']

        if op in options:
            if op == 'x':
                print(yellow + "[*] Closing.")
                time.sleep(1)
                exit()
            elif op == 'w':
                self.menu()
        else:
            print(red + "[!] Invalid Option")
            time.sleep(1.5)
            self.checkers()

        self.checkers_handle(op)

    def tools(self):
        self.cls()
        print(cyan + r"""
         ___    __    ____  _____  [Tools]
        / __)  /__\  (_  _)(  _  ) 
       ( (__  /(__)\  _)(_  )(_)(  [w] -> Go Back
        \___)(__)(__)(____)(_____) [x] -> Exit
              
        [1] Capture Remover | Combolist Tool
        [2] U:P Extractor | Combolist Tool""")
        op = input(cyan + "> ")
        options = ['x', 'w', '1', '2']

        if op in options:
            if op == 'x':
                print(yellow + "[*] Closing.")
                time.sleep(1)
                exit()
            elif op == 'w':
                self.menu()
        else:
            print(red + "[!] Invalid Option")
            time.sleep(1.5)
            self.tools()

        self.tools_handle(op)

    def settings(self):
        self.cls()
        print(cyan + f"""
         ___    __    ____  _____  [Settings]
        / __)  /__\  (_  _)(  _  ) 
       ( (__  /(__)\  _)(_  )(_)(  [w] -> Go Back
        \___)(__)(__)(____)(_____) [x] -> Exit
              
        Send hits to Webhook -> {settings.bool_data()[1]}
        Notify When Finished Checking -> {settings.bool_data()[0]}

        [1] Change Webhook
        [2] Enable/Disable | Sends Hits To Webhook
        [3] Enable/Disable | Notify When Finished Checking
        """)
        op = input(cyan + "> ")
        options = ['x', 'w', '1', '2', '3']

        if op in options:
            if op == 'x':
                print(yellow + "[*] Closing.")
                time.sleep(1)
                exit()
            elif op == 'w':
                self.menu()
        else:
            print(red + "[!] Invalid Option")
            time.sleep(1.5)
            self.settings()

        self.settings_handle(op)

    # ---------- Option Handlers -------------- #

    def checkers_handle(self, op):
        
        if op == '1':
            bww()
        
        elif op == '2':
            pluto()
        
        elif op == '3':
            disney()

        elif op == '4':
            wwe()

        self.checkers()

    def tools_handle(self, op):
        
        if op == '1':
            caprem()

        elif op == '2':
            upextract()

        self.tools()

    def settings_handle(self, op):
        
        if op == '1':
            settings.change_hook()
        
        elif op == '2':
            settings.hits_hook()

        elif op == '3':
            settings.notify()

        time.sleep(2.5)
        self.settings()
        
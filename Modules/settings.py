"""

CAIO Settings

"""

import os, json, requests, time
from colorama import Fore

# ------------------------ #

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW

# ------------------------ #

class Settings:
    def __init__(self):
        pass

    def cls(self):
        os.system('cls')

    def bool_data(self):
        with open('Modules/settings.json', 'r') as f:
            data = json.load(f)

        return data['notify'], data['send_hits']

    # ----------------------- #

    def change_hook(self):
        self.cls()
        hook = input(cyan + "Webhook: ")

        try:
            requests.post(hook, json={'content': 'Updated Webhook'})
            print(green + "[+] Updated Webhook")

            with open('Modules/settings.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            data['webhook'] = hook
            
            with open('Modules/settings.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)

        except:
            print(red + "\n[!] Invalid Webhook")
            time.sleep(1.5)
            self.change_hook()

    def hits_hook(self):
        self.cls()

        with open('Modules/settings.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        if data['send_hits'] == False:
            data['send_hits'] = True

            with open('Modules/settings.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(green + "[+] CAIO Will Now Send Each Hit You Get To Your Webhook")
        
        else:
            data['send_hits'] = False

            with open('Modules/settings.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)

            print(green + "[+] CAIO Will NOT Send Each Hit You Get To Your Webhook")

    def notify(self):
        self.cls()

        with open('Modules/settings.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if data['notify'] == True:
            data['notify'] = False

            with open('Modules/settings.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)

            print(green + "[+] CAIO Will NOT Notify You When It Stops Checking")
        
        else:
            data['notify'] = True

            with open('Modules/settings.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            
            print(green + "[+] CAIO Will Now Notify You When It Stops Checking")

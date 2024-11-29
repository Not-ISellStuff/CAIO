"""

CAIO File Manager

"""

import os, time
from colorama import Fore

# -------------------------#

cyan = Fore.CYAN
red = Fore.RED
yellow = Fore.YELLOW

# -------------------------#

class HitsManager:
    def __init__(self):
        pass

    # ---- Hits Manager ---- #

    def delete_hits(self):
        deleted = 0

        for n in os.listdir("Hits"):
            with open(f"Hits/{n}", 'r', encoding='utf-8') as f:
                lns = f.readlines()
                deleted += len(lns)

            with open(f"Hits/{n}", 'w') as f:
                pass

        return deleted

    def open_folder(self):
        os.startfile("Hits")

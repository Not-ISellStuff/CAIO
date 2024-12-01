import json
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(initialdir="Hits")

with open('Modules/Util/file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['path'] = path

with open('Modules/Util/file.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
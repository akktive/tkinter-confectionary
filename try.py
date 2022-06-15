from tkinter import *
import sqlite3
from tkinter.ttk import Combobox

sql = sqlite3.connect('C:\\SQLite\\CONFECTIONARY_GRISHAU.db')
db = sql.cursor()


root = Tk()

# first_listbox = Combobox()
#
# rows = db.execute("SELECT C_NAME FROM CAKES")
# for row in rows:
#     print(row)
#     first_listbox.insert(END, row)
# first_listbox.grid(column=0, row=1)

comboExample = Combobox()
rows = db.execute("SELECT C_NAME FROM CAKES")
for row in rows:
    comboExample['values'] = tuple(list(comboExample['values']) + [str(row)])
comboExample.grid(column=0, row=1)
comboExample.current(1)

root.mainloop()

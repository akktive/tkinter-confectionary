# from msilib import Table
from tkinter import *
import tkinter.ttk as ttk
import sqlite3
# from functools import partial
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import Calendar
from datetime import *

final_first = None
final_phone = None
final_cake_name = None
final_filling = None
final_decor = None
final_com = None


# Подключение к БД
sql = sqlite3.connect('C:\\SQLite\\CONFECTIONARY_GRISHAU.db')
db = sql.cursor()


class Window:
    def __init__(self, width, height, title="Бабушкино. Вход в систему", resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizable[0], resizable[1])
        self.root.configure(bg="#FDD7AA")


    def win_label(self, width, height, x, y, text, bg, font):
        label_text = Label(self.root, text=f"{text}", bg=f"{bg}", font=f"{font[0]}, {font[1]}", fg="#733C3C")
        label_text.place(width=f"{width}", height=f"{height}", x=f"{x}", y=f"{y}")

    def image_place(self):
        img = PhotoImage(file="logo2.png")
        img = img.subsample(4, 4)
        label_img = Label(self.root)
        label_img.image = img
        label_img['image'] = label_img.image
        label_img.place(x=180, y=30)

    def win_destroy(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


# class Table():
#     def __init__(self, headings=tuple(), rows=tuple()):
#         table = ttk.Treeview(show="headings", selectmode="browse")
#         table["columns"] = headings
#         table["displaycolumns"] = headings
#
#         for head in headings:
#             table.heading(head, text=head, anchor=W)
#             table.column(head, anchor=W, width=50, minwidth=50)
#
#         for row in rows:
#             table.insert('', END, values=tuple(row))
#
#         scrolltable = Scrollbar(command=table.yview)
#         table.configure(yscrollcommand=scrolltable.set)
#         scrolltable.pack(side=RIGHT, fill=Y)
#         table.pack(expand=YES, fill=BOTH)
#
#         style = ttk.Style()
#         style.theme_use("clam")
#         style.configure("Treeview", background="#FDD7AA", foreground="#C74B50")
#         style.configure("Treeview.Heading", background="#FDD7AA", foreground="#C74B50")


# Окна

def first_window():
	window.image_place()
	window.win_label(146, 30, 180, 130, text="Вход", bg="#FDD7AA", font=("Courier", 18))
	window.win_label(146, 30, 67, 170, text="Логин:", bg="#FDD7AA", font=("Courier", 16))
	window.win_label(146, 30, 60, 220, text="Пароль:", bg="#FDD7AA", font=("Courier", 16))
	global ent
	ent = Entry(font=("Courier", 18))
	ent.place(width=146, height=30, x=180, y=170)
	global ent2
	ent2 = Entry(font=("Courier", 18), show='*')
	ent2.place(width=146, height=30, x=180, y=220)
	button = Button(text="Войти", bg="#BE8C63", fg="white", font=("Courier", 14),
					command=check_enter)
	button.place(width=100, x=204, y=270)
	window.run()


def prod_window():
	global window
	window.win_destroy()
	global window2
	window2 = Window(700, 420, title="Окно продавца")

	window2.win_label(200, 30, 55, 2, text="Данные о покупателе", bg="#FDD7AA", font=("Courier", 12))
	window2.win_label(150, 30, 300, 2, text="Данные о торте", bg="#FDD7AA", font=("Courier", 12))

	window2.win_label(60, 30, 5, 50, text="Имя*:", bg="#FDD7AA", font=("Courier", 12))
	global ent_name
	ent_name = Entry(font=("Courier", 16), validate="all")
	ent_name.config(validate="key", validatecommand=(ent_name.register(callback_name), '%P'))
	ent_name.place(width=155, height=30, x=75, y=50)

	window2.win_label(60, 30, 5, 100, text="Тел*.:", bg="#FDD7AA", font=("Courier", 12))
	global ent_phone
	ent_phone = Entry(font=("Courier", 16), validate="all")
	ent_phone.config(validate="key", validatecommand=(ent_phone.register(callback_phone), '%P'))
	ent_phone.place(width=155, height=30, x=75, y=100)

	window2.win_label(130, 30, 5, 150, text="Время и дата*:", bg="#FDD7AA", font=("Courier", 12))

	window2.win_label(75, 30, 250, 50, text="Вес*:", bg="#FDD7AA", font=("Courier", 12))
	global ent_weight
	weight_var = IntVar()
	weight_var.set(2)
	ent_weight = Entry(font=("Courier", 16), validate="all", textvariable=weight_var)
	ent_weight.config(validate="key", validatecommand=(ent_weight.register(callback_tort), '%P'))
	ent_weight.place(width=155, height=30, x=315, y=50)

	window2.win_label(75, 30, 245, 100, text="Ярус*:", bg="#FDD7AA", font=("Courier", 12))
	global ent_tier
	tier_var = IntVar()
	tier_var.set(1)
	ent_tier = Entry(font=("Courier", 16), validate="all", textvariable=tier_var)
	ent_tier.config(validate="key", validatecommand=(ent_tier.register(callback_tort), '%P'))
	ent_tier.place(width=155, height=30, x=315, y=100)

	window2.win_label(75, 30, 235, 150, text="Начинка*:", bg="#FDD7AA", font=("Courier", 12))
	global combo_fil
	combo_fil = Combobox(state="readonly")
	combo_fil.configure(font=("Courier", 12))
	rows_fil = db.execute("SELECT F_NAME FROM FILLINGS")
	for row in rows_fil:
		combo_fil["values"] = tuple(list(combo_fil["values"]) + [str(row[0])])
	combo_fil.place(width=155, height=30, x=315, y=150)
	combo_fil.current(0)

	window2.win_label(75, 30, 242, 200, text="Декор*:", bg="#FDD7AA", font=("Courier", 12))
	global combo_dec
	combo_dec = Combobox(state="readonly")
	combo_dec.configure(font=("Courier", 12))
	rows_dec = db.execute("SELECT D_NAME FROM DECORS")
	for row in rows_dec:
		combo_dec["values"] = tuple(list(combo_dec["values"]) + [str(row[0])])
	combo_dec.place(width=155, height=30, x=315, y=200)
	combo_dec.current(0)

	window2.win_label(75, 30, 530, 2, text="Название:", bg="#FDD7AA", font=("Courier", 12))
	global combo_name
	combo_name = Combobox(state="readonly")
	combo_name.configure(font=("Courier", 12))
	rows_name = db.execute("SELECT C_NAME FROM CAKES")
	for row in rows_name:
		combo_name["values"] = tuple(list(combo_name["values"]) + [str(row[0])])
	combo_name.place(width=155, height=30, x=490, y=50)
	global var1
	var1 = IntVar()
	c1 = Checkbutton(text='Без названия', variable=var1, onvalue=1, offvalue=0, command=clear_name)
	c1.configure(bg="#FDD7AA", font=("Courier", 10))
	c1.place(x=490, y=85)

	window2.win_label(150, 20, 490, 125, text="Комментарий:", bg="#FDD7AA", font=("Courier", 12))
	global ent_com
	ent_com = Entry(font=("Courier", 12), justify=LEFT)
	ent_com.config(validate="key", validatecommand=(ent_com.register(callback_comm), '%P'))
	ent_com.place(width=155, height=80, x=490, y=150)

	button_1 = Button(text="Состав по\nназванию", bg="#C74B50", fg="white", font=("Courier", 14), command=get_cake_details)
	button_1.place(width=110, height=50, x=540, y=270)

	button = Button(text="Оформить\nЗАКАЗ", bg="#BE8C63", fg="white", font=("Courier", 14), command=make_order)
	button.place(width=110, height=50, x=540, y=340)

	button3 = Button(text="Предвар-я\nстоимость*", bg="#BE8C63", fg="white", font=("Courier", 14), command=count_price)
	button3.place(width=130, height=50, x=320, y=340)

	global var_price
	var_price = StringVar()
	label_price = Label(textvariable=var_price, bg="#FDD7AA", font=("Courier", 14))
	label_price.place(width=90, height=50, x=345, y=280)

	delta = date.today() + timedelta(days=14)
	global cal
	cal = Calendar(mindate=date.today(), maxdate=delta, background="#BE8C63", headersbackground="#BE8C63",
				   bordercolor="white", selectbackground="#C74B50")
	cal.place(x=20, y=240, width=210, height=160)

	global comboTime
	comboTime = Combobox(values=[
									"10:00",
									"12:00",
									"14:00",
									"16:00",
									"18:00",
									"20:00"], state="readonly")
	comboTime.configure(font=("Courier", 12))
	comboTime.place(width=155, height=30, x=20, y=190)
	comboTime.current(0)

	window2.run()


def create_entrys(row, column, pady, padx, data, i, q):
	global second_frame
	global ent100
	var1 = StringVar()
	ent100 = Entry(second_frame, font=("Courier", 16),textvariable=var1, state="readonly").grid(row=f"{row}", column=f"{column}", pady=f"{pady}", padx=f"{padx}")
	var1.set(data[i][q])


def insert_data_in_order():
	global data
	db.execute("SELECT * FROM ORDERS")
	data = list(db.fetchall())
	columns = count_columns()
	global num_of_orders
	rows = 10
	i = q = 0
	row = 1
	column = 1
	padx = 10
	pady = 10
	for a in range(columns):
		q = 0
		row = 0
		for b in range(rows):
			create_entrys(row, column, pady, padx, data, i, q)
			q += 1
			row += 1
		column += 1
		i += 1


def cond_window():
	global window
	window.win_destroy()

	window3 = Tk()
	window3.title("Окно кондитера")
	window3.geometry("900x600")
	window3.resizable(False, False)
	window3.configure(bg="#FDD7AA")

	main_frame = Frame(window3)
	main_frame.pack(fill=BOTH, expand=1)

	# Create Frame for X Scrollbar
	sec = Frame(main_frame, bg="#FDD7AA")
	sec.pack(fill=X, side=BOTTOM)

	# Create A Canvas
	my_canvas = Canvas(main_frame, bg="#FDD7AA")
	my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

	# Add A Scrollbars to Canvas
	x_scrollbar = ttk.Scrollbar(sec, orient=HORIZONTAL, command=my_canvas.xview)
	x_scrollbar.pack(side=BOTTOM, fill=X)
	# y_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
	# y_scrollbar.pack(side=RIGHT, fill=Y)

	# Configure the canvas
	my_canvas.configure(xscrollcommand=x_scrollbar.set)
	# my_canvas.configure(yscrollcommand=y_scrollbar.set)
	my_canvas.bind("<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox(ALL)))

	# Create Another Frame INSIDE the Canvas
	global second_frame
	second_frame = Frame(my_canvas, bg="#FDD7AA")

	# Add that New Frame a Window In The Canvas
	my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

	insert_data_in_order()
	lab2 = Label(second_frame, text="ID:", bg="#FDD7AA", font=("Courier", 14), fg="#733C3C").grid(row=0, column=0, padx=10, pady=10)
	lab3 = Label(second_frame, text="Тел.:", bg="#FDD7AA", font=("Courier", 14), fg="#733C3C").grid(row=1, column=0, padx=10, pady=10)
	lab4 = Label(second_frame, text="Дефолт:", bg="#FDD7AA", font=("Courier", 14), fg="#733C3C").grid(row=2, column=0, padx=10, pady=10)
	lab5 = Label(second_frame, text="Начинка:", bg="#FDD7AA", font=("Courier", 14), fg="#733C3C").grid(row=3, column=0, padx=10, pady=10)
	lab6 = Label(second_frame, text="Декор:", bg="#FDD7AA", font=("Courier", 14), fg="#733C3C").grid(row=4, column=0, padx=10, pady=10)
	lab7 = Label(second_frame, text="Коммент:", bg="#FDD7AA", font=("Courier", 14), fg="#733C3C").grid(row=5, column=0, padx=10, pady=10)
	lab8 = Label(second_frame, text="Статус:", bg="#FDD7AA", font=("Courier", 14), fg="#733C3C").grid(row=6, column=0, padx=10, pady=10)
	lab9 = Label(second_frame, text="Цена:", bg="#FDD7AA", font=("Courier", 14), fg="#733C3C").grid(row=7, column=0, padx=10, pady=10)
	lab10 = Label(second_frame, text="Дата:", bg="#FDD7AA", font=("Courier", 14), fg="#733C3C").grid(row=8, column=0, padx=10, pady=10)
	lab11 = Label(second_frame, text="Время:", bg="#FDD7AA", font=("Courier", 14), fg="#733C3C").grid(row=9, column=0, padx=10, pady=10)

	global id_combo
	id_combo = Combobox(state="readonly")
	id_combo.configure(font=("Courier", 12))
	rows_fil = db.execute("SELECT O_ID FROM ORDERS")
	for row in rows_fil:
		id_combo["values"] = tuple(list(id_combo["values"]) + [str(row[0])])
	id_combo.place(width=90, height=40, x=10, y=477)
	id_combo.current(0)
	but = Button(text="Заказ\nготов", bg="#BE8C63", fg="white", font=("Courier", 14), command=change_status)
	but.place(width=100, height=40, x=120, y=477)

	db.execute(f"SELECT BILL FROM ORDERS WHERE O_ID=?", (id_combo.get(),))
	money = db.fetchone()
	money = money[0]

	global var_money
	global ent_money
	var_money = StringVar()
	var_money.set(money)
	ent_money = Entry(textvariable=var_money, font=("Courier", 12))
	ent_money.place(width=90, height=40, x=10, y=537)
	but2 = Button(text="Утвердить\nцену", bg="#BE8C63", fg="white", font=("Courier", 14), command=insert_money)
	but2.place(width=100, height=40, x=120, y=537)

	window3.mainloop()


def insert_money():
	global ent_money
	global id_combo
	if ent_money.get() and id_combo.get():
		db.execute(f"SELECT STATUS FROM ORDERS WHERE O_ID=?", (id_combo.get(),))
		status = db.fetchone()
		if status[0] == 'Готов':
			messagebox.showerror("Ошибка", "Цена утверждена")
		else:
			db.execute(f"UPDATE ORDERS SET BILL=? WHERE O_ID=?", (ent_money.get(), id_combo.get()))
			sql.commit()
			messagebox.showinfo("Успешно", "Цена утверждена!")
			insert_data_in_order()


def change_status():
	global id_combo
	if id_combo.get():
		order_id = int(id_combo.get())
		db.execute(f"SELECT STATUS FROM ORDERS WHERE O_ID=?", (order_id,))
		status = db.fetchone()
		if status[0] == 'Готов':
			messagebox.showerror("Ошибка", "Заказ уже готов!")
		elif status:
			db.execute(f"UPDATE ORDERS SET STATUS = 'Готов' WHERE O_ID=?", (order_id,))
			sql.commit()
			messagebox.showinfo("Успешно", "Заказ готов!")
		else:
			messagebox.showerror("Ошибка", "Введите корректный номер заказа")
	else:
		messagebox.showerror("Ошибка", "Введите номер заказа")
	insert_data_in_order()


def count_columns():
	db.execute("SELECT COUNT(*) FROM ORDERS")
	data = db.fetchall()
	data = int(data[0][0])
	return data

def admin_window():
	global window
	window.win_destroy()
	global window4
	window4 = Window(700, 400, title="Окно админа")
	global tables_combo
	tables_combo = Combobox(state="readonly", values=[
														"Покупатели",
														"Торты",
														"Декор",
														"Начинки",
														"Заказы"
	])
	tables_combo.configure(font=("Courier", 18))
	tables_combo.place(width=190, height=40, x=10, y=10)
	tables_combo.current(0)

	global var_id
	global var_phone
	global var_name
	global var_f
	global var_d
	global var_com
	global var_status
	global var_bill
	global var_date
	global var_time

	var_id = StringVar()
	var_phone = StringVar()
	var_name = StringVar()
	var_f = StringVar()
	var_d = StringVar()
	var_com = StringVar()
	var_status = StringVar()
	var_bill = StringVar()
	var_date = StringVar()
	var_time = StringVar()

	global lab1
	global lab2
	global lab3
	global lab4
	global lab5
	global lab6
	global lab7
	global lab8
	global lab9
	global lab10
	global lab11
	global lab12
	global lab13
	global lab14

	lab1 = Label(text="Номер тел.:", font=("Courier", 12))
	lab2 = Label(text="Имя:", font=("Courier", 12))
	lab3 = Label(text="ID:", font=("Courier", 12))
	lab4 = Label(text="Вес:", font=("Courier", 12))
	lab5 = Label(text="Ярус:", font=("Courier", 12))
	lab6 = Label(text="ID начинки:", font=("Courier", 12))
	lab7 = Label(text="ID декора:", font=("Courier", 12))
	lab8 = Label(text="Название торта:", font=("Courier", 10))
	lab9 = Label(text="Название:", font=("Courier", 12))
	lab10 = Label(text="Цена:", font=("Courier", 12))
	lab11 = Label(text="Коммент:", font=("Courier", 12))
	lab12 = Label(text="Статус:", font=("Courier", 12))
	lab13 = Label(text="Дата:", font=("Courier", 12))
	lab14 = Label(text="Время:", font=("Courier", 12))

	global ent_id
	global ent_phone
	global ent_name
	global ent_f
	global ent_d
	global ent_com
	global ent_status
	global ent_bill
	global ent_date
	global ent_time

	ent_id = Entry(textvariable=var_id, font=("Courier", 12))
	ent_id.place(width=150, height=30, x=10, y=120)
	ent_phone = Entry(textvariable=var_phone, font=("Courier", 12))
	ent_phone.place(width=150, height=30, x=180, y=120)
	ent_name = Entry(textvariable=var_name, font=("Courier", 12))
	ent_name.place(width=150, height=30, x=350, y=120)
	ent_f = Entry(textvariable=var_f, font=("Courier", 12))
	ent_f.place(width=150, height=30, x=520, y=120)

	ent_d = Entry(textvariable=var_d, font=("Courier", 12))
	ent_d.place(width=150, height=30, x=10, y=200)
	ent_com = Entry(textvariable=var_com, font=("Courier", 12))
	ent_com.place(width=150, height=30, x=180, y=200)
	ent_status = Entry(textvariable=var_status, font=("Courier", 12))
	ent_status.place(width=150, height=30, x=350, y=200)
	ent_bill = Entry(textvariable=var_bill, font=("Courier", 12))
	ent_bill.place(width=150, height=30, x=520, y=200)

	ent_date = Entry(textvariable=var_date, font=("Courier", 12))
	ent_date.place(width=150, height=30, x=10, y=280)
	ent_time = Entry(textvariable=var_time, font=("Courier", 12))
	ent_time.place(width=150, height=30, x=180, y=280)

	button1 = Button(text="Выбрать", bg="#BE8C63", fg="white", font=("Courier", 15), command=in_up_del)
	button1.place(width=120, height=40, x=220, y=10)
	button2 = Button(text="Поиск", bg="#BE8C63", fg="white", font=("Courier", 15), command=find_info)
	button2.place(width=120, height=40, x=60, y=350)
	button3 = Button(text="Добавить", bg="#BE8C63", fg="white", font=("Courier", 15), command=in_up_del)
	button3.place(width=120, height=40, x=210, y=350)
	button4 = Button(text="Изменить", bg="#BE8C63", fg="white", font=("Courier", 15), command=in_up_del)
	button4.place(width=120, height=40, x=360, y=350)
	button5 = Button(text="Удалить", bg="#BE8C63", fg="white", font=("Courier", 15), command=in_up_del)
	button5.place(width=120, height=40, x=510, y=350)

	window4.run()


def find_info():
	global tables_combo
	global ent_id
	global ent_phone
	global var_id
	global var_phone
	global var_name
	global var_f
	global var_d
	global var_com
	global var_status
	global var_bill
	global var_date
	global var_time

	if tables_combo.get() == 'Покупатели':
		if ent_id.get():
			db.execute(f"SELECT B_NAME FROM BUYERS WHERE B_PHONE=?", (ent_id.get(),))
			name = db.fetchone()
			if name:
				var_phone.set(name[0])
			else:
				messagebox.showerror("Ошибка!", "Такого номера нет в базе!")
		else:
			messagebox.showerror("Ошибка!", "Введите номер телефона")
	elif tables_combo.get() == 'Торты':
		if ent_id.get():
			db.execute(f"SELECT * FROM CAKES WHERE C_ID=?", (ent_id.get(),))
			data = db.fetchall()
			if data:
				var_phone.set(data[0][1])
				var_name.set(data[0][2])
				var_f.set(data[0][3])
				var_d.set(data[0][4])
				var_com.set(data[0][5])


def in_up_del():
	global lab1
	global lab2
	global lab3
	global lab4
	global lab5
	global lab6
	global lab7
	global lab8
	global lab9
	global lab10
	global lab11
	global lab12
	global lab13
	global lab14

	lab1.place_forget()
	lab2.place_forget()
	lab3.place_forget()
	lab4.place_forget()
	lab5.place_forget()
	lab6.place_forget()
	lab7.place_forget()
	lab8.place_forget()
	lab9.place_forget()
	lab10.place_forget()
	lab11.place_forget()
	lab12.place_forget()
	lab13.place_forget()
	lab14.place_forget()

	#   forget all entry

	global tables_combo
	if tables_combo.get() == 'Покупатели':
		lab1.place(x=10, y=90)
		lab2.place(x=180, y=90)
	elif tables_combo.get() == 'Торты':
		lab3.place(x=10, y=90)
		lab4.place(x=180, y=90)
		lab5.place(x=350, y=90)
		lab6.place(x=520, y=90)
		lab7.place(x=10, y=170)
		lab8.place(x=180, y=170)
	elif tables_combo.get() == 'Декор':
		lab7.place(x=10, y=90)
		lab9.place(x=180, y=90)
		lab10.place(x=350, y=90)
	elif tables_combo.get() == 'Начинки':
		lab6.place(x=10, y=90)
		lab9.place(x=180, y=90)
		lab10.place(x=350, y=90)
	elif tables_combo.get() == 'Заказы':
		lab3.place(x=10, y=90)
		lab1.place(x=180, y=90)
		lab8.place(x=350, y=90)
		lab6.place(x=520, y=90)
		lab7.place(x=10, y=170)
		lab11.place(x=180, y=170)
		lab12.place(x=350, y=170)
		lab10.place(x=520, y=170)
		lab13.place(x=10, y=250)
		lab14.place(x=180, y=250)


# VALIDATION


def callback_comm(input):
	if len(str(input)) == 0:
		return True
	if len(str(input)) <= 14:
		return True
	else:
		return False


def callback_name(input):
	if len(str(input)) == 0:
		return True
	if len(str(input)) <= 14:
		return input.isalpha()
	else:
		return False


def callback_phone(input):
	if len(str(input)) == 0:
		return True
	if len(str(input)) <= 11:
		return input.isdigit()
	else:
		return False


def callback_tort(input):
	if len(str(input)) == 0:
		return True
	if len(str(input)) == 1:
		if str(input) != '0':
			return input.isdigit()
		else:
			return False
	else:
		return False


def check_enter():
	login = ent.get()
	password = ent2.get()
	db.execute("SELECT E_LOGIN, E_PASSWORD FROM EMPLOYEES WHERE E_LOGIN=? AND E_PASSWORD=?", (login, password))
	if db.fetchall():
		db.execute("SELECT E_POSITION FROM EMPLOYEES WHERE E_LOGIN=?", (login,))
		zapros = db.fetchone()
		if zapros == ('Кондитер 1', ):
			cond_window()
		if zapros == ('Продавец 1', ):
			prod_window()
		if zapros == ('Админ 1', ):
			admin_window()
	else:
		messagebox.showerror("Ошибка входа", "Неправильный логин или пароль!")


def get_cake_details():
	global final_cake_name
	final_cake_name = combo_name.get()
	if final_cake_name == "":
		messagebox.showerror("OШИБКА", "Выберите название и повторите попытку!")
	else:
		db.execute("SELECT F_ID FROM CAKES WHERE C_NAME=?", (final_cake_name,))
		global final_filling
		final_filling = db.fetchone()
		if final_filling != "":
			final_filling = int(final_filling[0]) - 1
			combo_fil.current(final_filling)
		db.execute("SELECT D_ID FROM CAKES WHERE C_NAME=?", (final_cake_name,))
		global final_decor
		final_decor = db.fetchone()
		if final_decor != "":
			final_decor = int(final_decor[0]) - 1
			combo_dec.current(final_decor)
		final_decor = combo_dec.get()
		db.execute("SELECT D_ID FROM DECORS WHERE D_NAME=?", (final_decor,))
		final_decor = db.fetchone()
		if final_decor != "":
			final_decor = int(final_decor[0])
		final_filling = combo_fil.get()
		db.execute("SELECT F_ID FROM FILLINGS WHERE F_NAME=?", (final_filling,))
		final_filling = db.fetchone()
		if final_filling is not None:
			final_filling = int(final_filling[0])
	if ent_com.get() != "":
		global final_com
		final_com = ent_com.get()


def clear_name():
	global final_cake_name
	if var1.get() == 1:
		global final_cake_name
		final_cake_name = ""
		combo_name.set('')
		combo_name.configure(state="disabled")
	else:
		combo_name.configure(state="readonly")


def make_order():
	if ent_name.get() == "" or ent_phone.get() == "" or ent_tier.get() == "" or ent_weight.get() == "" or var_price.get() == "":
		messagebox.showerror("OШИБКА", "Заполните все поля и повторите попытку!")
	else:
		db.execute(f"SELECT B_NAME FROM BUYERS WHERE B_PHONE=?", (ent_phone.get(),))
		global buyer_name
		buyer_name = db.fetchone()
		if buyer_name:
			if combo_name.get() != "":
				insert_order(combo_name.get(), "", "", ent_com.get())
			else:
				insert_order("", combo_fil.get(), combo_dec.get(), ent_com.get())
		else:
			insert_buyer()
			if combo_name.get() != "":
				insert_order(combo_name.get(), "", "", ent_com.get())
			else:
				insert_order("", combo_fil.get(), combo_dec.get(), ent_com.get())


def insert_buyer():
	db.execute(f"INSERT INTO BUYERS (B_PHONE, B_NAME) VALUES ('{ent_phone.get()}', '{ent_name.get()}')")
	sql.commit()


def insert_order(cake_name, filling, decor, comment):
	db.execute(f"INSERT INTO ORDERS (BUYER_PHONE, CAKE_NAME, FILLING_NAME, DECOR_NAME, COMMENT, STATUS, BILL, DATE, TIME) VALUES"
			   f" ('{ent_phone.get()}', '{cake_name}', '{filling}', '{decor}', '{comment}', 'В работе',"
			   f"'{var_price.get()}', '{cal.get_date()}', '{comboTime.get()}')")
	sql.commit()
	messagebox.showinfo("УСПЕШНО!", "Заказ принят!")


def count_price():
	if ent_tier.get() == "" or ent_weight.get() == "":
		messagebox.showerror("OШИБКА", "Заполните все поля и повторите попытку!")
	else:
		weight = int(ent_weight.get())
		db.execute(f"SELECT F_PRICE FROM FILLINGS WHERE F_NAME=?", (combo_fil.get(),))
		filling = db.fetchone()
		if filling is not None:
			filling = float(filling[0])
		db.execute(f"SELECT D_PRICE FROM DECORS WHERE D_NAME=?", (combo_dec.get(),))
		decor = db.fetchone()
		if decor is not None:
			decor = float(decor[0])
		price = 1200 + (weight*filling) + (weight*decor)
		price = str(price)
		var_price.set(price)


if __name__ == "__main__":
	window = Window(500, 350)
	first_window()

import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import simpledialog

def username(text):
    window = tk.Tk()
    window.withdraw()
    user_input = simpledialog.askstring(title="username", prompt=text)
    window.destroy()
    return user_input

class Moneymanage:
    user = username("name")
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("가계부")
        self.window.resizable(False, False)
        self.window.geometry("1000x700")

        self.date = tk.StringVar(self.window)
        self.money = tk.IntVar(self.window)
        self.category = tk.StringVar(self.window)
        self.balance = tk.StringVar(self.window)

        ##### FRAME #####
        self.fr_title = tk.Frame(self.window, width=700, height=50,bd=8, relief="raise")
        self.fr_title.pack(side=tk.TOP)
        self.fr_table = tk.Frame(self.window, width=500, height=500,bd=8, relief="raise")
        self.fr_table.pack(side=tk.RIGHT)
        self.fr_input = tk.Frame(self.window, width=500, height=500, bd=8, relief="raise")
        self.fr_input.pack(side=tk.LEFT)
        self.fr_forms = tk.Frame(self.fr_input, width=200, height=450)
        self.fr_forms.pack(side=tk.TOP)
        self.fr_button = tk.Frame(self.fr_input, width=500, height=100, bd=8, relief="raise")
        self.fr_button.pack(side=tk.BOTTOM)
        self.fr_combobox = tk.Frame(self.fr_forms)
        self.fr_radiobutton = tk.Frame(self.fr_forms)

        ##### LABEL #####
        self.lbl_title = tk.Label(self.fr_title, width=700, text="MONEY MANAGE")
        self.lbl_title.pack()
        self.lbl_date = tk.Label(self.fr_forms, text="Date")
        self.lbl_date.grid(row=0, column=0)
        self.lbl_balance = tk.Label(self.fr_forms, text="Balance")
        self.lbl_balance.grid(row=1, column=0)
        self.lbl_money = tk.Label(self.fr_forms, text="Money")
        self.lbl_money.grid(row=2, column=0)
        self.lbl_category = tk.Label(self.fr_forms, text="Category")
        self.lbl_category.grid(row=3, column=0)
        self.txt_total = tk.Label(self.fr_forms, text="Total")
        self.txt_total.grid(row=4, column=0)
        self.txt_result = tk.Label(self.fr_button)
        self.txt_result.pack(side=tk.TOP)

        ##### BUTTON #####
        self.btn_add = tk.Button(self.fr_button, width=10, text="Add", command=self.data_add)
        self.btn_add.pack(side=tk.LEFT)
        self.btn_delete = tk.Button(self.fr_button, width=10, text="Delete", command=self.data_delete)
        self.btn_delete.pack(side=tk.LEFT)
        self.btn_graph = tk.Button(self.fr_button, width=10, text="Graph", command=self.data_graph)
        self.btn_graph.pack(side=tk.LEFT)
        self.btn_graph = tk.Button(self.fr_button, width=10, text="Clear", command=self.clear)
        self.btn_graph.pack(side=tk.LEFT)

        ##### VALUES #####
        self.ent_date = tk.Entry(self.fr_forms, textvariable=self.date, width=30)
        self.ent_date.grid(row=0, column=1)
        self.income = tk.Radiobutton(self.fr_radiobutton, text = "Income", variable=self.balance, value="income").pack(side=tk.LEFT)
        self.outcome = tk.Radiobutton(self.fr_radiobutton, text = "Outcome", variable=self.balance, value="outcome").pack(side=tk.LEFT)
        self.fr_radiobutton.grid(row=1, column=1)
        self.ent_money = tk.Entry(self.fr_forms, textvariable= self.money, width=30)
        self.ent_money.grid(row=2, column=1)
        self.combobox = ttk.Combobox(self.fr_forms, textvariable=self.category, width=5)
        self.combobox['values'] = ['allowance','salary','food', 'transportation', 'apparel', 'saving', 'entertainment', 'etc']
        self.combobox.current(0)
        self.combobox.grid(row=3,column=1)

        ##### TABLE #####
        self.tree = ttk.Treeview(self.fr_table, columns=("ID","Date", "Balance", "Money", "Category"),
                            selectmode="extended", height=500)
        self.tree.heading('ID', text="ID")
        self.tree.heading('Date', text="Date")
        self.tree.heading('Balance', text="Balance")
        self.tree.heading('Money', text="Money")
        self.tree.heading('Category', text="Category")
        self.tree.column('#0', minwidth=0,width=30)
        self.tree.column('#1', minwidth=0,width=100)
        self.tree.column('#2', minwidth=0,width=100)
        self.tree.column('#3', minwidth=0,width=100)
        self.tree.column('#4', minwidth=0,width=100)
        self.tree.pack()

        ##### DATABASE #####
        self.conn = sqlite3.connect(f'{self.user}.db')
        self.cur = self.conn.cursor()
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.user} (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, balance TEXT, money INT, category TEXT)")

        self.data_display()
        self.window.mainloop()
        self.cur.close()
        self.conn.close()

    def fetch(self):
        self.cur.execute(f"SELECT * from {self.user}")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute(f"DELETE from {self.user} where id=?", (id,))
        self.conn.commit()

    def data_display(self):
        self.tree.delete(*self.tree.get_children())
        for i, row in enumerate(self.fetch()):
            self.tree.insert("", i, values=row)

    def data_set(self):
        self.date.set("")
        self.balance.set("")
        self.money.set("")
        self.category.set("")

    def data_add(self):
        try:
            if self.ent_date.get() == "" or self.money.get() == "" or self.balance.get()!="income" and self.balance.get()!="outcome":
                self.txt_result.config(text="Fail : Fill the values", fg="red")

            else:
                self.cur.execute(f"INSERT INTO {self.user} (date, balance, money, category) VALUES(?, ?, ?, ?)",
                                 (self.ent_date.get(), self.balance.get(), self.money.get(), self.combobox.get()))
                self.conn.commit()
                self.data_set()
                self.data_display()
                self.txt_result.config(text="Success", fg="green")
                self.cur.execute(f"SELECT * FROM {self.user}")
                rows = self.cur.fetchall()
                cols = [column[0] for column in self.cur.description]
                df = pd.DataFrame.from_records(data=rows, columns=cols)
                income = df[df['balance'] == "income"]
                sum_income = income['money'].sum()
                outcome = df[df['balance'] == "outcome"]
                sum_outcome = outcome['money'].sum()
                total = sum_income - sum_outcome
                self.txt_total.config(text=f"{total}", fg="blue")
                self.txt_total.grid(row=4, column=1)

        except tk.TclError:
            self.txt_result.config(text="Fail : values type error", fg="red")

    def data_delete(self):
        global row
        self.tree.delete(*self.tree.get_children())
        for row in self.fetch():
            self.tree.insert("", 0, values=row)
        self.remove(row[0])
        self.data_set()
        self.data_display()

    def clear(self):
        self.cur.execute(f"DELETE FROM {self.user}")
        self.cur.execute(f"UPDATE SQLITE_SEQUENCE SET seq=0 WHERE name ='{self.user}'")
        self.conn.commit()
        self.data_set()
        self.data_display()

    def data_graph(self):
        self.cur.execute(f"SELECT * FROM {self.user}")
        rows = self.cur.fetchall()
        cols = [column[0] for column in self.cur.description]
        df = pd.DataFrame.from_records(data=rows, columns=cols)
        df.to_csv(f'{self.user}.csv', sep=",", na_rep='NaN', encoding='utf-8-sig')

        plt.rcParams['axes.unicode_minus'] = False
        classes = ['food', 'transportation', 'apparel', 'saving', 'entertainment', 'etc']

        f = open(f"{self.user}.csv", encoding='utf-8')
        lines = f.readlines()

        outcome = [int(x.split(",")[4]) for x in lines[1:]]
        category_1 = [str(x.split(",")[5]) for x in lines[1:]]
        category_2 = ''.join(map(str, category_1))
        category = category_2.split()

        a_1 = []
        x = []
        if "food" in category:
            for i in range(len(category)):
                if category[i] == "food":
                    x.append(i)
        for i in range(len(x)):
            a_1.append(outcome[x[i]])
        a = sum(a_1)

        b_1 = []
        y = []
        if "transportation" in category:
            for i in range(len(category)):
                if category[i] == "transportation":
                    y.append(i)
        for i in range(len(y)):
            b_1.append(outcome[y[i]])
        b = sum(b_1)

        c_1 = []
        z = []
        if "entertainment" in category:
            for i in range(len(category)):
                if category[i] == "entertainment":
                    z.append(i)
        for i in range(len(z)):
            c_1.append(outcome[z[i]])
        c = sum(c_1)

        d_1 = []
        l = []
        if "apparel" in category:
            for i in range(len(category)):
                if category[i] == "apparel":
                    l.append(i)
        for i in range(len(l)):
            d_1.append(outcome[l[i]])
        d = sum(d_1)

        e_1 = []
        m = []
        if "saving" in category:
            for i in range(len(category)):
                if category[i] == "saving":
                    m.append(i)
        for i in range(len(m)):
            e_1.append(outcome[m[i]])
        e = sum(e_1)

        f_1 = []
        n = []
        if "etc" in category:
            for i in range(len(category)):
                if category[i] == "etc":
                    n.append(i)
        for i in range(len(n)):
            f_1.append(outcome[n[i]])
        f = sum(f_1)

        slices = [a, b, c, d, e, f]

        colors = ['lightblue', 'green', 'orange', 'Yellow', 'gold', 'pink']

        if sum(slices) != 0:
            plt.pie(slices, autopct='%2.3f%%', colors=colors, labels=classes)
            plt.legend(loc=(1, 0.7))
            plt.show()
        else:
            self.txt_result.config(text="Faile : Data is not available.", fg="red")

def main():
    Moneymanage()

if __name__ == '__main__':
    main()

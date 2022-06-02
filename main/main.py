import tkinter
import tkinter as tk
import sqlite3
import tkinter.ttk as ttk
import pandas as pd
import matplotlib.pyplot as plt

class Moneymanage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("가계부")
        self.window.resizable(False, False)
        self.window.geometry("1000x700")

        self.date = tk.StringVar()
        self.money = tk.IntVar()
        self.category = tk.StringVar()
        self.balance = tk.StringVar()

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
        self.btn_read = tk.Button(self.fr_button, width=10, text="Read", command=self.data_read)
        self.btn_read.pack(side=tk.LEFT)
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
        self.combobox['values'] = ['용돈','급여','식비', '교통비', '쇼핑비', '저축', '문화생활비', '기타']
        self.combobox.current(0)
        self.combobox.grid(row=3,column=1)

        ##### TABLE #####
        self.tree = ttk.Treeview(self.fr_table, columns=("Date", "Balance", "Money", "Category","Total"),
                            selectmode="extended", height=500)
        self.tree.heading('Date', text="Date")
        self.tree.heading('Balance', text="Balance")
        self.tree.heading('Money', text="Money")
        self.tree.heading('Category', text="Category")
        self.tree.heading('Total', text="Total")
        self.tree.column('#0', minwidth=0,width=0)
        self.tree.column('#1', minwidth=0,width=100)
        self.tree.column('#2', minwidth=0,width=100)
        self.tree.column('#3', minwidth=0,width=100)
        self.tree.column('#4', minwidth=0,width=100)
        self.tree.column('#5', minwidth=0, width=100)
        self.tree.pack()

        ##### DATABASE #####
        self.conn = sqlite3.connect('money_manager.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS money_manager (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, balance TEXT, money INT, category TEXT)")

        self.window.mainloop()

    def data_set(self):
        self.date.set("")
        self.balance.set("")
        self.money.set("")

    def total(self):
        self.cur.execute("SELECT * FROM money_manager")
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

    def data_add(self):
        try:
            if self.ent_date.get() == "" or self.money.get() == "":
                self.txt_result.config(text="Fail : Fill the values", fg="red")

            else:
                self.cur.execute("INSERT INTO `money_manager` (date, balance, money, category) VALUES(?, ?, ?, ?)",
                                 (self.ent_date.get(), self.balance.get(), self.money.get(), self.combobox.get()))
                self.conn.commit()
                self.data_set()
                self.txt_result.config(text="Success", fg="green")
                self.cur.execute("SELECT * FROM money_manager")
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

        except tkinter.TclError:
            self.txt_result.config(text="Fail : values type error", fg="red")



    def data_graph(self):
        self.cur.execute("SELECT * FROM money_manager")
        rows = self.cur.fetchall()
        cols = [column[0] for column in self.cur.description]
        df = pd.DataFrame.from_records(data=rows, columns=cols)
        df.to_csv('money_manage.csv', sep=",", na_rep='NaN', encoding='utf-8-sig')

        plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
        plt.rcParams['axes.unicode_minus'] = False

        classes = ['식비', '교통비', '쇼핑비', '저축', '문화생활비', '기타']

        f = open("money_manage.csv", encoding='utf-8')
        lines = f.readlines()
        date = [(x.split(",")[2]) for x in lines[1:]]
        outcome = [int(x.split(",")[4]) for x in lines[1:]]
        category_1 = [str(x.split(",")[5]) for x in lines[1:]]
        category_2 = ''.join(map(str, category_1))
        category = category_2.split()

        a_1 = []
        x = []
        if "식비" in category:
            for i in range(len(category)):
                if category[i] == "식비":
                    x.append(i)
        for i in range(len(x)):
            a_1.append(outcome[x[i]])
        a = sum(a_1)

        b_1 = []
        y = []
        if "교통비" in category:
            for i in range(len(category)):
                if category[i] == "교통비":
                    y.append(i)
        for i in range(len(y)):
            b_1.append(outcome[y[i]])
        b = sum(b_1)

        c_1 = []
        z = []
        if "문화생활비" in category:
            for i in range(len(category)):
                if category[i] == "문화생활비":
                    z.append(i)
        for i in range(len(z)):
            c_1.append(outcome[z[i]])
        c = sum(c_1)

        d_1 = []
        l = []
        if "쇼핑비" in category:
            for i in range(len(category)):
                if category[i] == "쇼핑비":
                    l.append(i)
        for i in range(len(l)):
            d_1.append(outcome[l[i]])
        d = sum(d_1)

        e_1 = []
        m = []
        if "저축" in category:
            for i in range(len(category)):
                if category[i] == "저축":
                    m.append(i)
        for i in range(len(m)):
            e_1.append(outcome[m[i]])
        e = sum(e_1)

        f_1 = []
        n = []
        if "기타" in category:
            for i in range(len(category)):
                if category[i] == "기타":
                    n.append(i)
        for i in range(len(n)):
            f_1.append(outcome[n[i]])
        f = sum(f_1)

        slices = [a, b, c, d, e, f]

        colors = ['lightblue', 'green', 'orange', 'Yellow', 'gold', 'pink']

        plt.pie(slices, autopct='%2.3f%%', colors=colors, labels=classes)

        plt.legend(loc=(1, 0.7))
        plt.show()


    def data_delete(self):
        pass

    def clear(self):
        self.cur.execute("DELETE from money_manager")
        self.tree.delete(*self.tree.get_children())
        self.conn.commit()
        self.data_set()

    def data_read(self):
        self.cur.execute("SELECT * from money_manager")
        fetch = self.cur.fetchall()
        for data in fetch:
            self.tree.insert('', 'end', values=(data[1], data[2], data[3], data[4]))
        self.txt_result.config(text="Successfully read data", fg="black")

def main():
    Moneymanage()

if __name__ == '__main__':
    main()
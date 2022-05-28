import tkinter as tk
import sqlite3
import tkinter.ttk as ttk

class Moneymanage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("가계부")

        self.date = tk.StringVar()
        self.income = tk.StringVar()
        self.outcome = tk.StringVar()
        self.category = tk.StringVar()
        self.total = 100000
        self.title = tk.Frame(self.window, width=900, height=50)
        self.title.pack()

        self.forms = tk.Frame(self.window, width=300, height=450)
        self.forms.pack(side=tk.TOP)
        self.fr_input = tk.Frame(self.window, width=300, height=500)
        self.fr_input.pack(side=tk.LEFT)
        self.ent_date = tk.Entry(self.fr_input, textvariable=self.date, width=30)
        self.ent_date.grid(row=0, column=1)
        self.ent_income = tk.Entry(self.fr_input, textvariable=self.income, width=30)
        self.ent_income.grid(row=1, column=1)
        self.ent_outcome = tk.Entry(self.fr_input, textvariable=self.outcome, width=30)
        self.ent_outcome.grid(row=2, column=1)
        self.ent_category = tk.Entry(self.fr_input, textvariable=self.category, width=30)
        self.ent_category.grid(row=3, column=1)
        self.lbl_date = tk.Label(self.fr_input, text="Date")
        self.lbl_date.grid(row=0, column=0)
        self.lbl_income = tk.Label(self.fr_input, text="Income")
        self.lbl_income.grid(row=1, column=0)
        self.lbl_outcome = tk.Label(self.fr_input, text="Outcome")
        self.lbl_outcome.grid(row=2, column=0)
        self.lbl_category = tk.Label(self.fr_input, text="Category")
        self.lbl_category.grid(row=3, column=0)


        self.fr_table = tk.Frame(self.window, width=300, height=500)
        self.fr_table.pack(side=tk.RIGHT)
        self.tree = ttk.Treeview(self.fr_table, columns=("Date", "Income", "Outcome", "Category", "Total"),
                            selectmode="extended", height=500)
        self.tree.heading('Date', text="Date")
        self.tree.heading('Income', text="Income")
        self.tree.heading('Outcome', text="Outcome")
        self.tree.heading('Category', text="Category")
        self.tree.heading('Total', text="Total")
        self.tree.column('#0', minwidth=0, width=0)
        self.tree.column('#1', minwidth=0, width=80)
        self.tree.column('#2', minwidth=0, width=120)
        self.tree.column('#3', minwidth=0, width=80)
        self.tree.column('#4', minwidth=0, width=150)
        self.tree.column('#5', minwidth=0, width=120)
        self.tree.pack()


        self.fr_button = tk.Frame(self.fr_input, width=300, height=100)
        self.fr_button.pack(side=tk.BOTTOM)
        self.btn_add = tk.Button(self.fr_button, width=10, text="ADD", command=self.data_add)
        self.btn_add.pack(side=tk.LEFT)
        self.txt_result = tk.Label(self.fr_button)
        self.txt_result.pack(side=tk.TOP)

        self.conn = sqlite3.connect('money_manager.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS money_manager (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,  income INTERGER, outcome INTERGER, category TEXT, total INTERGER)")

        self.window.mainloop()

    def data_add(self):
        if self.ent_date.get() =="" or self.ent_income.get() == "" or self.ent_outcome.get() == "" or self.ent_category.get():
            self.txt_result.config(text="Please complete the required field!", fg="red")
        else:
            self.cur.execute("INSERT INTO `money_manager` (date, income, outcome, category, total) VALUES(?, ?, ?, ?, ?)",
                             (str(self.ent_date.get()), str(self.ent_income.get()), str(self.ent_outcome.get()), str(self.ent_category.get()), int(self.total)))
            self.conn.commit()
            self.date.set("")
            self.category.set("")
            self.income.set("")
            self.outcome.set("")
            self.total.set("")
            self.cur.close()
            self.conn.close()
            self.txt_result.config(text="Add a data!", fg="green")

    def data_read(self):
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("SELECT * FROM 'money_manager' ORDER BY 'date' ASC")
        fetch = self.cur.fetchall()
        for data in fetch:
            self.tree.insert('', 'end', values=(data[1], data[2], data[3], data[4], data[5], data[6]))
        self.cur.close()
        self.conn.close()
        self.txt_result.config(text="Successfully read the data from database", fg="black")

def main():
    Moneymanage()

if __name__ == '__main__':
    main()

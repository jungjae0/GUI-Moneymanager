import tkinter as tk
import sqlite3
import tkinter.ttk as ttk

class Moneymanage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("가계부")
        self.window.resizable(True, True)
        self.window.geometry("900x500")

        self.date = tk.StringVar()
        self.income = tk.IntVar()
        self.outcome = tk.IntVar()
        self.category = tk.StringVar()

        ##### FRAME #####
        self.fr_title = tk.Frame(self.window, width=900, height=50, bg="black",bd=8, relief="raise")
        self.fr_title.pack(side=tk.TOP)
        self.fr_table = tk.Frame(self.window, width=300, height=500,bd=8, relief="raise")
        self.fr_table.pack(side=tk.RIGHT)
        self.fr_input = tk.Frame(self.window, width=600, height=500, bd=8, relief="raise")
        self.fr_input.pack(side=tk.LEFT)
        self.fr_forms = tk.Frame(self.fr_input, width=300, height=450)
        self.fr_forms.pack(side=tk.TOP)
        self.fr_button = tk.Frame(self.fr_input, width=300, height=100, bd=8, relief="raise")
        self.fr_button.pack(side=tk.BOTTOM)
        self.fr_combobox = tk.Frame(self.fr_forms)

        ##### LABEL #####
        self.lbl_title =  tk.Label(self.fr_title, width=900, text="MONEY MANAGE")
        self.lbl_title.pack()
        self.lbl_date = tk.Label(self.fr_forms, text="Date")
        self.lbl_date.grid(row=0, column=0)
        self.lbl_income = tk.Label(self.fr_forms, text="Income")
        self.lbl_income.grid(row=1, column=0)
        self.lbl_outcome = tk.Label(self.fr_forms, text="Outcome")
        self.lbl_outcome.grid(row=2, column=0)
        self.lbl_category = tk.Label(self.fr_forms, text="Category")
        self.lbl_category.grid(row=3, column=0)
        self.txt_result = tk.Label(self.fr_button)
        self.txt_result.pack(side=tk.TOP)

        ##### BUTTON #####
        self.btn_add = tk.Button(self.fr_button, width=10, text="ADD", command=self.data_add)
        self.btn_add.pack(side=tk.LEFT)
        self.btn_read = tk.Button(self.fr_button, width=10, text="READ", command=self.data_read)
        self.btn_read.pack(side=tk.LEFT)
        self.btn_delete = tk.Button(self.fr_button, width=10, text="DELETE", command=self.data_delete)
        self.btn_delete.pack(side=tk.LEFT)
        self.btn_graph = tk.Button(self.fr_button, width=10, text="GRAPH", command=self.data_graph)
        self.btn_graph.pack(side=tk.LEFT)

        ##### VALUES #####
        self.ent_date = tk.Entry(self.fr_forms, textvariable=self.date, width=30)
        self.ent_date.grid(row=0, column=1)
        self.combobox = ttk.Combobox(self.fr_forms, textvariable=self.category, width=5)
        self.combobox['values'] = ["용돈","급여","식비","생활비", "교통비", "저축", "문화생활비", "기타"]
        self.combobox.current(0)
        self.combobox.grid(row=3,column=1)
        self.ent_income = tk.Entry(self.fr_forms, textvariable=self.income, width=30)
        self.ent_income.grid(row=1, column=1)
        self.ent_outcome = tk.Entry(self.fr_forms, textvariable=self.outcome, width=30)
        self.ent_outcome.grid(row=2, column=1)

        ##### TABLE #####
        self.tree = ttk.Treeview(self.fr_table, columns=("Date", "Income", "Outcome", "Category"),
                            selectmode="extended", height=500)
        self.tree.heading('Date', text="Date")
        self.tree.heading('Income', text="Income")
        self.tree.heading('Outcome', text="Outcome")
        self.tree.heading('Category', text="Category")
        # self.tree.heading('Total', text="Total")
        self.tree.column('#0', minwidth=0, width=0)
        self.tree.column('#1', minwidth=0, width=120)
        self.tree.column('#2', minwidth=0, width=100)
        self.tree.column('#3', minwidth=0, width=100)
        self.tree.column('#4', minwidth=0, width=100)
        # self.tree.column('#5', minwidth=0, width=100)
        self.tree.pack()

        ##### DATABASE #####
        self.conn = sqlite3.connect('money_manager.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS money_manager (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,  income INT outcome INT, category TEXT)")

        self.window.mainloop()

    def data_add(self):
        try:
            if self.ent_date.get() =="" or self.ent_income.get() == "" or self.ent_outcome.get() == "":
                self.txt_result.config(text="Fail : Fill the income or outcome interger", fg="red")

            else:
                self.cur.execute("INSERT INTO `money_manager` (date, income, outcome, category) VALUES(?, ?, ?, ?)",
                                 (self.ent_date.get(), self.ent_income.get(), self.ent_outcome.get(), self.combobox.get()))
                self.conn.commit()
                self.date.set("")
                self.category.set("")
                self.income.set("")
                self.outcome.set("")
                self.cur.close()
                self.conn.close()
                self.txt_result.config(text="Complete", fg="green")

        except sqlite3.OperationalError:
            self.txt_result.config(text="Fail : values type error", fg="red")

    def data_graph(self):
        pass

    def data_delete(self):
        pass

    def data_read(self):
        self.conn = sqlite3.connect('money_manager.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS money_manager (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,  income INT outcome INT, category TEXT)")
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("SELECT * FROM 'money_manager' ORDER BY 'date' ASC")
        fetch = self.cur.fetchall()
        for data in fetch:
            self.tree.insert('', 'end', values=(data[1], data[2], data[3], data[4]))
        self.cur.close()
        self.conn.close()
        self.txt_result.config(text="Successfully read the data from database", fg="black")

def main():
    Moneymanage()

if __name__ == '__main__':
    main()

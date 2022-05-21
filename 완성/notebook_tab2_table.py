import tkinter as tk
from tkinter import ttk
import csv

class MoneyManage:
    def __init__(self):
        # main
        self.window = tk.Tk()
        self.window.title("가계부")

        self.tabcontrol = ttk.Notebook(self.window)

        # tab1
        self.tab1 = ttk.Frame(self.tabcontrol)
        self.tabcontrol.add(self.tab1, text = "가계부_사용자 입력")
        self.tabcontrol.pack(expand=1, fill = "both")

        # tab2
        self.tab2 = ttk.Frame(self.tabcontrol)
        self.tabcontrol.add(self.tab2, text="가계부_표")
        self.tabcontrol.pack(expand=1, fill="both")

        self.tree = ttk.Treeview(self.tab2, height=25, selectmode='extended')
        self.tree.pack()

        self.tree["columns"] = ("one", "two", "three", "four", "five")
        self.tree.column("one", width=120)
        self.tree.column("two", width=120)
        self.tree.column("three", width=120)
        self.tree.column("four", width=120)
        self.tree.column("five", width=120)
        self.tree.heading("one", text="날짜")
        self.tree.heading("two", text="항목")
        self.tree.heading("three", text="수입")
        self.tree.heading("four", text="지출")
        self.tree.heading("five", text="현재금액")
        self.tree["show"] = "headings"

        self.btn_load = tk.Button(self.tab2, text="불러오기", command=self.load_csv)
        self.btn_load.pack()
        self.btn_save = tk.Button(self.tab2, text="저장", command=self.save_csv)
        self.btn_save.pack()

        self.window.mainloop()

    def load_csv(self):
        with open("new.csv") as myfile:
            csvread = csv.reader(myfile, delimiter=',')

            for row in csvread:
                print('load row:', row)
                self.tree.insert("", 'end', values=row)

    def save_csv(self):
        with open("new.csv", "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')

            for row_id in self.tree.get_children():
                row = self.tree.item(row_id)['values']
                print('save row:', row)
                csvwriter.writerow(row)

def main():
    MoneyManage()

if __name__ == '__main__':
    main()


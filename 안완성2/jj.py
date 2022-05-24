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
        self.tabcontrol.add(self.tab1, text="가계부_사용자 입력")
        self.tabcontrol.pack(expand=1, fill="both")

        self.date = tk.IntVar(self.tab1)
        self.money_get = tk.IntVar(self.tab1)
        self.money_pay = tk.IntVar(self.tab1)
        self.category = tk.StringVar(self.tab1, value="")

        # 날짜 입력
        self.lbl_date = tk.Label(self.tab1, text="날짜").grid(row=0, column=0)
        self.ent_date = tk.Entry(self.tab1, textvariable=self.date, width=30)
        self.ent_date.grid(row=0, column=1, padx=20)

        # 수입 입력
        self.lbl_money_get = tk.Label(self.tab1, text="수입").grid(row=1, column=0)
        self.ent_money_get = tk.Entry(self.tab1, textvariable=self.money_get, width=30)
        self.ent_money_get.grid(row=1, column=1, padx=20)

        # 지출 입력
        self.lbl_money_pay = tk.Label(self.tab1, text="지출").grid(row=2, column=0)
        self.ent_money_pay = tk.Entry(self.tab1, textvariable=self.money_pay, width=30)
        self.ent_money_pay.grid(row=2, column=1, padx=20)

        # 항목 입력
        self.lbl_category = tk.Label(self.tab1, text="항목").grid(row=3, column=0)
        self.ent_category = tk.Entry(self.tab1, textvariable=self.category, width=30)
        self.ent_category.grid(row=3, column=1, padx=20)

        # 입력하기
        self.btn_enter = tk.Button(self.tab1, text="확인", command=self.enter, fg="blue").grid(row=4, column=2)

        # 결과 표시
        self.lbl_result = tk.Label(self.tab1, text="현재금액")
        self.lbl_result.grid(row=5, column=0)
        self.lbl_code = tk.Label(self.tab1)
        self.lbl_code.grid(row=5, column=1)

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
        with open("../termtest/new.csv") as myfile:
            csvread = csv.reader(myfile, delimiter=',')

            for row in csvread:
                print('load row:', row)
                self.tree.insert("", 'end', values=row)

    def save_csv(self):
        with open("../termtest/new.csv", "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')

            for row_id in self.tree.get_children():
                row = self.tree.item(row_id)['values']
                print('save row:', row)
                csvwriter.writerow(row)
    def enter(self):
        encode_result = self.enter_encode()
        self.lbl_code["text"] = f"{encode_result}"

    def enter_encode(text):


def main():
    MoneyManage()

if __name__ == '__main__':
    main()
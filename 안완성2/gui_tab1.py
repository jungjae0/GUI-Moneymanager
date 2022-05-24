import tkinter as tk

class MoneyManage():
    def __init__(self,window):
        window.title("소비/지출")
        self.date = tk.IntVar(window)
        self.money_get = tk.IntVar(window)
        self.money_pay = tk.IntVar(window)
        self.category = tk.StringVar(window, value="")

        # 날짜 입력
        self.lbl_date = tk.Label(window, text = "날짜").grid(row=0, column=0)
        self.ent_date = tk.Entry(window, textvariable=self.date, width=30)
        self.ent_date.grid(row=0, column=1, padx=20)

        # 수입 입력
        self.lbl_money_get = tk.Label(window, text = "수입").grid(row=1, column=0)
        self.ent_money_get = tk.Entry(window, textvariable=self.money_get, width=30)
        self.ent_money_get.grid(row=1, column=1, padx=20)

        # 지출 입력
        self.lbl_money_pay = tk.Label(window, text="지출").grid(row=2, column=0)
        self.ent_money_pay = tk.Entry(window, textvariable=self.money_pay, width=30)
        self.ent_money_pay.grid(row=2, column=1, padx=20)

        # 항목 입력
        self.lbl_category = tk.Label(window, text="항목").grid(row=3, column=0)
        self.ent_category = tk.Entry(window, textvariable=self.category, width=30)
        self.ent_category.grid(row=3, column=1, padx=20)


        # 입력하기
        self.btn_enter = tk.Button(window, text="확인", command=self.enter, fg="blue").grid(row=4, column=2)


        # 결과 표시
        self.lbl_result = tk.Label(window, text="현재금액")
        self.lbl_result.grid(row=5, column=0)
        self.lbl_code = tk.Label(window)
        self.lbl_code.grid(row=5,column=1)


    def enter(self):
        encode_result = enter_encode()
        self.lbl_code["text"] = f"{encode_result}"



def enter_encode(text):
    """입력받은 친구들을 저장"""
    tree.insert("", 'end', values=)
    tree.insert("", 'end', values=[2, "X", "Y", "Z"])
    tree.insert("", 'end', values=[3, "X", "Y", "Z"])




def main():
    window = tk.Tk()
    window.resizable(width=False, height=False)
    MoneyManage(window)
    window.mainloop()

if __name__ == "__main__":
    main()
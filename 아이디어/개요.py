from tkinter import simpledialog
import tkinter as tk
from tkinter import ttk
import csv

class MoneyManage:
    # 1. __init__
    def __init__(self, window):
        window.title("가계부")

    # 2. 이름에 따라 csv 파일 열리거나 생성되는 함수
    def gui_input(self,text: str) -> str:
        return simpledialog.askstring(title="이름입력", prompt=text)

    def user_check(self):
        pass
    ######### 확인 누르면 모든 게 다 들어갈 수 있게 하는 게 더 좋은 것 같기도...
    #############################################################
    # 3. 날짜 삽입 함수
    def insert_date(self):
        pass
    # 4. 수입 삽입 함수
    def insert_income(self):
        pass
    # 5. 지출 삽입 함수
    def insert_outcome(self):
        pass
    # 6. 항목 삽입 함수
    def insert_category(self):
        pass
    ###############################################################
    # 확인 한 번만 누르기
    def insert_value(self):
        pass
    ###############################################################
    # 7. 현재 금액 계산 함수
    def sum_total(self):
        pass
    # 8. 현재 금액 삽입 함수
    def insert_total(self):
        pass
    # 9. 저장 함수
    def save_csv(self):
        pass
    pass

def main():
    pass

if __name__ == '__main__':
    main()

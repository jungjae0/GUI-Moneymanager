import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()


def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)


def main():
    input_text = gui_input("이름은?")
    print(input_text)
    if input_text == "정재영":
        input_text = gui_input("나이는?")
        print(input_text)
    else:
        print("접근할 수 없습니다.")

if __name__ == "__main__":
    main()

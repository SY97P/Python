'''
체크 버튼 연습

체크버튼 : 켜고 끄는데 사용하는 위젯

'''

from tkinter import *
from tkinter import messagebox

def myfunc() :
    if chk == 0 :
        messagebox.showinfo("", "체크버튼이 꺼졌어요")
    else :
        messagebox.showinfo("", "체크버튼이 켜졌어요")

def main() :
    window = Tk()

    chk = IntVar()
    cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command = myfunc)

    cb1.pack()

    window.mainloop()



main()

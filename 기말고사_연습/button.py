'''
버튼 연습

버튼 : 마우스로 클릭하면 눌리는 효과와 함께 지정한 작업 실행

'''
from tkinter import *
from tkinter import messagebox

def myfunc() :
    messagebox.showinfo("강아지버튼", "강아지가 귀엽죠?")
    
def main() :
    window = Tk()

    button1 = Button(window, text="파이썬 종료", fg = "red", command = quit)

    button1.pack()

    button2 = Button(window, text="강아지 메시지", fg = "blue", command = myfunc)

    button2.pack()

    window.mainloop()


main()

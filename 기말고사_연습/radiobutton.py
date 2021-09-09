'''
라디오버튼 연습


라디오버튼 : 여러개 중에서 하나를 선택하는 데 사용하는 위젯


'''

from tkinter import *

def myfunc() :
    if var.get() == 1 :
        label1.configure(text="파이썬")
    elif var.get() == 2 :
        label1.configure(text="씨")
    else :
        label1.configure(text="Java")
    
def main() :
    window = Tk()

    var = IntVar()

    rb1 = Radiobutton(window, text="파이썬", variable = var, value = 1, command = myfunc)
    rb2 = Radiobutton(window, text="c++", variable=var, value=2, command = myfunc)
    rb3 = Radiobutton(window, text="자바", variable=var, value=3, command=myfunc)

    label1 = Label(window, text="선택한 언어", fg="red")
    
    rb1.pack()
    rb2.pack()
    rb3.pack()
    label1.pack()

    window.mainloop()




main()

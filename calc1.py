import tkinter
import tkinter.messagebox
top=tkinter.Tk()
def helloCallBack():
    tkMessageBox.showinfo("Hello Python","Hello world")
B=tkinter.Button(top,text="hello",commend=helloCallBack)   
B.pack()
top.mainloop()

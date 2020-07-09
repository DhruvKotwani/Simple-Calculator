from tkinter import *
from tkinter.messagebox import *
def clicked(event):
    b=event.widget
    text=b["text"]
    textfield.insert(END,text)

def equal():
    try:
        expression=textfield.get()
        answer=eval(expression)
        textfield.delete(0,END)
        textfield.insert(0,answer)
    except Exception as e:
        showerror("ERROR",e)


def allclear():
    textfield.delete(0,END)

def clear():
    exp=textfield.get()
    exp=exp[0:len(exp)-1]
    textfield.delete(0,END)
    textfield.insert(0,exp)

window=Tk()
window.title("MY CALCULATOR")
window.geometry("350x310")
title=Label(window,text="MY CALCULATOR")
title.pack(side="top")
textfield=Entry(window,justify="center",width=30,bg="grey",fg="white")
textfield.pack(padx=10,pady=20,fill=X)
buttonframe=Frame(window)
buttonframe.pack()
temp=1
for i in range(0,3):
    for j in range(0,3):
        button=Button(buttonframe,text=temp,width=10,height=2,activeforeground="white",activebackground="orange",relief="solid")
        temp=temp+1
        button.grid(row=i,column=j,padx=3,pady=2)
        button.bind("<Button-1>",clicked)


zerobutton=Button(buttonframe,text="0",width=10,height=2,activeforeground="white",activebackground="orange",relief="solid")
zerobutton.grid(row=3,column=0,padx=3,pady=2)
zerobutton.bind("<Button-1>",clicked)
dotbutton=Button(buttonframe,text=".",width=10,height=2,activeforeground="white",activebackground="orange",relief="solid")
dotbutton.grid(row=3,column=1,padx=3,pady=2)
dotbutton.bind("<Button-1>",clicked)
equalbutton=Button(buttonframe,text="=",width=10,height=2,activeforeground="white",activebackground="orange",relief="solid",command=equal)
equalbutton.grid(row=3,column=2,padx=3,pady=2)
dividebutton=Button(buttonframe,text="/",width=10,height=2,activeforeground="white",activebackground="orange",relief="solid")
dividebutton.grid(row=0,column=3)
dividebutton.bind("<Button-1>",clicked)
multiplybutton=Button(buttonframe,text="*",width=10,height=2,activeforeground="white",activebackground="orange",relief="solid")
multiplybutton.grid(row=1,column=3)
multiplybutton.bind("<Button-1>",clicked)
subtractbutton=Button(buttonframe,text="-",width=10,height=2,activeforeground="white",activebackground="orange",relief="solid")
subtractbutton.grid(row=2,column=3)
subtractbutton.bind("<Button-1>",clicked)
addbutton=Button(buttonframe,text="+",width=10,height=2,activeforeground="white",activebackground="orange",relief="solid")
addbutton.grid(row=3,column=3)
addbutton.bind("<Button-1>",clicked)
clearbutton=Button(buttonframe,text="<--",width=22,height=2,activeforeground="white",activebackground="orange",relief="solid",command=clear)
clearbutton.grid(row=4,column=0,columnspan=2)
allclearbutton=Button(buttonframe,text="AC",width=22,height=2,activeforeground="white",activebackground="orange",relief="solid",command=allclear)
allclearbutton.grid(row=4,column=2,columnspan=2)

window.mainloop()

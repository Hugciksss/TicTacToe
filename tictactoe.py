from tkinter import*
from tkinter import messagebox
mansLogs=Tk()
mansLogs.title('TicTacToe')

speletajsX=True
count=0
def btnClick(button):#padod visu pogu
    global speletajsX,count#kādi main\igie tiks izmantoti visā programmā
    if button["text"]==""and speletajsX==True:#spēlē spēlētājs x
        button["text"]="X"#maina uz x
        speletajsX=False
        count+=1




btn1=Button(mansLogs,text='',width=6,height=3,bd=10,font=('Black'),bg= 'red')
btn2=Button(mansLogs,text='',width=6,height=3,bd=10,font=('Black'),bg= 'red')
btn3=Button(mansLogs,text='',width=6,height=3,bd=10,font=('Black'),bg= 'red')
btn4=Button(mansLogs,text='',width=6,height=3,bd=10,font=('Black'),bg= 'red')
btn5=Button(mansLogs,text='',width=6,height=3,bd=10,font=('Black'),bg= 'red')
btn6=Button(mansLogs,text='',width=6,height=3,bd=10,font=('Black'),bg= 'red')
btn7=Button(mansLogs,text='',width=6,height=3,bd=10,font=('Black'),bg= 'red')
btn8=Button(mansLogs,text='',width=6,height=3,bd=10,font=('Black'),bg= 'red')
btn9=Button(mansLogs,text='',width=6,height=3,bd=10,font=('Black'),bg= 'red')

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=3,column=0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)







mansLogs.mainloop()
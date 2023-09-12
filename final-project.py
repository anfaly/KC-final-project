import tkinter
from tkinter import *
from tkinter import messagebox


gamewindow = Tk()
gamewindow.title("لعبه الاكس اوه")
gamewindow.geometry("855x800+400+400")
gamewindow.configure(background="gold")

topfram = Frame(gamewindow, height=380, bg="brown", bd=15, pady=2, width=790, relief=RIDGE)
topfram.grid(row=0, column=0)

downframe= Frame(gamewindow, bg="blue", bd=10, width=790, height=150, relief=RIDGE)
downframe.grid(row=1, column=0)

buttomframe= Frame(gamewindow, bg="pink", bd=10, width=790, height=130, relief=RIDGE)
buttomframe.grid(row=2, column=0)

playerx= IntVar()
playero= IntVar()

playerx.set(0)
playero.set(0)

buttons= StringVar()
click = True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "x"
        click = False
        scorekeeper()

    elif buttons["text"] == " " and click == False:
        buttons["text"] = "o"
        click = True
        scorekeeper()


def colorreturn():
    button1.configure(fg="black")
    button2.configure(fg="black")
    button3.configure(fg="black")
    button4.configure(fg="black")
    button5.configure(fg="black")
    button6.configure(fg="black")
    button7.configure(fg="black")
    button8.configure(fg="black")
    button9.configure(fg="black")


def scorekeeper():
    if(button1["text"]=="x" and button2["text"]=="x" and button3["text"]=="x"):
        button1.configure(fg="green")
        button2.configure(fg="green")
        button3.configure(fg="green")
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("الفائز هو اكس", "لقد ربحت اللعبه اكس")

    elif(button4["text"]=="x" and button5["text"]=="x" and button6["text"]=="x"):
        button4.configure(fg="green")
        button5.configure(fg="green")
        button6.configure(fg="green")
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("الفائز هو اكس", "لقد ربحت اللعبه اكس")
    elif (button7["text"]=="x" and button8["text"]=="x" and button9["text"]=="x"):
        button7.configure(fg="green")
        button8.configure(fg="green")
        button9.configure(fg="green")
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("الفائز هو اكس", "لقد ربحت اللعبه اكس")
    elif (button1["text"] == "x" and button4["text"] == "x" and button7["text"] == "x"):
        button1.configure(fg="green")
        button4.configure(fg="green")
        button7.configure(fg="green")
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("الفائز هو اكس", "لقد ربحت اللعبه اكس")
    elif (button2["text"]=="x" and button5["text"]=="x" and button8["text"]=="x"):
        button2.configure(fg="green")
        button5.configure(fg="green")
        button8.configure(fg="green")
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("الفائز هو اكس", "لقد ربحت اللعبه اكس")
    elif (button3["text"]=="x" and button6["text"]=="x" and button9["text"]=="x"):
        button3.configure(fg="green")
        button6.configure(fg="green")
        button9.configure(fg="green")
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("الفائز هو اكس", "لقد ربحت اللعبه اكس")
    elif (button1["text"]=="x" and button5["text"]=="x" and button9["text"]=="x"):
        button1.configure(fg="green")
        button5.configure(fg="green")
        button9.configure(fg="green")
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("الفائز هو اكس", "لقد ربحت اللعبه اكس")
    elif (button3["text"] == "x" and button5["text"] == "x" and button7["text"] == "x"):
        button3.configure(fg="green")
        button5.configure(fg="green")
        button7.configure(fg="green")
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo("الفائز هو اكس", "لقد ربحت اللعبه اكس ")
    elif (button1["text"] == "o" and button2["text"] == "o" and button3["text"] == "o"):
        button1.configure(fg="green")
        button2.configure(fg="green")
        button3.configure(fg="green")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("الفائز هو اوه", "لقد ربحت اللعبه اوه")

    elif (button4["text"] == "o" and button5["text"] == "o" and button6["text"] == "o"):
        button4.configure(fg="green")
        button5.configure(fg="green")
        button6.configure(fg="green")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("الفائز هر اوه", "لقد ربحت اللعبه اوه")
    elif (button7["text"] == "o" and button8["text"] == "o" and button9["text"] == "o"):
        button7.configure(fg="green")
        button8.configure(fg="green")
        button9.configure(fg="green")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("الفائز هر اوه", "لقد ربحت اللعبه اوه")
    elif (button1["text"] == "o" and button4["text"] == "o" and button7["text"] == "o"):
        button1.configure(fg="green")
        button4.configure(fg="green")
        button7.configure(fg="green")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("الفائز هر اوه", "لقد ربحت اللعبه اوه")
    elif (button2["text"] == "o" and button5["text"] == "o" and button8["text"] == "o"):
        button2.configure(fg="green")
        button5.configure(fg="green")
        button8.configure(fg="green")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("الفائز هو اوه", "لقد ربحت اللعبه اوه")
    elif (button3["text"] == "o" and button6["text"] == "o" and button9["text"] == "o"):
        button3.configure(fg="green")
        button6.configure(fg="green")
        button9.configure(fg="green")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("الفائز هو اوه", "لقد ربحت اللعبه اوه")
    elif (button1["text"] == "o" and button5["text"] == "o" and button9["text"] == "o"):
        button1.configure(fg="green")
        button5.configure(fg="green")
        button9.configure(fg="green")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("الفائز هو اوه", "لقد ربحت اللعبه اوه")
    elif (button3["text"] == "o" and button5["text"] == "o" and button7["text"] == "o"):
        button3.configure(fg="green")
        button5.configure(fg="green")
        button7.configure(fg="green")
        n = float(playero.get())
        score = (n + 1)
        playero.set(score)
        tkinter.messagebox.showinfo("الفائز هو اوه", "لقد ربحت اللعبه اوه")

def reset():
    colorreturn()
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(background="white")
    button2.configure(background="white")
    button3.configure(background="white")
    button4.configure(background="white")
    button5.configure(background="white")
    button6.configure(background="white")
    button7.configure(background="white")
    button8.configure(background="white")
    button9.configure(background="white")


def newgame():
    reset()
    playerx.set(0)
    playero.set(0)


button1 = Button(topfram, text = " ", font=("Times 24 bold"), height= 3, width= 6, bg="white", command=lambda :checker(button1))
button1.grid(row=1, column=0, sticky= S+N+E+W)

button2 = Button(topfram, text = " ", font=("Times 24 bold"), height= 3, width= 6, bg="white", command=lambda :checker(button2))
button2.grid(row=1, column=1, sticky= S+N+E+W)

button3 = Button(topfram, text = " ", font=("Times 24 bold"), height= 3, width= 6, bg="white", command=lambda :checker(button3))
button3.grid(row=1, column=2, sticky= S+N+E+W)

button4 = Button(topfram, text = " ", font=("Times 24 bold"), height= 3, width= 6, bg="white", command=lambda :checker(button4))
button4.grid(row=2, column=0, sticky= S+N+E+W)

button5 = Button(topfram, text = " ", font=("Times 24 bold"), height= 3, width= 6, bg="white", command=lambda :checker(button5))
button5.grid(row=2, column=1, sticky= S+N+E+W)

button6 = Button(topfram, text = " ", font=("Times 24 bold"), height= 3, width= 6, bg="white", command=lambda :checker(button6))
button6.grid(row=2, column=2, sticky= S+N+E+W)

button7 = Button(topfram, text = " ", font=("Times 24 bold"), height= 3, width= 6, bg="white", command=lambda :checker(button7))
button7.grid(row=3, column=0, sticky= S+N+E+W)

button8 = Button(topfram, text = " ", font=("Times 24 bold"), height= 3, width= 6, bg="white", command=lambda :checker(button8))
button8.grid(row=3, column=1, sticky= S+N+E+W)

button9 = Button(topfram, text = " ", font=("Times 24 bold"), height= 3, width= 6, bg="white", command=lambda :checker(button9))
button9.grid(row=3, column=2, sticky= S+N+E+W)

playerxresult = Label(downframe, font=("arial", 37, "bold"), text="عدد مرات الفوز للاعب اكس", pady=2, padx=2, bg="silver")
playerxresult.grid(row=0, column=1, sticky=E)
resultx = Entry(downframe, font=("arial", 36, "bold"),fg="green", bd=2, width=10, justify=CENTER, textvariable=playerx)
resultx.grid(row=0, column=0)

playeroresult = Label(downframe, font=("arial", 38, "bold"), text="عدد مرات الفوز للاعب  اوه", pady=2, padx=2, bg="silver")
playeroresult.grid(row=1, column=1, sticky=E)
resulto = Entry(downframe, font=("arial", 36, "bold"), fg="green", bd=2, width=10, justify=CENTER, textvariable=playero)
resulto.grid(row=1, column=0)


resetbutton = Button(buttomframe, text="اعاده اللعبه", command=reset, width=17, height=3, fg="black", bg="silver", font=
("Times 24 bold"))

resetbutton.grid(row=0, column=2)

newgamebutton = Button(buttomframe, text="بدء لعبه جديده", command=newgame, width=17, fg="green", height=3, bg="silver"
, font=("Times 24 bold"))


newgamebutton.grid(row=0, column=3)

quitbutton = Button(buttomframe, text="خروج", command=lambda :quit(gamewindow),width=17, height=3, fg="red", bg="silver"
                    , font=("Times 24 bold"))

quitbutton.grid(row=0, column=0)

pausebutton = Button(buttomframe, text="أعلى النتائج", width=17, height=3, bg="silver", fg="blue",
                      font=("Times 24 bold"))

pausebutton.grid(row=0, column=1)


gamewindow.mainloop()
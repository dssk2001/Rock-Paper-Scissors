import random
import tkinter as tk


window = tk.Tk()
window.geometry("300x300")
window.title("Rock Scissor Paper")


ui=""
ci=""
usc = 0
csc = 0

def rcc():
    return random.choice(['Rock','Paper','Scissor'])

def choice_to_number(choice):
    rps={'Scissor':0,'Paper':1,'Rock':2}
    return rps[choice]


def result(hc,cc):
    global usc
    global csc
    user = choice_to_number(hc)
    comp = choice_to_number(cc)
    if (user == comp):
        print("Tie")
    elif ((user - comp) % 3 == 2):
        print("You win")
        usc += 1
    else:
        print("Comp wins")
        csc += 1

    # Text
    text_area = tk.Text(master=window, height=12, width=30)
    text_area.grid(column=60, row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c}".format(
        uc=ui, cc=ci, u=usc, c=csc, font=('arial', 24, 'bold'))
    text_area.insert(tk.END, answer)


def rock():
    global ui
    global ci
    ui = 'Rock'
    ci = rcc()
    result(ui,ci)

def paper():
    global ui
    global ci
    ui = 'Paper'
    ci = rcc()
    result(ui,ci)

def scissor():
    global ui
    global ci
    ui = 'Scissor'
    ci = rcc()
    result(ui,ci)

button1=tk.Button(text="       Scissor         ",bg="blue",command=scissor, height=1,width=8,font=('calibri',15,'bold'))
button1.grid(column=60,row=1)
button2=tk.Button(text="        Paper          ",bg="pink",command=paper, height=1,width=8,font=('calibri',15,'bold'))
button2.grid(column=60,row=2)
button3=tk.Button(text="         Rock          ",bg="yellow",command=rock, height=1,width=8,font=('calibri',15,'bold'))
button3.grid(column=60,row=3)

window.mainloop()

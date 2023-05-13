
from tkinter import  N, TOP, W, Y, Button, Frame, Pack, StringVar, Tk, Toplevel, messagebox
import tkinter as tk
import sys
import math as s
from tracemalloc import stop
from math import *

###SEKCJA USTAWIENIA OKNA


root = Tk()
root.title('Kalkulator')

root.configure(background = "grey")
root.configure(bd=0, bg="grey",borderwidth=5, relief="solid")
root.geometry("508x465+700+150")




def wyjscie():
    pytanie = messagebox.askyesno(title = "Wyjście z programu", message = "Czy chcesz zakończyć pracę?")
    if pytanie:
        sys.exit()

variable = tk.StringVar();
label = tk.Label(root, textvariable = variable,foreground="black",background="grey",height=5,font="BOLD",activebackground="white",borderwidth=3, relief="solid",width=54).grid(columnspan=8,row=1)

variable.set("")
ans=str()

###SEKCJA FUNKCJI

def liczba0():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(0))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(0))
        variable.set(x)
def liczba1():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(1))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(1))
        variable.set(x)

def liczba2():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(2))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(2))
        variable.set(x)
def liczba3():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(3))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(3))
        variable.set(x)
def liczba4():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(4))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(4))
        variable.set(x)
def liczba5():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(5))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(5))
        variable.set(x)
def liczba6():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(6))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(6))
        variable.set(x)
def liczba7():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(7))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(7))
        variable.set(x)
def liczba8():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(8))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(8))
        variable.set(x)
def liczba9():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(9))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(9))
        variable.set(x)
def przecinek1():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(","))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(","))
        variable.set(x)
def plus():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str("+"))
        variable.set(x)
    else:
        x=str(str(variable.get())+str("+"))
        variable.set(x)
def minus():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str("-"))
        variable.set(x)
    else:
        x=str(str(variable.get())+str("-"))
        variable.set(x)
def wyczysc():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
    else:
        x=x[0:(len(x)-1)]
        variable.set(x)
def wyczysc1():
    variable.set("")
def wynik():
    global ans
    x=str(str(variable.get()))
    ###SEKCJA ZAMIANY ODPOWIEDNICH SYMBOLI 
    x=x.replace("²","**2")
    x=x.replace("³","**3")
    x=x.replace("ᶺ","**")
    x=x.replace("x","*")
    x=x.replace(",",".")
    try:
        eval(x)
    except SyntaxError:
        variable.set("Syntax Error")
    except :
        variable.set("Math Error")
    variable.set(eval(x))
    ans=str(str(variable.get()))
    
    
def pierwiastek():
    global ans
    x=str(str(variable.get()))
    try:
        eval(x)
    except SyntaxError:
        variable.set("Syntax Error")
    except :
        variable.set("Math Error")
    variable.set(sqrt(eval(x)))
    ans=str(str(variable.get()))
def mnozenie():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str("x"))
        variable.set(x)
    else:
        x=str(str(variable.get())+str("x"))
        variable.set(x)
def dzielenie():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str("/"))
        variable.set(x)
    else:
        x=str(str(variable.get())+str("/"))
        variable.set(x)
def potega2():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str("²"))
        variable.set(x)
    else:
        x=str(str(variable.get())+str("²"))
        variable.set(x)
def potega3():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str("³"))
        variable.set(x)
    else:
        x=str(str(variable.get())+str("³"))
        variable.set(x)
def notacja():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str("* 10ᶺ"))
        variable.set(x)
    else:
        x=str(str(variable.get())+str("* 10ᶺ"))
        variable.set(x)
     
def nawiasprzod():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str("("))
        variable.set(x)
    else:
        x=str(str(variable.get())+str("("))
        variable.set(x)
def nawiastyl():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str(")"))
        variable.set(x)
    else:
        x=str(str(variable.get())+str(")"))
        variable.set(x) 
def dowolnapotega():
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
        x=str(str(variable.get())+str("ᶺ"))
        variable.set(x)
    else:
        x=str(str(variable.get())+str("ᶺ"))
        variable.set(x) 
def last():
    global ans
    x=str(str(variable.get()))
    if x==("Syntax Error") or x==("Math Error"):
        variable.set("")
    
        variable.set(ans)
    else:
        
        variable.set(x+ans) 

    
    
    
####SEKCJA WYGLADU



liczba_0 = Button(root, text="0", width=5, command=liczba0,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
liczba_0.grid (column=2, row=6)

liczba_1 = Button(root, text="1", width=5, command=liczba1,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
liczba_1.grid (column=1, row=3)

liczba_2 = Button(root, text="2", width=5, command=liczba2,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
liczba_2.grid (column=2, row=3)

liczba_3 = Button(root, text="3", width=5, command=liczba3,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
liczba_3.grid (column=3, row=3)

liczba_4 = Button(root, text="4", width=5, command=liczba4,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
liczba_4.grid (column=1, row=4)

liczba_5 = Button(root, text="5", width=5, command=liczba5,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
liczba_5.grid (column=2, row=4)

liczba_6 = Button(root, text="6", width=5, command=liczba6,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
liczba_6.grid (column=3, row=4)

liczba_7 = Button(root, text="7", width=5, command=liczba7,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
liczba_7.grid (column=1, row=5)

liczba_8 = Button(root, text="8", width=5, command=liczba8,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
liczba_8.grid (column=2, row=5)

liczba_9 = Button(root, text="9", width=5, command=liczba9,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
liczba_9.grid (column=3, row=5)

x = Button(root, text="*", width=5, command=mnozenie,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
x.grid (column=4, row=3)

odejmowanie = Button(root, text="-", width=5, command=minus,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
odejmowanie.grid (column=4, row=4)

dodawanie = Button(root, text="+", width=5, command=plus,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
dodawanie.grid (column=4, row=5)

koniec_dzialania = Button(root, text="=", width=5, command=wynik,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
koniec_dzialania.grid (column=7, row=6)

przecinek = Button(root, text=",", width=5, command=przecinek1,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
przecinek.grid (column=3, row=6)

nieaktywne = Button(root, text="Cls", width=5, command=wyczysc1,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
nieaktywne.grid (column=4, row=6)

pierwiastkowanie = Button(root, text="√", width=5, command=pierwiastek,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
pierwiastkowanie.grid (column=5, row=4)

dzieleniee = Button(root, text="/", width=5, command=dzielenie,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
dzieleniee.grid (column=5, row=3)

mnozeniee = Button(root, text="Cofnij", width=5, command=wyczysc,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
mnozeniee.grid (column=5, row=6)

potegowanie22 = Button(root, text="x²", width=5, command=potega2,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
potegowanie22.grid (column=6, row=3)

potegowanie33 = Button(root, text="x³", width=5, command=potega3,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
potegowanie33.grid (column=6, row=4)

notacjaa = Button(root, text="Not.", width=5, command=notacja,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
notacjaa.grid (column=1, row=6)

nawiasp = Button(root, text="(", width=5, command=nawiasprzod,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
nawiasp.grid (column=5, row=5)

nawiast = Button(root, text=")", width=5, command=nawiastyl,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
nawiast.grid (column=6, row=5)

potega = Button(root, text="ᶺ", width=5, command=dowolnapotega,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
potega.grid (column=7, row=3)

Ans = Button(root, text="Ans", width=5, command=last,background="grey",foreground="black",height=3,font=("Times New Roman", 15),borderwidth=5)
Ans.grid (column=6, row=6)









    

root.mainloop()
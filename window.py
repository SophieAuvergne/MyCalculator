#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.font as tkFont # ou «import TkFont» pour python 2
from calc import *
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cypher_suite = Fernet(key)
cypher_text = cypher_suite.encrypt(b"Develop by Sophie")


window = Tk()
global number
global bool

bool = False #bool détermine si on doit efface l'écran avant d'ajouter un nb ou pas
number = ''
list = []

helv36 = tkFont.Font(family='Helvetica', size=36)
label = Label(text='', width=25, height=3, font=helv36, background="whiteSmoke")
label.grid(row=0, column=1, columnspan=6)
button_clear = Button(window, text='Clear', borderwidth =5, width = 39, height = 6, background='SteelBlue', command= lambda x=1:clear()).grid(row=1, column=1, columnspan=3)
button_div = Button(window, text='/', borderwidth =5, width = 10, height = 6, background='AliceBlue', command= lambda x=" / ":printNumber(x)).grid(row=1, column=4)
button_exp = Button(window, text="exp()", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" exp ":printNumber(x)).grid(row=1, column=5)
button_ln = Button(window, text="ln()", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" ln ":printNumber(x)).grid(row=1, column=6)

button_one = Button(window, text='1', borderwidth =5, width = 10, height = 6, background='LightSteelBlue', command= lambda x=1:printNumber(str(x))).grid(row=2, column=1)
button_two = Button(window, text='2', borderwidth =5, width = 10, height = 6, background='LightSteelBlue', command= lambda x=2:printNumber(str(x))).grid(row=2, column=2)
button_three = Button(window, text="3", borderwidth = 5 , width = 10, height = 6, background='LightSteelBlue', command= lambda x=3:printNumber(str(x))).grid(row=2, column=3)
button_mult = Button(window, text="x", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" x ":printNumber(x)).grid(row=2, column=4)
button_cos = Button(window, text="cos()", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" cos ":printNumber(x)).grid(row=2, column=5)
button_log = Button(window, text="log()", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" log ":printNumber(x)).grid(row=2, column=6)

button_for = Button(window, text='4', borderwidth = 5, width = 10, height = 6, background='LightSteelBlue', command= lambda x=4:printNumber(str(x))).grid(row=3, column=1)
button_five = Button(window, text='5', borderwidth = 5, width = 10, height = 6, background='LightSteelBlue', command= lambda x=5:printNumber(str(x))).grid(row=3, column=2)
button_six = Button(window, text="6", borderwidth = 5, width = 10, height = 6, background='LightSteelBlue', command= lambda x=6:printNumber(str(x))).grid(row=3, column=3)
button_sub = Button(window, text="-", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" - ":printNumber(x)).grid(row=3, column=4)
button_sin = Button(window, text="sin()", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" sin ":printNumber(x)).grid(row=3, column=5)
button_pow = Button(window, text="x**y", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" ** ":printNumber(x)).grid(row=3, column=6)

button_seven = Button(window, text='7', borderwidth = 5, width = 10, height = 6, background='LightSteelBlue', command= lambda x=7:printNumber(str(x))).grid(row=4, column=1)
button_eight = Button(window, text='8', borderwidth = 5, width = 10, height = 6, background='LightSteelBlue', command= lambda x=8:printNumber(str(x))).grid(row=4, column=2)
button_nine = Button(window, text="9", borderwidth = 5, width = 10, height = 6, background='LightSteelBlue', command= lambda x=9:printNumber(str(x))).grid(row=4, column=3)
button_plus = Button(window, text="+", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" + ":printNumber(x)).grid(row=4, column=4)
button_tan = Button(window, text="tan()", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" tan ":printNumber(x)).grid(row=4, column=5)
button_sqrt = Button(window, text="sqrt", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" sqrt ":printNumber(x)).grid(row=3, column=6)
button_mod = Button(window, text="%", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" % ":printNumber(x)).grid(row=4, column=6)

button_signe = Button(window, text='-', borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=" -":printNumber(x)).grid(row=5, column=1)
button_zero = Button(window, text='0', borderwidth = 5, width = 10, height = 6, background='LightSteelBlue', command= lambda x=0:printNumber(str(x))).grid(row=5, column=2)
button_point = Button(window, text=",", borderwidth = 5, width = 10, height = 6, background='AliceBlue', command= lambda x=".":printNumber(x)).grid(row=5, column=3)
button_egal = Button(window, text="=", borderwidth = 5, width = 39, height = 6, background='SteelBlue', command= lambda x="=":calcul(number)).grid(row=5, column=4, columnspan=6)

Label(text=cypher_text, width=86, height=3, background="whiteSmoke").grid(row=6, column=1, columnspan=6)

def printNumber(txt):
    global number
    global bool
    if bool == True:
        number = ''
        bool = False
    number = number + txt
    label.configure(text=number)

def clear():
    global bool
    bool = True
    txt = ''
    printNumber(txt)

def calcul(number):
    global bool
    indice = 0
    list = number.split(' ')
    number = ''
    for part in enumerate(list):
        test = Calc(list[indice-1], list[indice+1])
        if list[indice] == '+':
            result = test.add(list[indice-1], list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == '-':
            result = test.less(list[indice-1], list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == 'x':
            result = test.mult(list[indice-1], list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == '/':
            if list[indice+1] == "0":
                result = "Impossible : division par 0"
            else:
                result = test.div(list[indice-1], list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == 'cos':
            result = test.cosi(list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == 'sin':
            result = test.sinu(list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == 'tan':
            result = test.tang(list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == 'exp':
            result = test.expo(list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == 'log':
            result = test.loga(list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == '**':
            result = test.powa(list[indice-1], list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == '%':
            result = test.modu(list[indice-1], list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == 'sqrt':
            result = test.my_sqrt(list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        elif list[indice] == 'ln':
            result = test.logn(list[indice+1])
            list[indice+1] = result
            bool = True
            printNumber(str(result))
        indice += 1

window.mainloop()

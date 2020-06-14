import os
from playsound import playsound
from tkinter import *
from tkinter import messagebox
from time import sleep

window = Tk()

window['bg'] = "Black"
window.geometry("450x350+500+50")
window.resizable(False, False)
window.title("Encoding Morse")

#DICT COM TODAS AS LETRAS E NUMEROS DA VIDA REAL EM CODIGO MORSE
morse_code = {"A": ".-", "B": "-.", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."}

def encoding():
    word_raw = entryword.get()
    word = word_raw.upper()

    #DEFINE A VARIAVEL ERROR COM VALOR FALSE
    error = False

    #TRANSFORMA A PALAVRA EM UMA LISTA
    wordlist = list(word)

    #CONTADOR
    i = 0
    o = 0

    #LISTA COM AS LETRAS
    letras = []

    #LACO FOR COM RANGE NO COMPRIMENTO DA LISTA WORDLIST
    for encrypt in range(len(wordlist)):
        try:
            letras.append(morse_code[wordlist[i]])
            letras.append(" ")
            i+=1
        except:
            #EXCESSOES DE CARACTERES
            if wordlist[i] == " ":
                letras.append(" /  ")
                i+=1
            elif wordlist[i] == ",":
                letras.append(",")
                i+=1
            elif wordlist[i] == ".":
                letras.append(".")
                i+=1
            elif wordlist[i] == "!":
                letras.append("!")
                i+=1
            elif wordlist[i] == "?":
                letras.append("?")
                i+=1
            elif wordlist[i] == "@":
                letras.append("@")
                i+=1
            elif wordlist[i] == "#":
                letras.append("#")
                i+=1
            elif wordlist[i] == "$":
                letras.append("$")
                i+=1
            elif wordlist[i] == "%":
                letras.append("%")
                i+=1
            elif wordlist[i] == "&":
                letras.append("&")
                i+=1
            elif wordlist[i] == "*":
                letras.append("*")
                i+=1
            elif wordlist[i] == "=":
                letras.append("=")
                i+=1
            elif wordlist[i] == "+":
                letras.append("+")
                i+=1
            elif wordlist[i] == "ç":
                letras.append("ç")
                i+=1
            else:
                messagebox.showerror("Erro", "Você não pode utilizar acentos")
                error = True
                break
    if error == True:
        pass
    else:
        entryword.delete(0, END)
        wordcriptografed = "".join(letras)
        textresult['state'] = NORMAL
        textresult.delete(1.0, END)
        if word_raw == "":
            pass
        else:
            textresult.insert(END, str(word_raw)+" em código morse: \n")
            textresult.insert(END, str(wordcriptografed))
            wordcriptografedlist = list(wordcriptografed)
            for listar in range(len(wordcriptografedlist)):
                caracter = wordcriptografedlist[o]
                if caracter == ".":
                    playsound("sounds/bip curto.mp3")
                    sleep(0.15)
                    o+=1
                elif caracter == "-":
                    playsound("sounds/bip longo.mp3")
                    sleep(0.15)
                    o+=1
                elif caracter == "/":
                    sleep(0.25)
                    o+=1
                else:
                    o+=1

#WIDGETS
title = Label(window, text="Codificador Código Morse", fg="#FFFFFF", bg="Black", font="Menlo 20")
title.pack(side=TOP, pady=5, padx=12)

text1 = Label(window, text="Escreva algo (sem acentos):", fg="#FFFFFF", bg="Black", font="Menlo 16")
text1.pack(side=TOP)

entryword = Entry(window, bg="gray12", fg="#FFFFFF", font="Menlo 12", width=400)
entryword.pack(side=TOP, padx=12, pady=12)

botao = Button(window, bg="gray12", fg="#FFFFFF", font="Menlo 16", width=400, text="Codificar", command=encoding)
botao.pack(side=TOP, padx=12)

textresult = Text(window, bg="gray12", fg="#FFFFFF", font="Menlo 12", width=400, height=400, state=DISABLED)
textresult.pack(side=TOP, padx=12, pady=12)

window.mainloop()

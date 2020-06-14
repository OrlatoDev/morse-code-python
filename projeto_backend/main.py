import platform
import os
sistemaoperacional = platform.system()
if sistemaoperacional == "Windows":
    os.system("cls")
else:
    os.system("clear")

#ATRIBUINDO O VALOR DO INPUT.UPPER (MAIUSCULO) A VARIAVEL WORD
word = input("Escreva algo: ").upper()

#DICT COM TODAS AS LETRAS E NUMEROS DA VIDA REAL EM CODIGO MORSE
morse_code = {"A": ".-", "B": "-.", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."}

def encoding():
    #VARIAVEL ERRO COM O VALOR FALSE
    error = False

    #TRANSFORMA A PALAVRA EM UMA LISTA
    wordlist = list(word)

    #CONTADOR
    i = 0

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
                letras.append(" / ")
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
                error = True
                print("Você não pode usar acentos, pontos e hifens!")
                break
    if error == True:
        exit
    else:
        print("Código Morse: "+"".join(letras))

encoding()
import tkinter as tk
import random
import os
import sys

## -----------------------------
## -----------------------------

def obter_caminho_icone():
    if getattr(sys, 'frozen', False):
        
        return os.path.join(sys._MEIPASS, 'imagens', 'jdf_icone.ico')
    else:
        
        return 'imagens/jdf_icone.ico'
## -----------------------------
## -----------------------------


## -----------------------------
## Funções

def novo_jogo():
    global palavra, palavra_incompleta, escolhidas, acertos, erros, resposta, label_inc, label_esc, label_aviso, label_2, label_boneco1, label_boneco2, label_boneco3

    resposta = random.choice(palavras_lista).upper()
    palavra = list(resposta)
    palavra_incompleta = ["_"] * len(palavra)
    escolhidas.clear()
    acertos.clear()
    erros.clear()

    label_inc.config(text=" ".join(palavra_incompleta))
    label_esc.config(text="")
    label_aviso.config(text="ESCOLHA UMA LETRA", fg="blue")
    label_2.config(text="Qual a palavra?", fg="green")
    label_boneco1.config(text=" . ", fg="orange")
    label_boneco2.config(text=" ... ", fg="orange")
    label_boneco3.config(text=" . . ", fg="orange")




def verificarLetra(tentativa):
    letra = tentativa
    if len(erros) < 6:
        if letra in palavra:
            adicionarLetra(tentativa)
            if len(acertos) == len(resposta):
                label_boneco3.config(text=" / \ ", fg="green")
                label_boneco2.config(text=" /|\ ", fg="green")
                label_boneco1.config(text=" :D ", fg="green")
                label_2.config(text="VOCÊ GANHOU", fg="green")
        else:
            marcarErro(tentativa)
    elif len(erros) > 5 and len(acertos) < len(resposta):
        label_inc.config(text="ERROU", fg="black")

def adicionarLetra(tentativa):
    label_aviso.config(text="LETRA CORRETA", fg="green")

    if tentativa not in acertos:
        acertos.append(tentativa)

        cont = palavra.count(tentativa)

        if cont > 1:
            for c in range(0, cont-1):
                acertos.append(tentativa)
            
        for i, c in enumerate(palavra):
            if c == tentativa:
                palavra_incompleta[i] = tentativa
    
    palavra_inc = " ".join(palavra_incompleta)
    label_inc.config(text=palavra_inc)

    if tentativa in escolhidas:
        label_aviso.config(text="LETRA REPETIDA CORRETA", fg="orange")
    else:
        letrasEscolhidas(tentativa)
        label_aviso.config(text="LETRA CORRETA", fg="green")

def marcarErro(tentativa):
    if len(acertos) >= len(resposta):
        ok = "ok"
        
    else:
        if tentativa in escolhidas:
            label_aviso.config(text="LETRA REPETIDA ERRADA", fg="orange")
        else:
            letrasEscolhidas(tentativa)
            label_aviso.config(text="LETRA ERRADA", fg="red")
            erros.append(tentativa)

        ## Alterando BONECO COM ERROS

        if len(erros) == 1:
            label_boneco1.config(text=" O ")
        
        elif len(erros) == 2:
            label_boneco2.config(text=" .|. ")
        
        elif len(erros) == 3:
            label_boneco2.config(text=" /|. ")
        
        elif len(erros) == 4:
            label_boneco2.config(text=" /|\ ")
        
        elif len(erros) == 5:
            label_boneco3.config(text=" / . ")
        
        elif len(erros) == 6:
            label_boneco3.config(text=" / \ ", fg="red")
            label_boneco2.config(fg="red")
            label_boneco1.config(text=" X ", fg="red")
            label_2.config(text="VOCÊ PERDEU", fg="red")
            label_inc.config(text="ERROU", fg="black")
        



def letrasEscolhidas(tentativa):

    escolhidas.append(tentativa)
    letras_esc = " ".join(escolhidas)
    label_esc.config(text=letras_esc, fg="blue")


## -----------------------------

ok = "ok"

## -----------------------------
##Palavra Certa Da Forca


palavras_lista = [
    "elefante", "camaleao", "pinguim", "hipopotamo", "tubarao", "borboleta", "jacare",
    "computador", "relogio", "caneta", "cadeira", "abajur", "martelo", "telefone",
    "montanha", "deserto", "floresta", "oceano", "caverna", "vulcao", "ilha",
    "dentista", "bombeiro", "advogado", "arquiteto", "professor", "engenheiro", "jornalista",
    "abacaxi", "melancia", "morango", "cereja", "goiaba", "laranja", "carambola",
    "amarelo", "verde", "azul", "vermelho", "roxo", "lilas", "marrom",
    "liberdade", "coragem", "desafio", "vitoria", "esperanca", "misterio", "segredo",
    "cachorro", "gato", "cavalo", "pato", "leão", "pescador", "sol", "lua", "estrela"
]

resposta = random.choice(palavras_lista).upper()
palavra = list(resposta)
palavra_incompleta = []

for c in range(0, len(palavra)):
    palavra_incompleta.append("_")

##Todas Letras Digitadas
escolhidas = []

##Letras Digitadas Certas
acertos = []

##Letras Digitadas Erradas
erros = []

## -----------------------------

## -----------------------------
## INTERFACE

janela = tk.Tk()
janela.title("JdF - JOGO DA FORCA")
janela.geometry("385x845")
janela.iconbitmap(obter_caminho_icone())
janela.resizable(False, False)

## -----------------------------
## Botão novo jogo

botão_novo = tk.Button(janela, text="JOGAR NOVAMENTE", font=("Agency FB", 10), bg="orange", fg="white", relief="flat", bd=0, padx=5,pady=5, command=novo_jogo)
botão_novo.grid(row=0, column=1, pady=(20, 0))

## -----------------------------

labelTitulo = tk.Label(janela, text="JOGO DA FORCA", font=("Agency FB", 40))
labelTitulo.grid(row=1, column=1)

label_2 = tk.Label(janela, text="Qual a palavra?" , font=("Agency FB", 20), fg="green")
label_2.grid(row=2, column=1)

## -----------------------------
## Colocando a palavra escondida
palavra_inc = " ".join(palavra_incompleta)

label_inc = tk.Label(janela, text=palavra_inc, justify="left", anchor="w", bg="lightgray", font=("Agency FB", 20), fg="black")
label_inc.grid(row=3, column=1)

## -----------------------------
## Aviso de letra certa ou errado

label_aviso = tk.Label(janela, text="ESCOLHA UMA LETRA", font=("Agency FB", 15), fg="blue")
label_aviso.grid(row=4, column=1)

## -----------------------------


## Botões das letras
frame_teclado = tk.Frame(janela)
frame_teclado.grid(row=5, column=0, columnspan=5, pady=20)

alfabeto = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
coluna = 0
linha = 0

for letra in alfabeto:
    botão = tk.Button(frame_teclado, text=letra, width=5, height=2, bg="orange", fg="white", 
    command=lambda l=letra: verificarLetra(l))
    botão.grid(row=linha, column=coluna, padx=5, pady=5)

    coluna += 1
    if coluna > 6: 
        coluna = 0
        linha += 1
    

## -----------------------------
## Mostrar lista de letras escolhidas

letras_esc = " ".join(escolhidas)

label = tk.Label(janela, text="- LETRAS ESCOLHIDAS -", font=("Agency FB", 10), fg="blue")
label.grid(row=6, column=1)

label_esc = tk.Label(janela, text=" - - -", font=("Agency FB", 15), fg="blue")
label_esc.grid(row=7, column=1)

## -----------------------------

label_boneco1 = tk.Label(janela, text=" . ", font=("Century ", 50), fg="orange")
label_boneco1.grid(row=8, column=1)

label_boneco2 = tk.Label(janela, text=" ... ", font=("Century ", 70), fg="orange")
label_boneco2.grid(row=9, column=1)

label_boneco3 = tk.Label(janela, text=" . . ", font=("Century ", 70), fg="orange")
label_boneco3.grid(row=10, column=1)

## -----------------------------

label = tk.Label(janela, text=" python ", font=("Agency FB", 5), fg="black")
label.grid(row=11, column=0)


janela.mainloop()
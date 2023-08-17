from tkinter import *
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename


aux = ''

def retornaCaminho():
    global aux 
    aux = askopenfilename()


janela1 = Tk()
janela1.title("EDIÇÃO DE IMAGEM")
janela1.state('zoomed')
janela1.tk_setPalette(background='white')

menu = Menu(janela1, title='Menu principal', type='normal', tearoff=0, relief='raised')

file = Menu(menu, tearoff=0)
file.add_command(label='Salvar')
file.add_command(label='Salvar como')
file.add_separator()
file.add_command(label='Abrir arquivo')
file.add_command(label='Abrir arquivos recentes')
file.add_separator()
file.add_command(label='Sair', command=janela1.quit)

menu.add_cascade(label='Arquivo', menu=file)

edit = Menu(menu, tearoff=0)
edit.add_command(label='opção1')
edit.add_command(label='opção2')
edit.add_command(label='opção3')
edit.add_command(label='opção4')
edit.add_command(label='opção5')
edit.add_command(label='opção6')

menu.add_cascade(label='Editar', menu=edit)

biblioteca = Menu(menu, tearoff=0)
biblioteca.add_command(label='opção1')
biblioteca.add_command(label='opção2')
biblioteca.add_command(label='opção3')
biblioteca.add_command(label='opção4')
biblioteca.add_command(label='opção5')
biblioteca.add_command(label='opção6')

menu.add_cascade(label='Biblioteca', menu=biblioteca)

view = Menu(menu, tearoff=0)
view.add_command(label='opção1')
view.add_command(label='opção2')
view.add_command(label='opção3')
view.add_command(label='opção4')
view.add_command(label='opção5')
view.add_command(label='opção6')

menu.add_cascade(label = 'Janela', menu = view)

imagem = Menu(menu, tearoff=0)
imagem.add_command(label='opção1')
imagem.add_command(label='opção2')
imagem.add_command(label='opção3')
imagem.add_command(label='opção4')
imagem.add_command(label='opção5')
imagem.add_command(label='opção6')

menu.add_cascade(label = 'Imagem', menu = imagem)

ajuda = Menu(menu, tearoff=0)
ajuda.add_command(label='opção1')
ajuda.add_command(label='opção2')
ajuda.add_command(label='opção3')
ajuda.add_command(label='opção4')
ajuda.add_command(label='opção5')
ajuda.add_command(label='opção6')

menu.add_cascade(label = 'Ajuda', menu = ajuda)

sobre = Menu(menu, tearoff=0)
sobre.add_command(label='opção1')
sobre.add_command(label='opção2')
sobre.add_command(label='opção3')
sobre.add_command(label='opção4')
sobre.add_command(label='opção5')
sobre.add_command(label='opção6')

menu.add_cascade(label = 'Sobre', menu = sobre)

janela1.config(menu=menu)

janela1.iconbitmap('icon.ico')

div1 = Frame(janela1, background='black', width=1000, pady=350)
Grid.grid(div1, row=0, column=0)

texto = Label(div1, text="Escolha a imagem desejada para editá-la", justify='center', padx=350,  background='black', foreground='white')
bt1 = Button(div1, text="Escolher imagem", justify='center', padx=50, background='white', pady=10)

texto.pack()
bt1.pack()

div2 = Frame(janela1, background='white', width=800, height=750)
Grid.grid(div2, row=0, column=1)

texto2 = Label(div2, text="Opções", justify='center', background='grey', foreground='black', width=70, height=50)
texto2.pack()

#-------------------------------------------------------------------------

janela1.mainloop()

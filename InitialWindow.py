from tkinter import *
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
import cv2
import numpy as np

janela1 = Tk()
janela1.title("EDIÇÃO DE IMAGEM")
janela1.state('zoomed')

menu = Menu(janela1, title='Menu principal', type='normal', tearoff=0, relief='raised')

file = Menu(menu, tearoff=0)
file.add_command(label='Salvar')
file.add_command(label='Salvar como')
file.add_separator()
file.add_command(label='Abrir arquivo')
file.add_command(label='Abrir arquivos recentes')
file.add_separator()
file.add_command(label='Sair', command=janela1.quit)

menu.add_cascade(label='File', menu=file)

edit = Menu(menu, tearoff=0)
edit.add_command(label='opção1')
edit.add_command(label='opção2')
edit.add_command(label='opção3')
edit.add_command(label='opção4')
edit.add_command(label='opção5')
edit.add_command(label='opção6')

menu.add_cascade(label='Edit', menu=edit)

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

sobre = Menu(menu, tearoff=0)
sobre.add_command(label='opção1')
sobre.add_command(label='opção2')
sobre.add_command(label='opção3')
sobre.add_command(label='opção4')
sobre.add_command(label='opção5')
sobre.add_command(label='opção6')

menu.add_cascade(label = 'Sobre', menu = sobre)

janela1.config(menu=menu)

#p1 = PhotoImage(file='icon.png')

janela1.iconbitmap('icon.ico')

#janela1.iconphoto(False, p1)

janela1.mainloop()
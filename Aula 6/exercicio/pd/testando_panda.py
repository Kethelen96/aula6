import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter  as tk
from tkinter.filedialog import askopenfilename
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import tkinter.filedialog

# #importando dados de um arquivo excel 
# dados = pd.read_csv('pd/dados.csv')
# print(dados)

# meses = dados['meses']
# print(meses)

# #transformar um arquivo em uma lista
# meses = dados['meses'].to_list()
# valores = dados['valores'].to_list()
# print(meses, valores)

# plt.bar(meses,valores)
# plt.show()

def selecionar():
       caminho = filedialog.askopenfilename(
            title='Selecione o aquivo CSV',
            filetypes=(
                ("CSV files", "*.csv"),
                ("all files", "*.*") )
        )
       return caminho


def data_plot():
    caminho = selecionar()

    if caminho:
        dados = pd.read_csv(caminho)
        meses = dados['meses'].to_list()
        valores = dados['valores'].to_list()
        fig, grafico = plt.subplots()
        grafico.plot(meses,valores)

    
        #tkinter com o pyplot
        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    else:
        print('Erro no processo')


janela = tk.Tk()


btn = tk.Button(janela, text="Plot", command=data_plot)
btn.pack(pady=5)

janela.mainloop()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Tk
from tkinter import filedialog
import tkinter.filedialog
import pandas as pd
import os
import statistics as sta

def ler_arquivo():
    arquivo = filedialog.askopenfilename(
            title='Selecione o aquivo CSV',
            filetypes=(
                ("CSV files", "*.csv"),
                ("all files", "*.*") )
        )
    return arquivo

def data_plot():
    arquivo = ler_arquivo()

    if arquivo:
        dados = pd.read_csv(arquivo)
        vendas = dados['vendas'].to_list()
        vendedor = dados['vendedor'].to_list()
        fig, grafico = plt.subplots()
        grafico.plot(vendedor,vendas)
        
        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    else:
        print('Arquivo não encontrado')

def data_bar():
    arquivo = ler_arquivo()

    if arquivo:
        dados = pd.read_csv(arquivo)
        vendas = dados['vendas'].to_list()
        vendedor = dados['vendedor'].to_list()
        fig, grafico = plt.subplots()
        grafico.bar(vendedor,vendas)
        
        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    else:
        print('Arquivo não encontrado')

def data_pie():
    arquivo = ler_arquivo()

    if arquivo:
        dados = pd.read_csv(arquivo)
        vendas = dados['vendas'].to_list()
        vendedor = dados['vendedor'].to_list()
        fig, grafico = plt.subplots()
        grafico.pie(vendas, labels=vendedor)
        
        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    else:
        print('Arquivo não encontrado')

def data_scatter():
    arquivo = ler_arquivo()

    if arquivo:
        dados = pd.read_csv(arquivo)
        vendas = dados['vendas'].to_list()
        vendedor = dados['vendedor'].to_list()
        fig, grafico = plt.subplots()
        grafico.scatter(vendedor,vendas)

        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    else:
        print('Arquivo não encontrado')

def estatistica():
    arquivo = ler_arquivo()
    if arquivo:
        dados = pd.read_csv(arquivo)
        vendas = dados['vendas'].to_list()
        vendedor = dados['vendedor'].to_list()
        media = np.mean(vendas)
        desvio = np.std(vendas)
        #moda = np.correlate(vendas)
        mediana = np.median(vendas)
        maior_venda = np.max(vendas)
        menor_venda = np.min(vendas)
        label.config (label=f'''media':{media:.2f}
                                desvio:{desvio:.2f}
                                mediana:{mediana:.2f}
                                maior_venda:{maior_venda:.2f}
                                    
        
        
        )
       
    else: 
        print ('Erro calculo')

janela = tk.Tk()


btn1 = tk.Button(janela, text="Gráfico de linhas", command=data_plot)
btn1.pack(pady=2)

btn2 = tk.Button(janela, text="Gráfico de barras", command=data_bar)
btn2.pack(pady=2)

btn3 = tk.Button(janela, text="Gráfico de pizza", command=data_pie)
btn3.pack(pady=2)

btn4 = tk.Button(janela, text="Gráfico de dispersão", command=data_scatter)
btn4.pack(pady=2)

btn5 = tk.Button(janela, text="Mostrar estatísticas", command=estatistica)
btn5.pack(pady=2)

label = tk.Label(janela, text='')
label.pack()

janela.mainloop()
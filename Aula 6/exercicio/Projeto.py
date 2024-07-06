import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import pandas as pd


#criando os botões
j= tk.Tk()

btn1 = tk.Button(j, text="Plot Bar")
btn1.pack(pady=5)

btn2 = tk.Button(j, text="Plot Scatter")
btn2.pack(pady=5)

btn3 = tk.Button(j, text="Plot")
btn3.pack(pady=5)

btn4 = tk.Button(j, text="Plot Pie")
btn4.pack(pady=5)

btn5 = tk.Button(j, text="Estatistica")
btn5.pack(pady=5)

#criando o label que mostra a estatistica
display_sta = tk.Label(j, text= " ", bg="black", fg="white")
display_sta.pack(pady=5)

#janela em loop
j.mainloop()
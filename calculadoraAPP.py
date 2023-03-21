import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# função para converter as temperaturas
def converter_temperatura():
    escolha = int(opcao.get())

    if escolha == 1:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_label.configure(text=f'{fahrenheit}°F')

    elif escolha == 2:
        celsius = float(celsius_entry.get())
        kelvin = celsius + 273.15
        kelvin_label.configure(text=f'{kelvin} K')

    elif escolha == 3:
        fahrenheit = float(fahrenheit_entry.get())
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        kelvin_label.configure(text=f'{kelvin} K')

    elif escolha == 4:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_label.configure(text=f'{celsius}°C')

    elif escolha == 5:
        kelvin = float(kelvin_entry.get())
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        fahrenheit_label.configure(text=f'{fahrenheit}°F')

    elif escolha == 6:
        kelvin = float(kelvin_entry.get())
        celsius = kelvin - 273.15
        celsius_label.configure(text=f'{celsius}°C')

    # plotar o gráfico de conversão de temperatura
    x = np.linspace(-100, 500, 1000)
    y1 = x * 9/5 + 32
    y2 = x + 273.15
    y3 = (x - 32) * 5/9 + 273.15
    plt.plot(x, y1, 'b-', label='Celsius para Fahrenheit')
    plt.plot(x, y2, 'g-', label='Celsius para Kelvin')
    plt.plot(x, y3, 'r-', label='Fahrenheit para Kelvin')
    plt.legend(loc='upper left')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Temperatura (°F/K)')
    plt.title('Gráfico de Conversão de Temperatura')
    plt.show()

# criação da janela principal
janela = tk.Tk()
janela.title('Conversor de Temperaturas da Nicole <3')
janela.configure(bg='blue')

# criação dos widgets da janela
opcao = tk.StringVar()
opcao.set('1')

titulo_label = tk.Label(janela, text='Conversor de Temperaturas', font=('Arial', 16), bg='blue', fg='white')
titulo_label.pack(pady=10)

opcao_frame = tk.Frame(janela, bg='blue')
opcao_frame.pack()

opcao_label = tk.Label(opcao_frame, text='Escolha a conversão:', font=('Arial', 12), bg='blue', fg='white')
opcao_label.grid(row=0, column=0, padx=10)

opcao_menu = tk.OptionMenu(opcao_frame, opcao, '1', '2', '3', '4', '5', '6')
opcao_menu.grid(row=0, column=1)

celsius_frame = tk.Frame(janela, bg='blue')
celsius_frame.pack(pady=10)

celsius_label = tk.Label(celsius_frame, text='Temperatura em Celsius:', font=('Arial', 12), bg='blue', fg='white')
celsius_label.grid(row=0, column=0, padx=10)

celsius_entry = tk.Entry(celsius_frame, width=10)
celsius_entry.grid(row=0, column=1)

fahrenheit_label = tk.Label(celsius_frame, text='0°F', font=('Arial', 12), bg='blue', fg='white')
fahrenheit_label.grid(row=0, column=2)

fahrenheit_frame = tk.Frame(janela, bg='blue')
fahrenheit_frame.pack(pady=10)

fahrenheit_label = tk.Label(fahrenheit_frame, text='Temperatura em Fahrenheit:', font=('Arial', 12), bg='blue', fg='white')
fahrenheit_label.grid(row=0, column=0, padx=10)

fahrenheit_entry = tk.Entry(fahrenheit_frame, width=10)
fahrenheit_entry.grid(row=0, column=1)

celsius_label = tk.Label(fahrenheit_frame, text='0°C', font=('Arial', 12), bg='blue', fg='white')
celsius_label.grid(row=0, column=2)

kelvin_frame = tk.Frame(janela, bg='blue')
kelvin_frame.pack(pady=10)

kelvin_label = tk.Label(kelvin_frame, text='Temperatura em Kelvin:', font=('Arial', 12), bg='blue', fg='white')
kelvin_label.grid(row=0, column=0, padx=10)

kelvin_entry = tk.Entry(kelvin_frame, width=10)
kelvin_entry.grid(row=0, column=1)

celsius_label = tk.Label(kelvin_frame, text='0°C', font=('Arial', 12), bg='blue', fg='white')
celsius_label.grid(row=0, column=2)

converter_btn = tk.Button(janela, text='Converter', font=('Arial', 12), bg='blue', fg='white', command=converter_temperatura)
converter_btn.pack(pady=10)

janela.mainloop()

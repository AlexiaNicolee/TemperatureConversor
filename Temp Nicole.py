from tkinter import *
from tkinter import ttk

class ConversorTempNicole:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Temp da Nicole <3")
        self.root.geometry("400x300")
        self.root.configure(bg='white')

        self.lbl_temp = Label(self.root, text="Temperatura: ", bg='white', font=("Arial", 12))
        self.lbl_temp.grid(row=0, column=0, padx=10, pady=10)

        self.txt_temp = Entry(self.root, width=10, font=("Arial", 12))
        self.txt_temp.grid(row=0, column=1, padx=10, pady=10)

        self.lbl_origem = Label(self.root, text="De: ", bg='white', font=("Arial", 12))
        self.lbl_origem.grid(row=1, column=0, padx=10, pady=10)

        self.cbo_origem = ttk.Combobox(self.root, values=['Celsius', 'Fahrenheit', 'Kelvin'], font=("Arial", 12))
        self.cbo_origem.current(0)
        self.cbo_origem.grid(row=1, column=1, padx=10, pady=10)

        self.lbl_destino = Label(self.root, text="Para: ", bg='white', font=("Arial", 12))
        self.lbl_destino.grid(row=2, column=0, padx=10, pady=10)

        self.cbo_destino = ttk.Combobox(self.root, values=['Celsius', 'Fahrenheit', 'Kelvin'], font=("Arial", 12))
        self.cbo_destino.current(1)
        self.cbo_destino.grid(row=2, column=1, padx=10, pady=10)

        self.btn_converter = Button(self.root, text="Converter", bg='white', font=("Arial", 12), command=self.converter)
        self.btn_converter.grid(row=3, column=1, padx=10, pady=10)

        self.lbl_resultado = Label(self.root, text="", bg='white', font=("Arial", 12))
        self.lbl_resultado.grid(row=4, column=1, padx=10, pady=10)

    def converter(self):
        temperatura = float(self.txt_temp.get())
        origem = self.cbo_origem.get()
        destino = self.cbo_destino.get()

        if origem == 'Celsius':
            if destino == 'Fahrenheit':
                resultado = (temperatura * 9/5) + 32
            elif destino == 'Kelvin':
                resultado = temperatura + 273.15
            else:
                resultado = temperatura
        elif origem == 'Fahrenheit':
            if destino == 'Celsius':
                resultado = (temperatura - 32) * 5/9
            elif destino == 'Kelvin':
                resultado = (temperatura - 32) * 5/9 + 273.15
            else:
                resultado = temperatura
        else:
            if destino == 'Celsius':
                resultado = temperatura - 273.15
            elif destino == 'Fahrenheit':
                resultado = (temperatura - 273.15) * 9/5 + 32
            else:
                resultado = temperatura

        self.lbl_resultado.config(text=f"{resultado:.2f} {destino}")
        self.mudar_cor(resultado)

    def mudar_cor(self, resultado):
        if resultado < 10:
            self.root.configure(bg='blue')
        elif resultado > 30:
            self.root.configure(bg='red')
        else:
            self.root.configure(bg='white')
        
        self.root.after(1000, lambda: self.mudar_cor(resultado))

root = Tk()
app = ConversorTempNicole(root)
root.mainloop()

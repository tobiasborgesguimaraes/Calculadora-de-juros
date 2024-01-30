import tkinter as tk

root = tk.Tk()

class Aplicação:
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets()
        self.root.mainloop()
    
    def tela(self):
        self.root.title('Calculadora de juros')
        self.root.configure(background= "#FFE8CD")
        self.root.geometry('700x500')
        self.root.resizable(False, False)
    
    def widgets(self):
        self.labelCapital = tk.Label(root, text= 'Capital', bg= "#FFE8CD")
        self.labelCapital.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight=0.05)
        self.entryCapital = tk.Entry(root)
        self.entryCapital.place(relx= 0.15, rely= 0.2, relwidth= 0.2, relheight=0.05)

        self.labelTempo = tk.Label(root, text= 'Tempo', bg= "#FFE8CD")
        self.labelTempo.place(relx= 0.45, rely= 0.1, relwidth= 0.1, relheight=0.05)
        self.entryTempo = tk.Entry(root)
        self.entryTempo.place(relx= 0.4, rely= 0.2, relwidth= 0.2, relheight=0.05)

        self.labelJuros = tk.Label(root, text= 'Juros', bg= "#FFE8CD")
        self.labelJuros.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight=0.05)
        self.entryJuros = tk.Entry(root)
        self.entryJuros.place(relx= 0.65, rely= 0.2, relwidth= 0.2, relheight=0.05)

        self.calcularSimples = tk.Button(root, text= "Calcular com Juros Simples")
        self.calcularSimples.place(relx= 0.15, rely= 0.8, relwidth= 0.3, relheight=0.1)

        self.calcularComposto = tk.Button(root, text= "Calcular com Juros Compostos")
        self.calcularComposto.place(relx= 0.55, rely= 0.8, relwidth= 0.3, relheight=0.1)


Aplicação()
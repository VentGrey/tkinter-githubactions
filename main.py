import sys
import webbrowser

# Condicionar el import de tkinter de acuerdo a nuestra versión de Python.

if sys.version_info[0] == 3:
    from tkinter import Tk, Label, Button, Menu, Text, messagebox
else:
    from Tkinter import Tk, Label, Button, Menu, Text, messagebox

# Definir una clase para nuestra GUI.

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Visita La Esquina Gris")
        self.geometry("400x400")
        
        self.label = Label(self, text="¡Visita La Esquina Gris!")
        self.label.pack()
        
        self.button = Button(self, text="Visitar en mi navegador", command=self.visit)
        self.button.pack()
        
    def visit(self):
        webbrowser.open("https://ventgrey.github.io")
        
# Inicializar la GUI.

app = App()
app.mainloop()


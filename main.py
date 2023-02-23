import sys
import webbrowser
import traceback
import datetime
import pyi_splash
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
        
        self.label: Label = Label(self, text="¡Visita La Esquina Gris!")
        self.label.pack()
        
        self.button: Button = Button(self, text="Visitar en mi navegador", command=self.visit)
        self.button.pack()

        self.error_button = Button(self, text="Probar error", command=self.provoke_error)
        self.error_button.pack()
        
    def visit(self):
        webbrowser.open("https://ventgrey.github.io")

    def provoke_error(self):
        error: str = "Error de a mentis, maneja tus propios try-except"
        now = datetime.datetime.now()
        with open("registro.txt", "a") as file:
            file.write(f"Ocurrió un error {error} a las {now}\n")
        messagebox.showerror("Error", "Ha ocurrido un error, envie el archivo registro.txt al programador para ayudarle")

        
# Inicializar la GUI.

app: App = App()

# Cerrar el splashscreen
pyi_splash.close()

app.mainloop()


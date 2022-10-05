import tkinter as tk
from typing import Container
from constantes import style
from screens import Menu, Abrir, GuardarComo, Analizar, Errores, Ayuda, CargarArchivo

class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("PROYECTO 1_202110509")
        container = tk.Frame(self)
        #self.mode = "Archivo"
        container.pack(side="top", fill="both", expand=True)
        container.configure(background=style.BACKGROUND)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, Abrir, GuardarComo, Analizar, Errores, Ayuda, CargarArchivo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Menu)
        
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

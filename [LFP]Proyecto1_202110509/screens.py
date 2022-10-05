from cgitb import text
import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.messagebox import showinfo
from webbrowser import get
from constantes import style, config
from tkinter import *
from Token import Token
from Operacion import Operacion
from Excepcion import Excepcion


class Automata:
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u","v","w","x","y","z"]
    numeros = ["1","2","3","4","5","6","7","8","9","0", ".", "-"]
    tabla_tokens = []
    tabla_erorres = []
    cadena = ''
    fila = 0
    columna = 0
    estado_actual = 0
    estado_anterior = 0

    def recuperar_error(self, conte, columna, fila):
         #se registra el error
         error_obj = Excepcion( conte[0], "Error", columna, fila)
         self.tabla_erorres.append(error_obj)
        
    #     #se recupera del error, desechando caracteres hasta encontrar un delimitador,
    #     #en este caso un >
         res = conte
         caracter = res[0]
         while caracter != '>':
             res = res[1:]
             caracter = res[0]

         return conte[1:]

    def analizar1(self, cadena1):
        etiqueta_abre = ''
        etiqueta_cierra = ''
        token = ''
        operaciones = []
        cierre = False

        # recorrer cadena
        while len(cadena1) > 0:
            char = cadena1[0]

            # ignorar espacios en blanco o saltos de linea
            if char == '\n':
                self.fila += 1
                self.columna = 0
                cadena1 = cadena1[1:]
                continue
            elif char == ' ':
                self.columna += 1
                cadena1 = cadena1[1:]
                continue

            # verificar estado actual
            if self.estado_actual == 0:
                if char == '<':
                    self.estado_actual = 1
                    self.estado_anterior = 0
                else:
                    #solo creé nuevo estado para mover los errores y sea estado ERROR
                    #  self.estado_actual = 6
                    #  self.estado_anterior = 0
                     res = self.recuperar_error(cadena1, self.columna, self.fila)
                     cadena1 = res
                    #  self.estado_actual = 0
                    #  self.estado_anterior=6

            elif self.estado_actual == 1:
                if char.lower() in self.letras:
                    self.estado_actual = 1
                    self.estado_anterior = 1
                elif char == '>':
                    self.estado_actual = 2
                    self.estado_anterior = 1
                elif char == '=':
                    self.estado_actual = 3
                    self.estado_anterior = 1
                elif char == '/':
                    self.estado_actual = 5
                    self.estado_anterior = 1
                else:
                    # self.estado_actual = 6
                    # self.estado_anterior = 1
                    res = self.recuperar_error(cadena1, self.columna, self.fila)
                    cadena1 = res
                    # self.estado_actual = 1
                    # self.estado_anterior=6                    

            elif self.estado_actual == 2:
                if char in '<':
                    self.estado_actual = 1
                    self.estado_anterior = 2
                elif char in self.numeros:
                    self.estado_actual = 4
                    self.estado_anterior = 2
                else:
                    # self.estado_actual = 6
                    # self.estado_anterior = 2
                    res = self.recuperar_error(cadena1, self.columna, self.fila)
                    cadena1 = res
                    # self.estado_actual = 2
                    # self.estado_anterior=6

            elif self.estado_actual == 3:
                if char.lower() in self.letras:
                    self.estado_actual = 1
                    self.estado_anterior = 3
                else:
                    # self.estado_actual = 6
                    # self.estado_anterior = 3
                    res = self.recuperar_error(cadena1, self.columna, self.fila)
                    cadena1 = res
                    # self.estado_actual = 3
                    # self.estado_anterior=6                   

            elif self.estado_actual == 4:
                if char in '<':
                    self.estado_actual = 1
                    self.estado_anterior = 4
                elif char in self.numeros:
                    self.estado_actual = 4
                    self.estado_anterior = 4
                else:
                    #   self.estado_actual = 6
                    #   self.estado_anterior = 4
                      res = self.recuperar_error(cadena1, self.columna, self.fila)
                      cadena1 = res
                    #   self.estado_actual = 4
                    #   self.estado_anterior=6


            elif self.estado_actual == 5:
                if char.lower() in self.letras:
                    self.estado_actual = 1
                    self.estado_anterior = 5
                else:
                    #   self.estado_actual = 6
                    #   self.estado_anterior = 5
                      res = self.recuperar_error(cadena1, self.columna, self.fila)
                      cadena1 = res
                    #   self.estado_actual = 5
                    #   self.estado_anterior=6

            # print(self.estado_anterior, '->', self.estado_actual)
            self.columna += 1
            cadena1 = cadena1[1:]


    def imprimir_errores(self):
        errores = ""
        #  print('-'*43)
        #  print ("| {:<7} | {:<7} | {:<4} | {:<4} |".format('Lexema','Tipo','Columna','fila'))
        #  print('-'*43)
        for error in self.tabla_erorres:
            #print ("| {:<7} | {:<7} | {:<7} | {:<4} |".format(error.error, error.tipo, error.columna, error.fila))
            errores += ('<td align = "center">'+error.error+'</td>\n<td align = "center">'+error.tipo+'</td>\n<td align = "center">'+str(error.columna)+'</td>\n<td align = "center">'+str(error.fila)+'</td>\n</tr>\n')  
        html = ('<table border="1" style="width:100%" align = "center">\n'+
                 '<tr>\n'+
                 '<th>Lexema</th>\n'+
                 '<th>Tipo</th>\n'+
                 '<th>Columna</th>\n'+
                 '<th>Fila</th>\n'+
                 '</tr>\n'+
                 '<tr>\n'+
                 errores)
        self.tabla_erorres.clear()
        return html 
                       


    def analizar(self, cadena, operacion:Operacion):
        etiqueta_abre = ''
        etiqueta_cierra = ''
        token = ''
        operaciones = []
        cierre = False
        tipo = operaciones

        # recorrer cadena
        while len(cadena) > 0:
            char = cadena[0]

            # ignorar espacios en blanco o saltos de linea
            if char == '\n':
                self.fila += 1
                self.columna = 0
                cadena = cadena[1:]
                continue
            elif char == ' ':
                self.columna += 1
                cadena = cadena[1:]
                continue

            # verificar estado actual
            if self.estado_actual == 0:
                if char == '<':
                    self.guardar_token(char)
                    self.estado_actual = 1
                    self.estado_anterior = 0

            elif self.estado_actual == 1:
                if char.lower() in self.letras:
                    token += char
                    self.estado_actual = 1
                    self.estado_anterior = 1
                elif char == '>':
                    self.guardar_token(token)
                    self.guardar_token(char)

                    if cierre:
                        etiqueta_cierra = token
                        cierre = False

                        if etiqueta_cierra.lower() == 'operacion':
                            operacion.operandos = operaciones
                            return [cadena, operacion]

                    if etiqueta_abre.lower() == 'operacion':
                        op = Operacion(token)
                        valor = self.analizar(cadena[1:], op)
                        cadena = valor[0]
                        operaciones.append(valor[1])
                    
                    etiqueta_abre = token
                    token = ''

                    self.estado_actual = 2
                    self.estado_anterior = 1
                elif char == '=':
                    etiqueta_abre = token

                    self.guardar_token(token)
                    self.guardar_token(char)
                    token = ''

                    self.estado_actual = 3
                    self.estado_anterior = 1
                elif char == '/':
                    cierre = True
                    self.guardar_token(char)

                    self.estado_actual = 5
                    self.estado_anterior = 1
                # else:
                #     res = self.recuperar_error(cadena, self.columna, self.fila)
                #     cadena = res

            elif self.estado_actual == 2:
                if char in '<':
                    self.guardar_token(char)

                    self.estado_actual = 1
                    self.estado_anterior = 2
                elif char in self.numeros:
                    token += char
                    self.estado_actual = 4
                    self.estado_anterior = 2
                # else:
                #     res = self.recuperar_error(cadena, self.columna, self.fila)
                #     cadena = res


            elif self.estado_actual == 3:
                if char.lower() in self.letras:
                    token += char
                    self.estado_actual = 1
                    self.estado_anterior = 3
                # else:
                #     res = self.recuperar_error(cadena, self.columna, self.fila)
                #     cadena = res
                    

            elif self.estado_actual == 4:
                if char in '<':
                    if etiqueta_abre.lower() == 'numero':
                        operaciones.append(token)
                    self.guardar_token(token)
                    self.guardar_token(char)
                    token = ''
                    self.estado_actual = 1
                    self.estado_anterior = 4
        

                elif char in self.numeros:
                    token += char

                    self.estado_actual = 4
                    self.estado_anterior = 4
                # else:
                #     res = self.recuperar_error(cadena, self.columna, self.fila)
                #     cadena = res

            elif self.estado_actual == 5:
                if char.lower() in self.letras:
                    token += char
                    self.estado_actual = 1
                    self.estado_anterior = 5
                # else:
                #     res = self.recuperar_error(cadena, self.columna, self.fila)
                #     cadena = res
            # print(self.estado_anterior, '->', self.estado_actual)
            self.columna += 1
            cadena = cadena[1:]

        operacion.operandos = operacion
        return [cadena, operaciones]

    def guardar_token(self, lexema):
        nuevo_token = Token(self.fila, self.columna, lexema)
        #self.tabla_tokens.clear()
        self.tabla_tokens.append(nuevo_token)

    def imprimir_tokens(self):
        print('-'*31)
        print ("| {:<4} | {:<7} | {:<10} |".format('Fila','Columna','Lexema'))
        print('-'*31)
        for token in self.tabla_tokens:
            print ("| {:<4} | {:<7} | {:<10} |".format(token.fila, token.columna, token.lexema))
        self.tabla_tokens.clear()
    



#-----------------------Pantalla de Inicio--------------------------------------
class Menu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        #self.opcion = tk.StringVar(self, value="Archivo")

        self.init_widgets()
    
    
    def moveToArchivo(self):
        #self.controller.mode = self.opcion.get()
        self.abrirArch = filedialog.askopenfile(title = 'Abrir Archivo', filetypes = [('Text Files', '*.txt'), 
        ('All Files', '*.*')])
        with open(self.abrirArch.name, 'r') as f:
            self.Archi = f.read()
        #self.Archi = open(self.abrirArch.name, 'r')
        abierto = self.abrirArch.name
        cont = self.Archi
        moverInfo(cont, abierto)
        #print(cont)
        #print(self.abrirArch)
        self.controller.show_frame(CargarArchivo)


    def moveToAyuda(self):
        self.controller.show_frame(Ayuda)

    def regresar(self):
        self.controller.show_frame(Menu)
    
    def salir(self):
        sys.exit()
    
    def init_widgets(self):
        tk.Label(
            self, 
            text = "======MENÚ PRINCIPAL======",
            justify= tk.CENTER,
            **style.STYLE
            ).pack(
                side = tk.TOP,
                fill = tk.BOTH,
                expand = True,
                padx = 22,
                pady = 11
            )
        optionFrame = tk.Frame(self)
        optionFrame.configure(background=style.COMPONENT)
        optionFrame.pack(
            side=tk.TOP, 
            fill=tk.BOTH, 
            expand=True,
            padx=22,
            pady=11
        )
        tk.Label(
            optionFrame,
            text = "=====Elija una opción=====",
            justify= tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Cargar Archivo",
            command=self.moveToArchivo,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Ayuda",
            command=self.moveToAyuda,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Salir",
            command=self.salir,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )


#------------------------------------------------------------------------------------------------------------
contenido=""
direccion=""
def moverInfo(cont, abierto):
    global contenido, direccion
    contenido = cont
    direccion = abierto
    #print(contenido)
    return contenido, direccion

#------------------------------------------------------------------------------------------------------------
class CargarArchivo(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.init_widgets()
    
    def regresar(self):
        self.controller.show_frame(Menu)
    
    def moveToAbrir(self):
        self.controller.show_frame(Abrir)
    
    def AbrirArchi(self):
        with open(direccion, 'r') as f:
            global cont1
            cont1 = f.read()
        moverInfo(cont1, direccion)
        abrirArch()

    def guardarA(self):
        messagebox.showwarning(message="Se ha guardado el Archivo", title="GUARDADO")

    def guardarCom(self):
        files = [('Text Document', '*.txt'),
                ('All Files', '*.*'),  
                ('Python Files', '*.py')] 
        file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
        with open(direccion, 'r') as f:
            cont2 = f.read()
        file.write(cont2) 
        messagebox.showwarning(message="Se ha guardado el Archivo", title="FELICIDADES")

    def analizar(self):
        cont = ""
        sumas = 1
        restas = 1
        mult = 1
        div = 1
        pot = 1
        mod = 1
        tan = 1
        cos = 1
        sen = 1
        raiz = 1
        inve = 1
        complejo = 1
        autom = Automata()
        with open(direccion, 'r') as f:
            cont3 = f.read()
        cadena = cont3
        resultado = autom.analizar(cadena, Operacion(''))
        for oper in resultado[1]:
            opera = oper.operar()
            #print(opera)
            opera1=oper.resultado(opera)
            texto = " "
            opera2 = " "
            if oper.nombreOperacion() == 'suma':
                texto = sumas
                opera2=str(opera)
                sumas += 1
            if oper.nombreOperacion() == 'resta':
                texto = restas
                opera2=str(opera)
                restas += 1
            if oper.nombreOperacion() == 'multiplicacion':
                texto = mult
                opera2=str(opera)
                mult += 1
            if oper.nombreOperacion() == 'division':
                texto = div
                opera2=str(opera)
                div += 1
            if oper.nombreOperacion() == 'potencia':
                texto = pot
                opera2=("Potencia"+" "+"("+str(opera)+")")
                pot += 1
            if oper.nombreOperacion() == 'mod':
                texto = mod
                opera2=("Mod"+" "+"("+opera+")")
                mod += 1
            if oper.nombreOperacion() == 'tangente':
                texto = tan
                opera2=("Tangente"+" "+"("+opera+")")
                tan += 1
            if oper.nombreOperacion() == 'coseno':
                texto = cos
                opera2=("Coseno"+" "+"("+opera+")")
                cos += 1
            if oper.nombreOperacion() == 'seno':
                texto = sen
                opera2=("Seno"+" "+"("+opera+")")
                sen += 1
            if oper.nombreOperacion() == 'raiz':
                texto = raiz
                opera2=("Raiz"+" "+"("+opera+")")
                raiz += 1
            if oper.nombreOperacion() == 'inverso':
                texto = inve
                opera2=("Inverso"+" "+"("+opera+")")
                inve += 1
            cont += "<h3>Operacion"+" "+oper.nombreOperacion()+" "+str(texto)+":"+"</h3>\n"+"<h4>"+opera2 + " = " +str(opera1)+"</h4>\n"                  
        #autom.imprimir_tokens()
        messagebox.showwarning(message="Análisis Completado", title="FELICIDADES")
        escribirHtml(cont)
    
    def errores(self):
         autom = Automata()
         with open(direccion, 'r') as f:
             cont3 = f.read()
         autom.analizar1(cont3)
         #autom.imprimir_errores()
         messagebox.showwarning(message="Errores impresos", title="FELICIDADES")
         escribirHtml1(autom.imprimir_errores())

    def init_widgets(self):
        optionFrame = tk.Frame(self)
        optionFrame.configure(background=style.COMPONENT)
        optionFrame.pack(
            side=tk.TOP, 
            fill=tk.BOTH, 
            expand=True,
            padx=22,
            pady=11
        )
        tk.Label(
            optionFrame,
            text = "=====Elija una opción=====",
            justify= tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Abrir Archivo",
            command=self.AbrirArchi,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Guardar Como",
            command=self.guardarCom,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Analizar",
            command=self.analizar,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Errores",
            command=self.errores,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Regresar",
            command=self.regresar,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )

#------------------------------------------------------------------------------------------------------------
def escribirHtml(cont):
    with open("RESULTADOS_202110509.html", "w") as archivo:
        antes = ("<!DOCTYPE html>\n"+
            "<html>\n"+
            "<head>\n"+
            "<title>"+"RESULTADOS"+"</title>\n"+
            "</head>\n"+
            "<body>\n"
            "<h1>RESULTADOS</h1>\n")
        despues = ("</body>\n"+
                    "</html>")
           
        archivo.write(antes+cont+despues)
    archivo.close()
    directorio = os.getcwd()
    os.startfile(directorio+"\RESULTADOS_202110509.html")

def escribirHtml1(cont1):
    with open("ERRORES_202110509.html", "w") as archivo:
        antes = ("<!DOCTYPE html>\n"+
            "<html>\n"+
            "<head>\n"+
            "<title>"+"ERRORES"+"</title>\n"+
            "</head>\n"+
            "<body>\n"
            "<h1>ERRORES</h1>\n")
        despues = ("</body>\n"+
                    "</html>")
           
        archivo.write(antes+cont1+despues)
    archivo.close()
    directorio = os.getcwd()
    os.startfile(directorio+"\ERRORES_202110509.html")
#------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------
def abrirArch():
    ventana = tk.Tk()
    ventana.geometry("670x550")
    ventana.title("Archivo")
    ventana.resizable(False,False)
    ventana.configure(background=style.BACKGROUND)

    def regresar():
        ventana.destroy()

    def guardarArch():
        global archivo
        with open(direccion, "w") as archivo:
            archivo.write(cajita.get(1.0, tk.END+"-1c"))
        messagebox.showwarning(message="Se ha guardado el Archivo", title="GUARDADO")
        ventana.destroy()


    cajita =Text(ventana, width=50, height=10, **style.STYLE)
    cajita.insert("1.0",contenido)
    cajita.pack(
            side=tk.TOP, 
            fill=tk.BOTH,
            expand=True, 
            padx=22, 
            pady=11)

    tk.Button(
            ventana,
            text = "Guardar",
            command=guardarArch,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
    tk.Button(
            ventana,
            text = "Regresar",
            command=regresar,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )





#------------------------------------------------------------------------------------------------------------
class Abrir(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.init_widgets()

    def regresar(self):
        self.controller.show_frame(CargarArchivo)

    def init_widgets(self):
        optionFrame = tk.Frame(self)
        optionFrame.configure(background=style.COMPONENT)
        # optionFrame.pack(
        #     side=tk.TOP, 
        #     fill=tk.BOTH, 
        #     expand=True,
        #     padx=22,
        #     pady=11
        # ) 
        #global caja1

        cajita =Text(self, width=50, height=10, **style.STYLE)
        cajita.insert("1.0","hola"+contenido)
        cajita.pack(
            side=tk.TOP, 
            fill=tk.BOTH,
            expand=True, 
            padx=22, 
            pady=11)
        tk.Button(
            self,
            text = "Guardar",
            #command=self.capturar,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Regresar",
            command=self.regresar,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
#------------------------------------------------------------------------------------------------------------

class GuardarComo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        

#------------------------------------------------------------------------------------------------------------

class Analizar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller

#------------------------------------------------------------------------------------------------------------

class Errores(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller


#------------------------------------------------------------------------------------------------------------

#Crear manuales nada mas
class Ayuda(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.init_widgets()

    def mensaje(self):
        showinfo("Temas de Ayuda", "Curso: Lab. Lenguajes Formales y de Programación\nNombre: Mario Ernesto Marroquín Pérez\nCarné: 202110509"),

    def regresar(self):
        self.controller.show_frame(Menu)
    
    def abrirManualUsuario(self):
        directorio = os.getcwd()
        os.startfile(directorio+"\Manuales\ManualUsuPrueba.pdf")

    def abrirManualTec(self):
        directorio = os.getcwd()
        os.startfile(directorio+"\Manuales\ManualTecPrueba.pdf")

    def init_widgets(self):
        optionFrame = tk.Frame(self)
        optionFrame.configure(background=style.COMPONENT)
        # optionFrame.pack(
        #     side=tk.TOP, 
        #     fill=tk.BOTH, 
        #     expand=True,
        #     padx=22,
        #     pady=11
        # )
        
        tk.Button(
            self,
            text = "Manual de Usuario",
            command=self.abrirManualUsuario,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Manual Técnico",
            command=self.abrirManualTec,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Temas de Ayuda",
            command=self.mensaje,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        tk.Button(
            self,
            text = "Regresar",
            command=self.regresar,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )

# Modulos basicos utilizados
import tkinter
import tkinter.messagebox
import sqlite3
from os.path import abspath,join
import sys

# Clase de ejecución de la interfaz
class inicio:
    def __init__(self):
        self.ventana=tkinter.Tk()
        self.ventana.geometry("600x640+383+24")
        self.ventana.iconbitmap(self.ruta_absoluta("imagenes/icono.ico"))
        self.ventana.resizable(width=False,height=False)
        self.ventana.title("Inicio")
        self.ventana.config(bg="#8085AC")
    
        #imagen
        self.imagen=tkinter.PhotoImage(file=self.ruta_absoluta("imagenes/finanzApp.png"))

        # Labels
        self.imagenAplicacion=tkinter.Label(self.ventana,image=self.imagen)
        self.imagenAplicacion.config(bg="#8085AC",width=215,height=250)
        self.imagenAplicacion.pack(pady=15)
        self.nombreApp=tkinter.Label(self.ventana,text="finanzApp ",font=("Times New Roman",21,"bold"),bg="#8085AC")
        self.nombreApp.place(x=230,y=235)

        #botones
        self.botonIngresos=tkinter.Button(self.ventana,text="Ingresos",font=("arial",11,"bold"),width=9,height=1,command=self.ingresos)
        self.botonIngresos.place(x=255,y=280)
        self.botonIngresos.config(cursor='hand2',bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonEgresos=tkinter.Button(self.ventana,text="Egresos",font=("arial",11,"bold"),width=9,height=1,command=self.egresos)
        self.botonEgresos.place(x=255,y=325)
        self.botonEgresos.config(cursor='hand2',bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonEstadisticas=tkinter.Button(self.ventana,text="Estadisticas",font=("arial",11,"bold"),width=9,height=1,command=self.estadisticas)
        self.botonEstadisticas.place(x=255,y=370)
        self.botonEstadisticas.config(cursor='hand2',bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botoninfo=tkinter.Button(self.ventana,text="Informacion",font=("arial",11,"bold"),width=9,height=1,command=self.info)
        self.botoninfo.place(x=255,y=415)
        self.botoninfo.config(cursor='hand2',bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonAcercade=tkinter.Button(self.ventana,text="Acerca de",font=("arial",11,"bold"),width=9,height=1,command=self.acercade)
        self.botonAcercade.place(x=255,y=460)
        self.botonAcercade.config(cursor='hand2',bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonSalir=tkinter.Button(self.ventana,text="Salir",font=("arial",11,"bold"),width=9,height=1,command=self.salir)
        self.botonSalir.place(x=255,y=505)
        self.botonSalir.config(cursor='hand2',bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)

        #pie de pagina
        self.pieDepagina=tkinter.Label(self.ventana,text="© 2025 - Rheyjach Arrieta",font=("arial",10,"bold"),bg="#8085AC")
        self.pieDepagina.place(x=217,y=620)

        #crear base de datos y tablas
        self.crear()
        
        #Bucle de la interfaz
        self.ventana.mainloop()

        #funciones
    #funcion de rutas
    def ruta_absoluta(self,ruta_relativa):
        if hasattr(sys,'_MEIPASS'):
            self.ruta_base=sys._MEIPASS
        else:
            self.ruta_base=abspath(".")
        return join(self.ruta_base,ruta_relativa)
    #funciones de los botones
    def ingresos(self):
        from ingresos import ingresos
        self.ventana.destroy()
        ingresos()
    def egresos(self):
        from egresos import egresos
        self.ventana.destroy()
        egresos()
    def estadisticas(self):
        from estadisticas import estadisticas
        self.ventana.destroy()
        estadisticas()
    def info(self):
        tkinter.messagebox.showinfo("INFORMACION","Esta aplicacion tiene la capacidad de registrar tus ingresos y egresos,"
                                    " a la vez que genera un balance general y unas estadisticas relacionadas que permitiran"
                                    " que tomes decisiones fundamentadas en terminos financieros")
    def acercade(self):
        tkinter.messagebox.showinfo("ACERCA DE","Esta aplicacion fue desarrollada por Rheyjach Arrieta Delgado con el objetivo"
                                    " de desarrollar una aplicacion funcional")
    def salir(self):
        self.salirAplicacion=tkinter.messagebox.askokcancel("SALIR","¿Desea salir de la aplicacion?")
        if self.salirAplicacion==True:
            self.ventana.destroy()
    #funciones de conexiones a base de datos
    def crear(self):
        self.conexion=sqlite3.connect('datos.db')
        self.cursor=self.conexion.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS ingresos(Registro INTEGER PRIMARY KEY AUTOINCREMENT,Ingreso REAL NOT NULL, Origen TEXT NOT NULL,Categoria TEXT NOT NULL, Fecha TEXT NOT NULL)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS egresos(Registro INTEGER PRIMARY KEY AUTOINCREMENT,Egreso REAL NOT NULL, Origen TEXT NOT NULL,Categoria TEXT NOT NULL, Fecha TEXT NOT NULL)")
        self.conexion.commit()
        self.conexion.close()

# Este script inicia la aplicación creando una instancia de la clase 'inicio'
if __name__=='__main__':
    ejecutar=inicio()
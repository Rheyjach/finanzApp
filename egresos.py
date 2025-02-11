# Modulos basicos utilizados
import tkinter
import tkinter.messagebox
import tkinter.ttk
import sqlite3
from datetime import date
from os.path import abspath,join
import sys

# Clase de ejecución de la interfaz
class egresos:
    def __init__(self):
        self.ventana=tkinter.Tk()
        self.ventana.title("finanzApp")
        self.ventana.geometry("600x640+383+24")
        self.ventana.iconbitmap(self.ruta_absoluta("imagenes/icono.ico"))
        self.ventana.config(bg="#8085AC")
        self.ventana.resizable(width=False,height=False)

        #barra menu
        self.barraMenu=tkinter.Menu()
        self.ventana.config(menu=self.barraMenu)
        self.barraMenu.add_command(label="Informacion",command=self.info)
        self.barraMenu.add_command(label="Acerca de",command=self.acercade)
        self.barraMenu.add_command(label="Salir",command=self.salir)
        
        #labels
        #registrar egresos
        self.registrarEgresos=tkinter.Label(self.ventana,text="Registrar Egresos",font=("arial",15,"bold"),bg="#8085AC")
        self.registrarEgresos.place(x=15,y=15)
        self.Egreso=tkinter.Label(self.ventana,text="Egreso ($)",font=("arial",13,"bold"),bg="#8085AC")
        self.Egreso.place(x=15,y=45)
        self.origen=tkinter.Label(self.ventana,text="Origen",font=("arial",13,"bold"),bg="#8085AC")
        self.origen.place(x=165,y=45)
        self.categoria=tkinter.Label(self.ventana,text="Categoria",font=("arial",13,"bold"),bg="#8085AC")
        self.categoria.place(x=315,y=45)
        self.separador1=tkinter.Label(self.ventana,text='________________________',font=("arial",13,"bold"),bg="#8085AC")
        self.separador1.place(x=15,y=95)
        #filtros
        self.filtros=tkinter.Label(self.ventana,text="Filtros",font=("arial",15,"bold"),bg="#8085AC")
        self.filtros.place(x=15,y=120)
        self.filtroRegistro=tkinter.Label(self.ventana,text="Registro",font=("arial",13,"bold"),bg="#8085AC")
        self.filtroRegistro.place(x=15,y=150)
        self.filtroEgreso=tkinter.Label(self.ventana,text="Egreso ($)",font=("arial",13,"bold"),bg="#8085AC")
        self.filtroEgreso.place(x=165,y=150)
        self.filtroOrigen=tkinter.Label(self.ventana,text="Origen",font=("arial",13,"bold"),bg="#8085AC")
        self.filtroOrigen.place(x=315,y=150)
        self.filtroFecharegistro=tkinter.Label(self.ventana,text="Fecha",font=("arial",13,"bold"),bg="#8085AC")
        self.filtroFecharegistro.place(x=15,y=205)
        self.filtroMes=tkinter.Label(self.ventana,text="Mes",font=("arial",13,"bold"),bg="#8085AC")
        self.filtroMes.place(x=165,y=205)
        self.filtroCategoria=tkinter.Label(self.ventana,text="Categoria",font=("arial",13,"bold"),bg="#8085AC")
        self.filtroCategoria.place(x=315,y=205)
        self.separador2=tkinter.Label(self.ventana,text='________________________',font=("arial",13,"bold"),bg="#8085AC")
        self.separador2.place(x=15,y=255)
        #eliminar
        self.eliminar=tkinter.Label(self.ventana,text="Eliminar",font=("arial",15,"bold"),bg="#8085AC")
        self.eliminar.place(x=15,y=280)
        self.eliminarRegistro=tkinter.Label(self.ventana,text="Registro",font=("arial",13,"bold"),bg="#8085AC")
        self.eliminarRegistro.place(x=15,y=310)
        self.separador3=tkinter.Label(self.ventana,text='________________________',font=("arial",13,"bold"),bg="#8085AC")
        self.separador3.place(x=15,y=335)
        #tabla
        self.egresosAlmacenados=tkinter.Label(self.ventana,text="Egresos Almacenados",font=("arial",15,"bold"),bg="#8085AC")
        self.egresosAlmacenados.place(x=15,y=358)

        #entrys
        #registrar ingresos
        self.entryEgreso=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=9)
        self.entryEgreso.place(x=15,y=70)
        self.entryOrigen=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=9)
        self.entryOrigen.place(x=165,y=70)
            #lista deplegable
        self.listaDesplegable=tkinter.ttk.Combobox(self.ventana,values=["Vivienda","Comida","Salud","Transporte","Inversion","Empresarial","Recreacion","Imprevisto","Otro"],state='readonly',font=("arial",11,"bold"),width=11)
        self.listaDesplegable.place(x=315,y=70)
        #filtros
        self.entryfiltroRegistro=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=9)
        self.entryfiltroRegistro.place(x=15,y=175)
        self.entryfiltroEgreso=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=9)
        self.entryfiltroEgreso.place(x=165,y=175)
        self.entryfiltroOrigen=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=9)
        self.entryfiltroOrigen.place(x=315,y=175)
        self.entryfiltroFecha=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=9)
        self.entryfiltroFecha.place(x=15,y=230)
        self.entryfiltroMes=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=9)
        self.entryfiltroMes.place(x=165,y=230)
            #lista deplegable
        self.filtrolistaDesplegable=tkinter.ttk.Combobox(self.ventana,values=["Vivienda","Comida","Salud","Transporte","Inversion","Empresarial","Recreacion","Imprevisto","Otro"],state='readonly',font=("arial",11,"bold"),width=11)
        self.filtrolistaDesplegable.place(x=315,y=230)
        #eliminar
        self.entryeliminarRegistro=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=9)
        self.entryeliminarRegistro.place(x=105,y=310)
        

        #botones
        #registrar ingresos
        self.botonRegistrar=tkinter.Button(self.ventana,text="Registrar",font=("arial",11,"bold"),width=9,height=1,command=self.registrar)
        self.botonRegistrar.place(x=465,y=60)
        self.botonRegistrar.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        #filtros
        self.botonfiltroRegistro=tkinter.Button(self.ventana,text="Filtrar",font=("arial",7,"bold"),width=5,height=1,command=self.funcionfiltroRegistro)
        self.botonfiltroRegistro.place(x=105,y=178)
        self.botonfiltroRegistro.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonfiltroEgreso=tkinter.Button(self.ventana,text="Filtrar",font=("arial",7,"bold"),width=5,height=1,command=self.funcionfiltroEgreso)
        self.botonfiltroEgreso.place(x=255,y=178)
        self.botonfiltroEgreso.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonfiltroOrigen=tkinter.Button(self.ventana,text="Filtrar",font=("arial",7,"bold"),width=5,height=1,command=self.funcionfiltroOrigen)
        self.botonfiltroOrigen.place(x=405,y=178)
        self.botonfiltroOrigen.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonfiltroFecha=tkinter.Button(self.ventana,text="Filtrar",font=("arial",7,"bold"),width=5,height=1,command=self.funcionfiltroFecha)
        self.botonfiltroFecha.place(x=105,y=233)
        self.botonfiltroFecha.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonfiltroMes=tkinter.Button(self.ventana,text="Filtrar",font=("arial",7,"bold"),width=5,height=1,command=self.funcionfiltroMes)
        self.botonfiltroMes.place(x=255,y=233)
        self.botonfiltroMes.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonfiltroCategoria=tkinter.Button(self.ventana,text="Filtrar",font=("arial",7,"bold"),width=5,height=1,command=self.funcionfiltroCategoria)
        self.botonfiltroCategoria.place(x=430,y=233)
        self.botonfiltroCategoria.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        #eliminar
        self.botoneliminarRegistro=tkinter.Button(self.ventana,text="Eliminar",font=("arial",7,"bold"),width=8,height=1,command=self.funcionEliminarregistro)
        self.botoneliminarRegistro.place(x=200,y=310)
        self.botoneliminarRegistro.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        #volver al inicio
        self.botonInicio=tkinter.Button(self.ventana,text="Inicio",font=("arial",11,"bold"),width=9,height=1,command=self.inicio)
        self.botonInicio.place(x=465,y=575)
        self.botonInicio.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        #mostrar todos los datos
        self.botonmostrarDatos=tkinter.Button(self.ventana,text="Registros Totales",font=("arial",11,"bold"),width=14,height=1,command=self.funcionTotalregistros)
        self.botonmostrarDatos.place(x=15,y=575)
        self.botonmostrarDatos.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)

        #scroll
        self.scrollVertical=tkinter.Scrollbar(self.ventana, orient="vertical")
        self.scrollVertical.place(x=560,y=385,height=185)

        #tabla treeview
        self.tabla=tkinter.ttk.Treeview(self.ventana,columns=('Registro','Egreso ($)','Origen','Categoria','Fecha de Registro'),yscrollcommand=self.scrollVertical.set)
        self.tabla.place(x=15,y=385)
        self.tabla.config(height=8)
            #encabezados
        self.tabla.heading('#1',text='Registro')
        self.tabla.heading('#2',text='Egreso ($)')
        self.tabla.heading('#3',text='Origen')
        self.tabla.heading('#4',text='Categoria')
        self.tabla.heading('#5',text='Fecha de Registro')

            #columnas
        self.tabla.column('#0',width=0,stretch=tkinter.NO)
        self.tabla.column('#1',width=105,anchor='center')
        self.tabla.column('#2',width=105,anchor='center')
        self.tabla.column('#3',width=105,anchor='center')
        self.tabla.column('#4',width=105,anchor='center')
        self.tabla.column('#5',width=105,anchor='center')

        #eventos de la tabla
        self.tabla.bind("<Button-1>", self.copiar_valor)

        #vinculacion del scroll con la tabla
        self.scrollVertical.config(command=self.tabla.yview)

        #llamar funciones basicas de base de datos
        self.cargar()

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
    #funciones barra de menu
    def info(self):
        tkinter.messagebox.showinfo("INFORMACION","Esta interfaz de la aplicacion tiene la capacidad de registrar tus egresos,"
                                    " eliminar registros y filtrar segun tus consideraciones. Ademas, posee una tabla "
                                    "que permitira monitorear tus egresos")
    def acercade(self):
        tkinter.messagebox.showinfo("ACERCA DE","Esta aplicacion fue desarrollada por Rheyjach Arrieta Delgado con el objetivo"
                                    " de desarrollar una aplicacion funcional")
    def salir(self):
        self.salirAplicacion=tkinter.messagebox.askokcancel("SALIR","¿Desea salir de la aplicacion?")
        if self.salirAplicacion==True:
            self.ventana.destroy()
    # conexion a base de datos
    def guardar(self,egreso,origen,categoria,fecha):
        self.conexion=sqlite3.connect('datos.db')
        self.cursor=self.conexion.cursor()
        self.cursor.execute("INSERT INTO egresos(Egreso,Origen,Categoria,Fecha) VALUES(?,?,?,?)",(egreso,origen,categoria,fecha))
        self.conexion.commit()
        self.conexion.close()
        tkinter.messagebox.showinfo("EXITO","La informacion ha sido ingresada exitosamente")

    def cargar(self):
        #limpiar tabla
        for self.row in self.tabla.get_children():
            self.tabla.delete(self.row)
        
        #cargar datos
        self.conexion=sqlite3.connect('datos.db')
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT * FROM egresos")
        self.filas=self.cursor.fetchall()
        self.conexion.close()

        #ingresar datos a la tabla
        for self.fila in self.filas:
            self.tabla.insert("","end",values=self.fila)
    #funciones de botones
        #registrar
    def registrar(self):
        self.variableEgreso=self.entryEgreso.get().strip()
        self.variableOrigen=self.entryOrigen.get().strip()
        self.variableCategoria=self.listaDesplegable.get()
        if not self.variableEgreso or not self.variableOrigen or not self.variableCategoria:
            tkinter.messagebox.showinfo("AVISO","Los campos Egreso y Origen tienen que estar llenos, al igual que seleccionar un tipo de Categoria para poder registrar la informacion")
        else:
            try:
                self.variableEgreso=float(self.variableEgreso)
                if self.variableEgreso < 0:
                    tkinter.messagebox.showerror("ERROR","El campo Egreso solo permite valores numericos mayores o iguales a 0")
                else:
                    self.variableFecha=date.today().isoformat()
                    self.guardar(self.variableEgreso,self.variableOrigen,self.variableCategoria,self.variableFecha)
                    self.cargar()
            except:
                tkinter.messagebox.showerror("ERROR","El campo Egreso solo permite valores numericos mayores o iguales a 0")
    #filtros
    def funcionfiltroRegistro(self):
        self.variablefiltroRegistro=self.entryfiltroRegistro.get().strip()
        if not self.variablefiltroRegistro:
            tkinter.messagebox.showinfo("AVISO","El Campo Registro de la seccion de filtros tiene que estar lleno para poder hacer el filtro")
        else:
            try:
                self.variablefiltroRegistro=int(self.variablefiltroRegistro)
                if self.variablefiltroRegistro <=0:
                    tkinter.messagebox.showerror("ERROR","El campo Registro de la seccion de filtros tiene que ser mayor que 0")
                else:
                    for self.row in self.tabla.get_children():
                        self.tabla.delete(self.row)
                    
                    self.conexion=sqlite3.connect('datos.db')
                    self.cursor=self.conexion.cursor()
                    self.cursor.execute("SELECT * FROM egresos WHERE Registro=? ORDER BY Fecha DESC",(self.variablefiltroRegistro,))
                    self.filas=self.cursor.fetchall()
                    self.conexion.close()

                    for self.fila in self.filas:
                        self.tabla.insert("","end",values=self.fila)
            except:
                tkinter.messagebox.showerror("ERROR","El campo Registro de la seccion de filtros tiene que ser un valor numerico entero")
    def funcionfiltroEgreso(self):
        self.variablefiltroEgreso=self.entryfiltroEgreso.get().strip()
        if not self.variablefiltroEgreso:
            tkinter.messagebox.showinfo("AVISO","El Campo Egreso de la seccion de filtros tiene que estar lleno para poder hacer el filtro")
        else:
            try:
                self.variablefiltroEgreso=float(self.variablefiltroEgreso)
                if self.variablefiltroEgreso < 0:
                    tkinter.messagebox.showerror("ERROR","El campo Egreso de la seccion de filtros tiene que ser un valor numerico mayor o igual a 0")
                else:
                    for self.row in self.tabla.get_children():
                        self.tabla.delete(self.row)
                    
                    self.conexion=sqlite3.connect('datos.db')
                    self.cursor=self.conexion.cursor()
                    self.cursor.execute("SELECT * FROM egresos WHERE Egreso=? ORDER BY Fecha DESC",(self.variablefiltroEgreso,))
                    self.filas=self.cursor.fetchall()
                    self.conexion.close()

                    for self.fila in self.filas:
                        self.tabla.insert("","end",values=self.fila)
            except:
                tkinter.messagebox.showerror("ERROR","El campo Egreso de la seccion de filtros tiene que ser un valor numerico")
    def funcionfiltroOrigen(self):
        self.variablefiltroOrigen=self.entryfiltroOrigen.get().strip()
        if not self.variablefiltroOrigen:
            tkinter.messagebox.showinfo("AVISO","El campo Origen de la seccion de filtros tiene que estar lleno para poder hacer el filtro")
        else:
            for self.row in self.tabla.get_children():
                self.tabla.delete(self.row)
                    
            self.conexion=sqlite3.connect('datos.db')
            self.cursor=self.conexion.cursor()
            self.cursor.execute("SELECT * FROM egresos WHERE Origen=? ORDER BY Fecha DESC",(self.variablefiltroOrigen,))
            self.filas=self.cursor.fetchall()
            self.conexion.close()

            for self.fila in self.filas:
                self.tabla.insert("","end",values=self.fila)
    def funcionfiltroFecha(self):
        self.variablefiltroFecha=self.entryfiltroFecha.get().strip()
        if not self.variablefiltroFecha:
            tkinter.messagebox.showinfo("AVISO","El campo Fecha de la seccion de filtros tiene que estar lleno para poder hacer el filtro")
        else:
            for self.row in self.tabla.get_children():
                self.tabla.delete(self.row)
                    
            self.conexion=sqlite3.connect('datos.db')
            self.cursor=self.conexion.cursor()
            self.cursor.execute("SELECT * FROM egresos WHERE Fecha=? ORDER BY Fecha DESC",(self.variablefiltroFecha,))
            self.filas=self.cursor.fetchall()
            self.conexion.close()

            for self.fila in self.filas:
                self.tabla.insert("","end",values=self.fila)
    def funcionfiltroMes(self):
        self.variablefiltroMes=self.entryfiltroMes.get().strip()
        if not self.variablefiltroMes:
            tkinter.messagebox.showinfo("AVISO","El campo Mes de la seccion de filtros tiene que estar lleno para poder hacer el filtro")
        else:
            try:
                self.variablefiltroMes=int(self.variablefiltroMes)
                if self.variablefiltroMes < 1 or self.variablefiltroMes > 12:
                    tkinter.messagebox.showerror("ERROR","El campo Mes de la seccion de filtros tiene que ser un valor numerico entero entre 1 y 12")
                else:
                    self.variablefiltroMes=f"{self.variablefiltroMes:02}"
                    for self.row in self.tabla.get_children():
                        self.tabla.delete(self.row)
                            
                    self.conexion=sqlite3.connect('datos.db')
                    self.cursor=self.conexion.cursor()
                    self.cursor.execute("SELECT * FROM egresos WHERE STRFTIME('%m',Fecha)=? ORDER BY Fecha DESC",(self.variablefiltroMes,))
                    self.filas=self.cursor.fetchall()
                    self.conexion.close()

                    for self.fila in self.filas:
                        self.tabla.insert("","end",values=self.fila)
            except:
                tkinter.messagebox.showerror("ERROR","El campo Mes de la seccion de filtros tiene que ser un valor numerico entero entre 1 y 12")
    def funcionfiltroCategoria(self):
        self.variablefiltroCategoria=self.filtrolistaDesplegable.get()
        if not self.variablefiltroCategoria:
            tkinter.messagebox.showinfo("AVISO","Tiene que seleccionar una opcion para filtrar por Categoria")
        else:
            for self.row in self.tabla.get_children():
                self.tabla.delete(self.row)
                    
            self.conexion=sqlite3.connect('datos.db')
            self.cursor=self.conexion.cursor()
            self.cursor.execute("SELECT * FROM egresos WHERE Categoria=? ORDER BY Fecha DESC",(self.variablefiltroCategoria,))
            self.filas=self.cursor.fetchall()
            self.conexion.close()

            for self.fila in self.filas:
                self.tabla.insert("","end",values=self.fila)
    #eliminar
    def funcionEliminarregistro(self):
        self.variableEliminarregistro=self.entryeliminarRegistro.get().strip()
        if not self.variableEliminarregistro:
            tkinter.messagebox.showinfo("AVISO","El campo Registro de la seccion Eliminar tiene que estar lleno para poder eliminar algun registro")
        else:
            try:
                self.variableEliminarregistro=int(self.variableEliminarregistro)
                self.conexion=sqlite3.connect('datos.db')
                self.cursor=self.conexion.cursor()
                self.cursor.execute("SELECT Registro From egresos")
                self.registrosAlmacenados=self.cursor.fetchall()
                self.conexion.close()

                self.registrosDisponibles=[self.r[0] for self.r in self.registrosAlmacenados]
                if self.variableEliminarregistro not in self.registrosDisponibles:
                    tkinter.messagebox.showinfo("AVISO","El Registro ingresado no se encuentra almacenado")
                else:
                    self.conexion=sqlite3.connect('datos.db')
                    self.cursor=self.conexion.cursor()
                    self.cursor.execute("DELETE FROM egresos WHERE Registro=?",(self.variableEliminarregistro,))
                    self.conexion.commit()
                    self.conexion.close()
                    tkinter.messagebox.showinfo("EXITO",f"El Registro {self.variableEliminarregistro} fue eliminado correctamente")
                    self.cargar()
            except:
                tkinter.messagebox.showerror("ERROR","El campo Registro de la seccion Eliminar tiene que ser un valor numerico entero")
    def funcionTotalregistros(self):
        self.cargar()
        #inicio
    def inicio(self):
        from inicio import inicio
        self.ventana.destroy()
        inicio()
    #copiar valores de tabla
    def copiar_valor(self,evento):
        # Obtener el item seleccionado
        self.item = self.tabla.identify_row(evento.y)
        self.column = self.tabla.identify_column(evento.x)

        if self.item and self.column:
            self.column_index = int(self.column.replace("#", "")) - 1
            self.value = self.tabla.item(self.item)["values"][self.column_index]

            # Copiar al portapapeles
            self.ventana.clipboard_clear()
            self.ventana.clipboard_append(self.value)
            self.ventana.update()
            tkinter.messagebox.showinfo("COPIADO",f"Copiado al portapapeles: {self.value}")


# Modulos basicos utilizados
import tkinter
import tkinter.messagebox
import tkinter.ttk
import sqlite3
from os.path import abspath,join
import sys

# Clase de ejecución de la interfaz
class estadisticas:
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
        self.balanceFinanciero=tkinter.Label(self.ventana,text="Balance Financiero",font=("arial",15,"bold"),bg="#8085AC")
        self.balanceFinanciero.place(x=15,y=5)
        self.filtros=tkinter.Label(self.ventana,text="Filtros",font=("arial",15,"bold"),bg="#8085AC")
        self.filtros.place(x=15,y=270)
        self.Mes=tkinter.Label(self.ventana,text="Mes",font=("arial",13,"bold"),bg="#8085AC")
        self.Mes.place(x=190,y=300)
        self.Year=tkinter.Label(self.ventana,text="Año",font=("arial",13,"bold"),bg="#8085AC")
        self.Year.place(x=15,y=300)
        self.especialYear=tkinter.Label(self.ventana,text="Año",font=("arial",13,"bold"),bg="#8085AC")
        self.especialYear.place(x=405,y=280)
        self.especialMes=tkinter.Label(self.ventana,text="Mes",font=("arial",13,"bold"),bg="#8085AC")
        self.especialMes.place(x=470,y=280)
        self.graficos=tkinter.Label(self.ventana,text="Graficos",font=("arial",15,"bold"),bg="#8085AC")
        self.graficos.place(x=15,y=325)
        self.tipodeGrafica=tkinter.Label(self.ventana,text="Tipo de Grafico",font=("arial",13,"bold"),bg="#8085AC")
        self.tipodeGrafica.place(x=15,y=350)
        #entrys
        self.entryfiltroMes=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=6)
        self.entryfiltroMes.place(x=230,y=300)
        self.entryfiltroYear=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=6)
        self.entryfiltroYear.place(x=55,y=300)
        self.entryespecialMes=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=6)
        self.entryespecialMes.place(x=470,y=300)
        self.entryespecialYear=tkinter.Entry(self.ventana,font=("arial",13,"bold"),width=6)
        self.entryespecialYear.place(x=405,y=300)
        #lista desplegable
        self.listaDesplegable=tkinter.ttk.Combobox(self.ventana,state='readonly',values=["Grafico de Lineas (Mensual): Ingresos - Egresos","Grafico de Barras: Balance Mensual","Grafico Circular: Categorias - Ingresos (Historicos)","Grafico Circular: Categorias - Egresos (Historicos)"],font=("arial",9,"bold"),width=50)
        self.listaDesplegable.place(x=140,y=350)

        #botones
        self.botonfiltroYear=tkinter.Button(self.ventana,text="Filtrar",font=("arial",8,"bold"),width=6,height=1,command=self.funcionFiltroYear)
        self.botonfiltroYear.place(x=120,y=298)
        self.botonfiltroYear.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonfiltroMes=tkinter.Button(self.ventana,text="Filtrar",font=("arial",8,"bold"),width=6,height=1,command=self.funcionFiltroMes)
        self.botonfiltroMes.place(x=295,y=298)
        self.botonfiltroMes.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonfiltroEspecial=tkinter.Button(self.ventana,text="Filtrar",font=("arial",8,"bold"),width=6,height=1,command=self.funcionfiltroEspecial)
        self.botonfiltroEspecial.place(x=535,y=298)
        self.botonfiltroEspecial.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonmostrarDatos=tkinter.Button(self.ventana,text="Registros Totales",font=("arial",8,"bold"),width=13,height=1,command=self.cargar)
        self.botonmostrarDatos.place(x=395,y=15)
        self.botonmostrarDatos.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botonInicio=tkinter.Button(self.ventana,text="Inicio",font=("arial",8,"bold"),width=7,height=1,command=self.inicio)
        self.botonInicio.place(x=505,y=15)
        self.botonInicio.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)
        self.botongraficos=tkinter.Button(self.ventana,text="Mostrar",font=("arial",8,"bold"),width=6,height=1,command=self.funcionBarra)
        self.botongraficos.place(x=515,y=348)
        self.botongraficos.config(cursor="hand2",bg="#9C9594",activebackground="#9C9594",bd=2,borderwidth=3)

        #scroll
        self.scrollVertical=tkinter.Scrollbar(self.ventana,orient="vertical")
        self.scrollVertical.place(x=575,y=45,height=225)

        #tabla
        self.tabla=tkinter.ttk.Treeview(self.ventana,columns=("Año","Mes","Ingreso Mensual","Egreso Mensual","Balance"),yscrollcommand=self.scrollVertical.set)
        self.tabla.place(x=15,y=45)

            #encabezados
        self.tabla.heading("#1",text="Año")
        self.tabla.heading("#2",text="Mes")
        self.tabla.heading("#3",text="Ingreso Mensual")
        self.tabla.heading("#4",text="Egreso Mensual")
        self.tabla.heading("#5",text="Balance")
            #columnas
        self.tabla.column("#0",width=0,stretch=tkinter.NO)
        self.tabla.column("#1",width=110,anchor="center")
        self.tabla.column("#2",width=110,anchor="center")
        self.tabla.column("#3",width=110,anchor="center")
        self.tabla.column("#4",width=110,anchor="center")
        self.tabla.column("#5",width=110,anchor="center")

        #eventos de la tabla
        self.tabla.bind("<Button-1>", self.copiar_valor)

            #vinculacion scroll con la tabla
        self.scrollVertical.config(command=self.tabla.yview)

        #funciones basicas de base de datos
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
        tkinter.messagebox.showinfo("INFORMACION","Esta interfaz de la aplicacion contiene acumulados, graficos y filtros de tus"
                                    " ingresos, egresos y balance financiero que permitiran monitorear tus finanzas")
    def acercade(self):
        tkinter.messagebox.showinfo("ACERCA DE","Esta aplicacion fue desarrollada por Rheyjach Arrieta Delgado con el objetivo"
                                    " de desarrollar una aplicacion funcional")
    def salir(self):
        self.salirAplicacion=tkinter.messagebox.askokcancel("SALIR","¿Desea salir de la aplicacion?")
        if self.salirAplicacion==True:
            self.ventana.destroy()
    #conexion a base de datos
    def cargar(self):
        for self.row in self.tabla.get_children():
            self.tabla.delete(self.row)

        self.conexion=sqlite3.connect('datos.db')
        self.cursor=self.conexion.cursor()
        self.cursor.execute('''SELECT año, CAST(mes AS INTEGER) AS mes, SUM(total_ingreso) AS Total_Ingreso, SUM(total_egreso) AS Total_Egreso, SUM(total_ingreso) - SUM(total_egreso) AS Balance 
                            FROM (SELECT strftime('%Y', Fecha) AS año, strftime('%m', Fecha) AS mes, SUM(ingreso) AS total_ingreso, 0 AS total_egreso
                             FROM ingresos GROUP BY strftime('%Y', Fecha), strftime('%m', Fecha) UNION ALL SELECT strftime('%Y', Fecha) AS año, strftime('%m', Fecha) AS mes, 0 AS total_ingreso, SUM(egreso) AS total_egreso
                             FROM egresos GROUP BY strftime('%Y', Fecha), strftime('%m', Fecha)) AS union_tablas GROUP BY año, mes ORDER BY año, mes''')
        self.filas=self.cursor.fetchall()
        self.conexion.close()

        for self.fila in self.filas:
            self.tabla.insert("","end",values=self.fila)

    #funciones de botones
        #inicio
    def inicio(self):
        from inicio import inicio
        self.ventana.destroy()
        inicio()
        #filtros
    def funcionFiltroYear(self):
        self.variablefiltroYear=self.entryfiltroYear.get().strip()
        if not self.variablefiltroYear:
            tkinter.messagebox.showinfo("AVISO","El campo Año de la seccion de filtros tiene que estar lleno para poder hacer el filtro")
        else:
            try:
                self.variablefiltroYear=int(self.variablefiltroYear)
                if self.variablefiltroYear < 2025:
                    tkinter.messagebox.showinfo("AVISO","El campo Año de la seccion de filtros tiene que ser mayor o igual a 2025, debido a que fue el año en el que se empezo a usar este programa")
                else:
                    for self.row in self.tabla.get_children():
                        self.tabla.delete(self.row)

                    self.conexion=sqlite3.connect('datos.db')
                    self.cursor=self.conexion.cursor()
                    self.cursor.execute('''SELECT * FROM (SELECT año, CAST(mes AS INTEGER) AS mes, SUM(total_ingreso) AS Total_Ingreso, SUM(total_egreso) AS Total_Egreso, SUM(total_ingreso) - SUM(total_egreso) AS Balance 
                            FROM (SELECT strftime('%Y', Fecha) AS año, strftime('%m', Fecha) AS mes, SUM(ingreso) AS total_ingreso, 0 AS total_egreso
                             FROM ingresos GROUP BY strftime('%Y', Fecha), strftime('%m', Fecha) UNION ALL SELECT strftime('%Y', Fecha) AS año, strftime('%m', Fecha) AS mes, 0 AS total_ingreso, SUM(egreso) AS total_egreso
                             FROM egresos GROUP BY strftime('%Y', Fecha), strftime('%m', Fecha)) AS union_tablas GROUP BY año, mes ) AS temporal WHERE año=? ORDER BY año DESC, mes DESC''',(str(self.variablefiltroYear),))
                    self.filas=self.cursor.fetchall()
                    self.conexion.close()

                    for self.fila in self.filas:
                        self.tabla.insert("","end",values=self.fila)
            except:
                tkinter.messagebox.showerror("ERROR","El campo Año de la seccion de filtros tiene que ser un valor numerico entero")
    def funcionFiltroMes(self):
        self.variablefiltroMes=self.entryfiltroMes.get().strip()
        if not self.variablefiltroMes:
            tkinter.messagebox.showinfo("AVISO","El campo Mes de la seccion de filtros tiene que estar lleno para poder hacer el filtro")
        else:
            try:
                self.variablefiltroMes=int(self.variablefiltroMes)
                if self.variablefiltroMes < 1 or self.variablefiltroMes > 12:
                    tkinter.messagebox.showinfo("AVISO","El campo Mes de la seccion de filtros tiene que ser un valor numerico entero entre 1 y 12")
                else:
                    self.variablefiltroMes=f"{self.variablefiltroMes:02}"
                    for self.row in self.tabla.get_children():
                        self.tabla.delete(self.row)

                    self.conexion=sqlite3.connect('datos.db')
                    self.cursor=self.conexion.cursor()
                    self.cursor.execute('''SELECT * FROM (SELECT año, CAST(mes AS INTEGER) AS mes, SUM(total_ingreso) AS Total_Ingreso, SUM(total_egreso) AS Total_Egreso, SUM(total_ingreso) - SUM(total_egreso) AS Balance 
                            FROM (SELECT strftime('%Y', Fecha) AS año, strftime('%m', Fecha) AS mes, SUM(ingreso) AS total_ingreso, 0 AS total_egreso
                             FROM ingresos GROUP BY strftime('%Y', Fecha), strftime('%m', Fecha) UNION ALL SELECT strftime('%Y', Fecha) AS año, strftime('%m', Fecha) AS mes, 0 AS total_ingreso, SUM(egreso) AS total_egreso
                             FROM egresos GROUP BY strftime('%Y', Fecha), strftime('%m', Fecha)) AS union_tablas GROUP BY año, mes ) AS temporal WHERE mes=? ORDER BY año DESC, mes DESC''',(self.variablefiltroMes,))
                    self.filas=self.cursor.fetchall()
                    self.conexion.close()

                    for self.fila in self.filas:
                        self.tabla.insert("","end",values=self.fila)
            except:
                tkinter.messagebox.showerror("ERROR","El campo Mes de la seccion de filtros tiene que ser un valor numerico entero entre 1 y 12")
    def funcionfiltroEspecial(self):
        self.variablefiltroEspecialyear=self.entryespecialYear.get().strip()
        self.variablefiltroEspecialmes=self.entryespecialMes.get().strip()
        if not self.variablefiltroEspecialmes or not self.variablefiltroEspecialyear:
            tkinter.messagebox.showinfo("AVISO","Para hacer el filtro combinado se necesita que el Campo Año y Mes esten llenos")
        else:
            try:
                self.variablefiltroEspecialyear=int(self.variablefiltroEspecialyear)
                self.variablefiltroEspecialmes=int(self.variablefiltroEspecialmes)
                if self.variablefiltroEspecialmes < 1 or self.variablefiltroEspecialmes > 12 or self.variablefiltroEspecialyear < 2025:
                    tkinter.messagebox.showinfo("AVISO","El campo Año tiene que ser mayor o igual a 2025 y el campo Mes tiene que estar entre 1 y 12")
                else:
                    self.variablefiltroEspecialyear=str(self.variablefiltroEspecialyear)
                    self.variablefiltroEspecialmes=f"{self.variablefiltroEspecialmes:02}"
                    for self.row in self.tabla.get_children():
                        self.tabla.delete(self.row)
                    
                    self.conexion=sqlite3.connect('datos.db')
                    self.cursor=self.conexion.cursor()
                    self.cursor.execute('''SELECT * FROM (SELECT año, CAST(mes AS INTEGER) AS mes, SUM(total_ingreso) AS Total_Ingreso, SUM(total_egreso) AS Total_Egreso, SUM(total_ingreso) - SUM(total_egreso) AS Balance 
                            FROM (SELECT strftime('%Y', Fecha) AS año, strftime('%m', Fecha) AS mes, SUM(ingreso) AS total_ingreso, 0 AS total_egreso
                             FROM ingresos GROUP BY strftime('%Y', Fecha), strftime('%m', Fecha) UNION ALL SELECT strftime('%Y', Fecha) AS año, strftime('%m', Fecha) AS mes, 0 AS total_ingreso, SUM(egreso) AS total_egreso
                             FROM egresos GROUP BY strftime('%Y', Fecha), strftime('%m', Fecha)) AS union_tablas GROUP BY año, mes ) AS temporal WHERE año=? and mes=? ORDER BY año DESC, mes DESC''',(self.variablefiltroEspecialyear,self.variablefiltroEspecialmes))
                    self.filas=self.cursor.fetchall()
                    self.conexion.close()

                    for self.fila in self.filas:
                        self.tabla.insert("","end",values=self.fila)
            except:
                tkinter.messagebox.showerror("ERROR","Los Campos Año y Mes en el filtro combinado tienen que ser valores numericos enteros")
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
    # Graficos de la tabla
    def funcionGraficos(self):
        self.variableLista=self.listaDesplegable.get()
        if not self.variableLista:
            self.progreso.stop()
            self.progreso.destroy()
            tkinter.messagebox.showinfo("AVISO","Tiene que seleccionar un tipo de grafico para poder mostrarlo en la interfaz")
        else:
            from matplotlib.figure import Figure
            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
            self.progreso.stop()
            self.progreso.destroy()
            tkinter.messagebox.showinfo("GRAFICO ELABORADO","Presione Aceptar para ver el grafico seleccionado")
            if self.variableLista == 'Grafico de Lineas (Mensual): Ingresos - Egresos' or self.variableLista=='Grafico de Barras: Balance Mensual':
                self.conexion=sqlite3.connect('datos.db')
                self.cursor=self.conexion.cursor()
                self.cursor.execute('''SELECT año, CAST(mes AS INTEGER) AS mes, SUM(total_ingreso) AS Total_Ingreso, SUM(total_egreso) AS Total_Egreso, SUM(total_ingreso) - SUM(total_egreso) AS Balance 
                            FROM (SELECT strftime('%Y', Fecha) AS año, strftime('%m', Fecha) AS mes, SUM(ingreso) AS total_ingreso, 0 AS total_egreso
                             FROM ingresos GROUP BY strftime('%Y', Fecha), strftime('%m', Fecha) UNION ALL SELECT strftime('%Y', Fecha) AS año, strftime('%m', Fecha) AS mes, 0 AS total_ingreso, SUM(egreso) AS total_egreso
                             FROM egresos GROUP BY strftime('%Y', Fecha), strftime('%m', Fecha)) AS union_tablas GROUP BY año, mes ORDER BY año, mes''')
                self.filas=self.cursor.fetchall()
                self.conexion.close()
                self.datosYear=[self.ye[0] for self.ye in self.filas]
                self.datosMes=[self.m[1] for self.m in self.filas]
                self.etiquetasTiempo=[f"{a}-{m}" for a,m in zip(self.datosYear,self.datosMes)]
                self.datosIngresos=[self.i[2] for self.i in self.filas]
                self.datosEgresos=[self.e[3] for self.e in self.filas]
                self.datosBalance=[self.b[4] for self.b in self.filas]
                if self.variableLista=='Grafico de Lineas (Mensual): Ingresos - Egresos':
                    if hasattr(self,'canvas'):
                        self.canvas.get_tk_widget().destroy()
                    self.figuraLineas= Figure(figsize=(5,4),dpi=55)
                    self.ax=self.figuraLineas.add_subplot(111)
                    self.ax.plot(self.etiquetasTiempo, self.datosIngresos, label='Ingresos', marker='o', linestyle='-', color='green')
                    self.ax.plot(self.etiquetasTiempo, self.datosEgresos, label='Egresos', marker='o', linestyle='-', color='red')
                    self.ax.set_xlabel('Año-Mes')
                    self.ax.set_ylabel('Valor ($)')
                    self.ax.tick_params(axis='x', rotation=90)
                    self.ax.legend()
                    self.figuraLineas.tight_layout()

                    self.canvas = FigureCanvasTkAgg(self.figuraLineas,self.ventana)
                    self.canvas.get_tk_widget().place(x=15,y=395,width=555,height=223)
                    self.canvas.draw()
                else:
                    if hasattr(self,'canvas'):
                        self.canvas.get_tk_widget().destroy()
                    self.figuraBarras=Figure(figsize=(5,4),dpi=55)
                    self.ax=self.figuraBarras.add_subplot(111)
                    self.ax.bar(self.etiquetasTiempo,self.datosBalance,color='skyblue')
                    self.ax.set_xlabel('Año-Mes')
                    self.ax.set_ylabel('Valor ($)')
                    self.ax.tick_params(axis='x', rotation=90)
                    self.figuraBarras.tight_layout()

                    self.canvas = FigureCanvasTkAgg(self.figuraBarras,self.ventana)
                    self.canvas.get_tk_widget().place(x=15,y=395,width=555,height=223)
                    self.canvas.draw()
            else:
                self.conexion=sqlite3.connect('datos.db')
                self.cursor=self.conexion.cursor()
                self.cursor.execute("SELECT Categoria,SUM(Ingreso) FROM ingresos GROUP BY Categoria")
                self.filasIngresos=self.cursor.fetchall()
                self.cursor.execute("SELECT Categoria,SUM(Egreso) FROM egresos GROUP BY Categoria")
                self.filasEgresos=self.cursor.fetchall()
                self.conexion.close()
                self.datosCategoria_ingresos=[self.cai[0] for self.cai in self.filasIngresos]
                self.datosCategoria_egresos=[self.cae[0] for self.cae in self.filasEgresos]
                self.datosIngresos_categoria=[self.ing[1] for self.ing in self.filasIngresos]
                self.datosEgresos_categoria=[self.egr[1] for self.egr in self.filasEgresos]
                if self.variableLista=='Grafico Circular: Categorias - Ingresos (Historicos)':
                    if hasattr(self,'canvas'):
                        self.canvas.get_tk_widget().destroy()
                    self.figuraCircularingresos=Figure(figsize=(5,4),dpi=55)
                    self.ax=self.figuraCircularingresos.add_subplot(111)
                    self.ax.pie(self.datosIngresos_categoria,labels=self.datosCategoria_ingresos,startangle=90,autopct='%1.1f%%')
                    self.figuraCircularingresos.tight_layout()

                    self.canvas = FigureCanvasTkAgg(self.figuraCircularingresos,self.ventana)
                    self.canvas.get_tk_widget().place(x=15,y=395,width=555,height=223)
                    self.canvas.draw()
                else:
                    if hasattr(self,'canvas'):
                        self.canvas.get_tk_widget().destroy()
                    self.figuraCircularegresos=Figure(figsize=(5,4),dpi=55)
                    self.ax=self.figuraCircularegresos.add_subplot(111)
                    self.ax.pie(self.datosEgresos_categoria,labels=self.datosCategoria_egresos,startangle=90,autopct='%1.1f%%')
                    self.figuraCircularegresos.tight_layout()

                    self.canvas = FigureCanvasTkAgg(self.figuraCircularegresos,self.ventana)
                    self.canvas.get_tk_widget().place(x=15,y=395,width=555,height=223)
                    self.canvas.draw()
    # barra de interactividad
    def funcionBarra(self):
        self.progreso=tkinter.ttk.Progressbar(self.ventana, length=300, mode='indeterminate')
        self.progreso.place(x=170,y=370)
        self.progreso.start(5)
        self.ventana.after(2000,self.funcionGraficos)






        


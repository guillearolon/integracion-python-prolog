import tkinter as tk
import tkinter.simpledialog as simpledialog
import tkinter.filedialog as filedialog
import tkinter.font as font
import tkinter.ttk as ttk

################## EJEMPLOS DE USOS EN TKINTER ##################

# Widgets básicos:
tk.Button(text="Click Me", command='callback_function')  # Botón interactivo.
tk.Label(text="Hello, World!")  # Etiqueta para mostrar texto o imágenes.
tk.Entry()  # Campo de entrada de una sola línea para texto.
tk.Text()  # Área de texto multi-línea editable.
tk.Checkbutton(text="Check me!")  # Botón de verificación.
tk.Radiobutton(text="Option 1")  # Botón de opción.
tk.delete('0', 'end') # Elimina desde el principio al final del Entry
tk.destroy() # Cierra la sesión de la ventana tk

# Contenedores:
tk.Frame()  # Marco contenedor para organizar y agrupar widgets.
tk.LabelFrame(text="Group")  # Marco contenedor con un título.

# Otros widgets de entrada:
tk.Scale(from_=0, to=100)  # Control deslizante.
tk.Spinbox(from_=0, to=100)  # Cuadro de selección con flechas para aumentar o disminuir valores.
tk.Listbox()  # Lista desplegable o de selección múltiple.

# Widgets de selección:
tk.OptionMenu()  # Menú desplegable de selección.

# Contenedores especiales:
tk.Canvas()  # Área para dibujar gráficos o figuras.
tk.PanedWindow()  # Ventana dividida en paneles ajustables.

# Otros elementos:
tk.Menu()  # Barra de menú.
tk.Scrollbar()  # Barra de desplazamiento.
tk.Message()  # Cuadro de mensaje para mostrar texto en varias líneas.

# Diálogos y ventanas emergentes:
tk.Toplevel()  # Ventana emergente.
simpledialog.askstring("Title", "Please enter your name:")  # Diálogo simple para solicitar entrada de texto.
filedialog.askopenfilename()  # Cuadro de diálogo para abrir archivos.

# Manejo de eventos:
tk.bind()  # Método para enlazar eventos con funciones. Se utiliza con un widget específico.
tk.after()  # Método para ejecutar funciones después de un intervalo de tiempo.

# Estilos y apariencia:
tk.Font()  # Módulo para definir y manipular estilos de fuente.
ttk.Style()  # Módulo que proporciona widgets temáticos con una apariencia más moderna y consistente.
tk.iconbitmap('icono.ico')  # No es un método, es una función para establecer el icono de la ventana.
tk.config(bg="lightblue")  # No es un método, es una función para configurar el color de fondo de la ventana.

# Gestión de geometría:
tk.pack()  # Método para organizar widgets utilizando un algoritmo de empaquetado.
tk.grid()  # Método para organizar widgets en una cuadrícula.
tk.place()  # Método para colocar widgets en una posición específica mediante coordenadas.
tk.minsize(400, 300)  # No es un método, es una función para configurar el tamaño mínimo de la ventana.
tk.maxsize(800, 600)  # No es un método, es una función para configurar el tamaño máximo de la ventana.
tk.geometry('+x+y') # Acomodar la ventana en el eje x + y
tk.geometry('x,y') # Tamaño de la ventana

# Manipulación de imágenes:
tk.PhotoImage()  # Clase para manejar imágenes GIF y PGM/PPM.

# Iniciar el bucle principal de eventos de Tkinter:
tk.mainloop()  # Método para iniciar el bucle principal de eventos de Tkinter.

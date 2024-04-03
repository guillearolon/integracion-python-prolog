import tkinter as tk

root = tk.Tk()

root.title("Prolog")

#x,y
root.geometry('+550+300')
root.geometry('300x100')

contenido = tk.Label(root, text="Consultas a Prolog", font=('Arial', 15 ))
contenido.pack()

def envio():
    entradas = entrada.get()
    print(entradas)
    entrada.delete(0, 'end') #Borro el campo entry post envio

entrada = tk.Entry(root, width=30)
entrada.pack()

boton = tk.Button(root, text="Enviar", command=envio)
boton.pack()

boton = tk.Button(root, text="Cerrar", command=root.destroy)
boton.pack()

root.mainloop()
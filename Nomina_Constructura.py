Nombre = "Santiago Villa Ramos"

import tkinter as tk
from tkinter import messagebox

# Diccionario con salarios por día según el cargo
salarios = {
    "Ingeniero": 200000,
    "Arquitecto": 180000,
    "Maestro de obra": 120000,
    "Obrero": 80000
}

empleados = []

# Función para calcular pago
def calcular_pago():
    nombre = entry_nombre.get()
    cargo = cargo_var.get()
    dias = entry_dias.get()

    if nombre == "" or dias == "":
        messagebox.showwarning("Error", "Ingrese todos los datos")
        return

    dias = int(dias)
    salario_dia = salarios[cargo]
    total = dias * salario_dia

    label_resultado.config(text=f"Total a pagar: ${total}")
    return total

# Función para guardar datos
def guardar():
    nombre = entry_nombre.get()
    cargo = cargo_var.get()
    dias = int(entry_dias.get())
    total = calcular_pago()

    empleados.append((nombre, cargo, dias, total))
    messagebox.showinfo("Guardado", "Empleado guardado correctamente")

# Función para mostrar reporte
def reporte():
    ventana_reporte = tk.Toplevel()
    ventana_reporte.title("Reporte de Nómina")

    texto = tk.Text(ventana_reporte, width=60, height=15)
    texto.pack()

    texto.insert(tk.END, "REPORTE DE NÓMINA\n\n")

    for emp in empleados:
        texto.insert(tk.END, f"Nombre: {emp[0]}\n")
        texto.insert(tk.END, f"Cargo: {emp[1]}\n")
        texto.insert(tk.END, f"Días trabajados: {emp[2]}\n")
        texto.insert(tk.END, f"Total a pagar: ${emp[3]}\n")
        texto.insert(tk.END, "-----------------------------\n")

# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Nómina - Constructora Mejor")
ventana.geometry("400x350")

tk.Label(ventana, text="Nombre del empleado").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Cargo").pack()
cargo_var = tk.StringVar()
cargo_var.set("Ingeniero")

menu_cargo = tk.OptionMenu(ventana, cargo_var, *salarios.keys())
menu_cargo.pack()

tk.Label(ventana, text="Días trabajados").pack()
entry_dias = tk.Entry(ventana)
entry_dias.pack()

tk.Button(ventana, text="Calcular Pago", command=calcular_pago).pack(pady=5)
tk.Button(ventana, text="Guardar", command=guardar).pack(pady=5)
tk.Button(ventana, text="Mostrar Reporte", command=reporte).pack(pady=5)

label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

ventana.mainloop()
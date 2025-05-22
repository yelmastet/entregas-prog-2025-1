"""
Calculadora de electrónica:
Hacer un programa que haga calcule el valor de componentes electrónicos.

Este programa de interfaz gráfica le pide al usuario
ingresar un código o una serie de colores para luego
mostrar el valor del componente según el código o colores brindados
(código para los condensadores y colores para las resistencias).

Autor: David Torres <dstorresr@academia.usbbog.edu.co>

Fecha: 2025-05-22
"""

import tkinter as tk
from tkinter import ttk, messagebox

# Tabla de colores para resistencias (valor, multiplicador, tolerancia)
colores = {
    "Negro": (0, 1, None),
    "Marrón": (1, 10, "±1%"),
    "Rojo": (2, 100, "±2%"),
    "Naranja": (3, 1_000, None),
    "Amarillo": (4, 10_000, None),
    "Verde": (5, 100_000, "±0.5%"),
    "Azul": (6, 1_000_000, "±0.25%"),
    "Violeta": (7, 10_000_000, "±0.1%"),
    "Gris": (8, 100_000_000, "±0.05%"),
    "Blanco": (9, 1_000_000_000, None),
    "Dorado": (None, 0.1, "±5%"),
    "Plateado": (None, 0.01, "±10%")
}

def interpretar_condensador(codigo: str) -> str:
    """
    Convierte un código numérico de condensador (3 cifras) a su valor en pF, nF o µF.

    Args:
        codigo (str): Código de 3 cifras, como '104' o '472'

    Returns:
        str: Representación legible del valor (ej: '100 nF (100000 pF)')
    """
    if not codigo.isdigit() or len(codigo) < 2:
        return "Código inválido. Debe tener al menos 2 cifras."

    try:
        sig = int(codigo[:-1])
        mult = int(codigo[-1])
        valor_pf = sig * (10 ** mult)

        if valor_pf >= 1_000_000:
            return f"{valor_pf/1_000_000:.2f} µF ({valor_pf} pF)"
        elif valor_pf >= 1_000:
            return f"{valor_pf/1_000:.2f} nF ({valor_pf} pF)"
        else:
            return f"{valor_pf} pF"
    except Exception:
        return "Error al interpretar el código."

def interpretar_resistencia(b1: str, b2: str, b3: str, tolerancia: str) -> str:
    """
    Calcula el valor de una resistencia de 4 bandas a partir de colores.

    Args:
        b1, b2, b3, tolerancia (str): Colores seleccionados

    Returns:
        str: Valor de la resistencia con tolerancia
    """
    try:
        d1 = colores[b1][0]
        d2 = colores[b2][0]
        mult = colores[b3][1]
        tol = colores[tolerancia][2]

        if None in (d1, d2) or mult is None:
            return "Color inválido para dígitos o multiplicador."

        valor = (d1 * 10 + d2) * mult

        if valor >= 1_000_000:
            valor_str = f"{valor/1_000_000:.2f} MΩ"
        elif valor >= 1_000:
            valor_str = f"{valor/1_000:.2f} kΩ"
        else:
            valor_str = f"{valor:.2f} Ω"

        return f"{valor_str} {tol if tol else ''}"
    except Exception:
        return "Error al interpretar los colores."

# Interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Identificador de Componentes")
ventana.geometry("450x400")
ventana.resizable(False, False)

# Sección: Condensadores
frame_cond = tk.LabelFrame(ventana, text="Condensadores", padx=10, pady=10)
frame_cond.pack(padx=10, pady=10, fill="x")

tk.Label(frame_cond, text="Código (ej. 104, 472):").pack()
entrada_codigo = tk.Entry(frame_cond, font=("Arial", 12))
entrada_codigo.pack(pady=5)

resultado_cond = tk.Label(frame_cond, text="", fg="blue", font=("Arial", 12))
resultado_cond.pack()

def calcular_cond():
    codigo = entrada_codigo.get().strip()
    resultado_cond.config(text=interpretar_condensador(codigo))

tk.Button(frame_cond, text="Calcular valor", command=calcular_cond).pack(pady=5)

# Sección: Resistencias
frame_res = tk.LabelFrame(ventana, text="Resistencias (4 bandas)", padx=10, pady=10)
frame_res.pack(padx=10, pady=10, fill="x")

tk.Label(frame_res, text="Selecciona los colores:").pack()

colores_lista = list(colores.keys())

cmb_b1 = ttk.Combobox(frame_res, values=colores_lista, state="readonly")
cmb_b2 = ttk.Combobox(frame_res, values=colores_lista, state="readonly")
cmb_b3 = ttk.Combobox(frame_res, values=colores_lista, state="readonly")
cmb_tol = ttk.Combobox(frame_res, values=colores_lista, state="readonly")

cmb_b1.set("Marrón")
cmb_b2.set("Negro")
cmb_b3.set("Rojo")
cmb_tol.set("Dorado")

cmb_b1.pack(padx=2, pady=2)
cmb_b2.pack(padx=2, pady=2)
cmb_b3.pack(padx=2, pady=2)
cmb_tol.pack(padx=2, pady=2)

resultado_res = tk.Label(frame_res, text="", fg="green", font=("Arial", 12))
resultado_res.pack()

def calcular_resistencia():
    r = interpretar_resistencia(cmb_b1.get(), cmb_b2.get(), cmb_b3.get(), cmb_tol.get())
    resultado_res.config(text=r)

tk.Button(frame_res, text="Calcular resistencia", command=calcular_resistencia).pack(pady=5)

# Menú de ayuda
def mostrar_ayuda():
    messagebox.showinfo("Ayuda", 
    "Condensadores:\nIntroduce el código de 3 cifras (ej. 104 → 100nF).\n\n"
    "Resistencias:\nSelecciona los colores en orden (4 bandas) para calcular el valor.")

barra = tk.Menu(ventana)
ayuda = tk.Menu(barra, tearoff=0)
ayuda.add_command(label="¿Cómo usar?", command=mostrar_ayuda)
barra.add_cascade(label="Ayuda", menu=ayuda)
ventana.config(menu=barra)

# Ejecutar la app
ventana.mainloop()

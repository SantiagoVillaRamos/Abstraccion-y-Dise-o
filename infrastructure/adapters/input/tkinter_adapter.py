"""
Adaptador de ENTRADA: TkinterAdapter
Implementa la interfaz gráfica usando Tkinter.
Solo conoce el NominaServicePort (puerto de entrada), nunca la implementación
concreta del servicio ni los detalles del repositorio o del reporte.
"""
import tkinter as tk
from tkinter import messagebox

from domain.entities.cargo import Cargo
from domain.ports.input.nomina_service_port import NominaServicePort


class TkinterAdapter:
    """
    Adaptador de entrada (Driving Adapter) que implementa la UI con Tkinter.
    Traduce las acciones del usuario en llamadas al puerto de entrada.
    No contiene lógica de negocio.
    """

    def __init__(self, servicio: NominaServicePort) -> None:
        """
        Args:
            servicio: Puerto de entrada que expone los casos de uso.
        """
        self._servicio = servicio
        self._ventana = tk.Tk()
        self._construir_ui()

    # ------------------------------------------------------------------ #
    # Construcción de la interfaz
    # ------------------------------------------------------------------ #

    def _construir_ui(self) -> None:
        """Configura y construye todos los widgets de la ventana principal."""
        v = self._ventana
        v.title("Sistema de Nómina - Constructora Mejor")
        v.geometry("420x400")
        v.resizable(False, False)
        v.configure(bg="#1e1e2e")

        estilo_label = {"bg": "#1e1e2e", "fg": "#cdd6f4", "font": ("Inter", 10)}
        estilo_entry = {"bg": "#313244", "fg": "#cdd6f4", "insertbackground": "#cdd6f4",
                        "relief": "flat", "font": ("Inter", 10)}
        estilo_btn = {"bg": "#89b4fa", "fg": "#1e1e2e", "activebackground": "#74c7ec",
                      "relief": "flat", "font": ("Inter", 10, "bold"), "cursor": "hand2",
                      "padx": 10, "pady": 5}

        # Título
        tk.Label(v, text="🏗 Sistema de Nómina", bg="#1e1e2e",
                 fg="#89b4fa", font=("Inter", 14, "bold")).pack(pady=(20, 5))
        tk.Label(v, text="Constructora Mejor", **estilo_label).pack(pady=(0, 15))

        # Nombre
        tk.Label(v, text="Nombre del empleado", **estilo_label).pack(anchor="w", padx=30)
        self._entry_nombre = tk.Entry(v, width=40, **estilo_entry)
        self._entry_nombre.pack(padx=30, pady=(2, 10), ipady=4)

        # Cargo
        tk.Label(v, text="Cargo", **estilo_label).pack(anchor="w", padx=30)
        self._cargo_var = tk.StringVar(value=Cargo.INGENIERO.descripcion)
        menu_cargo = tk.OptionMenu(v, self._cargo_var, *Cargo.listar_descripciones())
        menu_cargo.config(bg="#313244", fg="#cdd6f4", activebackground="#45475a",
                          relief="flat", font=("Inter", 10), width=33)
        menu_cargo.pack(padx=30, pady=(2, 10), anchor="w")

        # Días trabajados
        tk.Label(v, text="Días trabajados", **estilo_label).pack(anchor="w", padx=30)
        self._entry_dias = tk.Entry(v, width=40, **estilo_entry)
        self._entry_dias.pack(padx=30, pady=(2, 15), ipady=4)

        # Botones
        frame_botones = tk.Frame(v, bg="#1e1e2e")
        frame_botones.pack()
        tk.Button(frame_botones, text="💰 Calcular Pago",
                  command=self._on_calcular, **estilo_btn).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="💾 Guardar",
                  command=self._on_guardar, **estilo_btn).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="📄 Reporte",
                  command=self._on_reporte, **estilo_btn).grid(row=0, column=2, padx=5)

        # Resultado
        self._label_resultado = tk.Label(v, text="", bg="#1e1e2e",
                                         fg="#a6e3a1", font=("Inter", 11, "bold"))
        self._label_resultado.pack(pady=15)

    # ------------------------------------------------------------------ #
    # Manejadores de eventos (llaman al puerto de entrada)
    # ------------------------------------------------------------------ #

    def _leer_inputs(self) -> tuple[str, str, int]:
        """Lee y valida los campos del formulario."""
        nombre = self._entry_nombre.get().strip()
        cargo = self._cargo_var.get()
        dias_str = self._entry_dias.get().strip()

        if not nombre or not dias_str:
            raise ValueError("Todos los campos son obligatorios.")

        if not dias_str.isdigit() or int(dias_str) <= 0:
            raise ValueError("Los días trabajados deben ser un número entero positivo.")

        return nombre, cargo, int(dias_str)

    def _on_calcular(self) -> None:
        """Llama al caso de uso calcular_pago a través del puerto de entrada."""
        try:
            nombre, cargo, dias = self._leer_inputs()
            total = self._servicio.calcular_pago(nombre, cargo, dias)
            self._label_resultado.config(
                text=f"Total a pagar: ${total:,}", fg="#a6e3a1"
            )
        except ValueError as e:
            messagebox.showwarning("Datos inválidos", str(e))

    def _on_guardar(self) -> None:
        """Llama al caso de uso registrar_empleado a través del puerto de entrada."""
        try:
            nombre, cargo, dias = self._leer_inputs()
            empleado = self._servicio.registrar_empleado(nombre, cargo, dias)
            self._label_resultado.config(
                text=f"✅ Guardado: {empleado.nombre} — ${empleado.calcular_pago():,}",
                fg="#a6e3a1"
            )
            self._entry_nombre.delete(0, tk.END)
            self._entry_dias.delete(0, tk.END)
        except ValueError as e:
            messagebox.showwarning("Datos inválidos", str(e))

    def _on_reporte(self) -> None:
        """Llama al caso de uso generar_reporte y muestra el resultado en una ventana."""
        mensaje = self._servicio.generar_reporte()

        ventana_reporte = tk.Toplevel(self._ventana)
        ventana_reporte.title("Reporte de Nómina")
        ventana_reporte.configure(bg="#1e1e2e")
        ventana_reporte.geometry("520x420")

        frame = tk.Frame(ventana_reporte, bg="#1e1e2e")
        frame.pack(fill="both", expand=True, padx=15, pady=15)

        tk.Label(frame, text="📋 Reporte de Nómina", bg="#1e1e2e",
                 fg="#89b4fa", font=("Inter", 12, "bold")).pack(pady=(0, 10))

        # Empleados
        empleados = self._servicio.obtener_todos_los_empleados()
        if not empleados:
            tk.Label(frame, text="No hay empleados registrados.", bg="#1e1e2e",
                     fg="#f38ba8", font=("Inter", 10)).pack()
        else:
            texto = tk.Text(frame, bg="#313244", fg="#cdd6f4", font=("Courier", 9),
                            relief="flat", wrap="none")
            scroll = tk.Scrollbar(frame, command=texto.yview)
            texto.configure(yscrollcommand=scroll.set)
            scroll.pack(side="right", fill="y")
            texto.pack(fill="both", expand=True)

            for emp in empleados:
                texto.insert(tk.END, f"{'─'*44}\n")
                texto.insert(tk.END, f"  Nombre  : {emp.nombre}\n")
                texto.insert(tk.END, f"  Cargo   : {emp.cargo.descripcion}\n")
                texto.insert(tk.END, f"  Días    : {emp.dias_trabajados}\n")
                texto.insert(tk.END, f"  Total   : ${emp.calcular_pago():,}\n")

            total = sum(e.calcular_pago() for e in empleados)
            texto.insert(tk.END, f"{'═'*44}\n")
            texto.insert(tk.END, f"  TOTAL NÓMINA : ${total:,}\n")
            texto.config(state="disabled")

        # Notificación del archivo exportado
        tk.Label(frame, text=mensaje, bg="#1e1e2e", fg="#a6e3a1",
                 font=("Inter", 8), wraplength=480, justify="left").pack(pady=(10, 0))

    # ------------------------------------------------------------------ #
    # Ejecución
    # ------------------------------------------------------------------ #

    def ejecutar(self) -> None:
        """Inicia el loop principal de la interfaz gráfica."""
        self._ventana.mainloop()

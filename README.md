# Sistema de Nómina - Constructora Mejor

## 📋 Descripción

Sistema de gestión de nómina para constructoras desarrollado en Python usando **Tkinter**. Permite registrar empleados, calcular sus salarios según el cargo y días trabajados, y generar reportes de nómina.

## ✨ Características

- **Registro de empleados**: Agregar empleados con nombre, cargo y días trabajados
- **Cálculo automático de pagos**: Calcula el total a pagar basado en el cargo y días de trabajo
- **Salarios predefinidos**: Estructura salarial configurada por cargo:
  - Ingeniero: $200,000/día
  - Arquitecto: $180,000/día
  - Maestro de obra: $120,000/día
  - Obrero: $80,000/día
- **Generación de reportes**: Visualización de toda la nómina registrada
- **Interfaz gráfica amigable**: Usando Tkinter para una mejor experiencia de usuario

## 🛠️ Requisitos

- Python 3.6+
- Tkinter (incluido por defecto en Python)

## 🚀 Instalación

1. Clonar o descargar el proyecto
2. No requiere instalación de dependencias adicionales

## 📖 Uso

Ejecutar el programa:

```bash
python Nomina_Constructura.py
```

### Pasos para usar:

1. **Ingresar nombre del empleado** en el campo de texto
2. **Seleccionar el cargo** del empleado (Ingeniero, Arquitecto, Maestro de obra u Obrero)
3. **Ingresar los días trabajados** en el campo correspondiente
4. **Calcular Pago**: Ver el total a pagar antes de guardar
5. **Guardar**: Registrar el empleado en el sistema
6. **Mostrar Reporte**: Ver todos los empleados registrados y sus montos a pagar

## 📁 Estructura del código

- **Diccionario `salarios`**: Almacena los salarios diarios por cargo
- **Lista `empleados`**: Guarda los registros de todos los empleados
- **`calcular_pago()`**: Calcula el monto a pagar
- **`guardar()`**: Registra el empleado en el sistema
- **`reporte()`**: Genera una ventana con el reporte completo de nómina
- **Interfaz gráfica**: Ventana principal con campos de entrada y botones de acción

## 👨‍💼 Información del Autor

- **Nombre**: Santiago Villa Ramos
- **Asignatura**: Estructuras de Datos - Quinto Semestre UNAD

## 📝 Notas

Este proyecto es un trabajo académico que implementa conceptos de estructuras de datos y diseño orientado a objetos en Python.

---

*Última actualización: Marzo 2026*

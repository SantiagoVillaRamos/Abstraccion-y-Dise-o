# 🏗️ Sistema de Nómina — Constructora Mejor

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/UI-Tkinter-informational?style=flat-square)
![Arquitectura](https://img.shields.io/badge/Arquitectura-Hexagonal-blueviolet?style=flat-square)
![SOLID](https://img.shields.io/badge/Principios-SOLID-success?style=flat-square)
![UNAD](https://img.shields.io/badge/UNAD-Estructuras%20de%20Datos-orange?style=flat-square)

Sistema de gestión de nómina para empresas del sector construcción, desarrollado en Python con **Arquitectura Hexagonal (Ports & Adapters)**, principios **SOLID**, encapsulamiento y diseño orientado a objetos.

---

## 📋 Tabla de contenidos

1. [Funcionalidades](#funcionalidades)
2. [Cargos y tarifas](#cargos-y-tarifas)
3. [Arquitectura](#arquitectura-hexagonal)
4. [Conceptos aplicados](#conceptos-aplicados)
5. [Instalación y ejecución](#instalación-y-ejecución)
6. [Autor](#autor)

---

## ✨ Funcionalidades

| Botón | Descripción |
|---|---|
| 💰 **Calcular Pago** | Abre una ventana con el desglose completo del pago (sin guardar) |
| 💾 **Guardar** | Registra al empleado en el sistema y muestra el total |
| 📄 **Reporte** | Genera y muestra un reporte de todos los empleados, exportado a `reporte_nomina.txt` |

### Vista de la ventana "Calcular Pago"

La ventana emergente muestra:
- Nombre del empleado
- Cargo asignado
- Días trabajados
- Salario diario del cargo
- **Total a pagar** (destacado en verde)
- Fórmula aplicada: `salario_diario × días = total`

---

## 💼 Cargos y tarifas

| Cargo | Salario diario |
|---|---|
| Ingeniero | $200,000 COP |
| Arquitecto | $180,000 COP |
| Maestro de obra | $120,000 COP |
| Obrero | $80,000 COP |

> **Fórmula de pago:** `Total = Salario diario × Días trabajados`

---

## 🏛️ Arquitectura Hexagonal

La arquitectura sigue el patrón **Ports & Adapters**, donde el núcleo de dominio es completamente independiente de frameworks, bases de datos o interfaces gráficas.

```
abstraccion_y_diseño/
├── main.py                                    ← Composition Root (Inyección de dependencias)
│
├── domain/                                    ← ♦ NÚCLEO (sin dependencias externas)
│   ├── entities/
│   │   ├── cargo.py                           ← Enum Cargo con salario diario encapsulado
│   │   └── empleado.py                        ← Entidad con lógica de negocio pura
│   └── ports/
│       ├── input/
│       │   └── nomina_service_port.py         ← Puerto de ENTRADA (ABC) — casos de uso
│       └── output/
│           ├── empleado_repository_port.py    ← Puerto de SALIDA (ABC) — persistencia
│           └── reporte_port.py               ← Puerto de SALIDA (ABC) — reportes
│
├── application/                               ← ⚙ CASOS DE USO
│   └── services/
│       └── nomina_service.py                  ← Implementa NominaServicePort
│
└── infrastructure/                            ← 🔌 ADAPTADORES (detalles técnicos)
    └── adapters/
        ├── input/
        │   └── tkinter_adapter.py             ← UI Tkinter (adaptador de ENTRADA)
        └── output/
            ├── in_memory_repository.py        ← Repositorio en memoria (adaptador de SALIDA)
            └── txt_reporte_adapter.py         ← Exporta reporte a .txt (adaptador de SALIDA)
```

### Flujo de dependencias

```
┌─────────────────┐       ┌──────────────────────┐
│  TkinterAdapter │──────►│  NominaServicePort   │ (Puerto de entrada)
│  (UI / Entrada) │       └──────────┬───────────┘
└─────────────────┘                  │ implementa
                              ┌──────▼──────────┐
                              │  NominaService  │ (Capa de aplicación)
                              └──────┬──────────┘
                     ┌──────────────┼──────────────┐
                     ▼              ▼              ▼
         ┌──────────────────┐  ┌──────────────────────┐
         │ RepositoryPort   │  │    ReportePort        │
         │ (Puerto salida)  │  │   (Puerto salida)     │
         └────────┬─────────┘  └──────────┬────────────┘
                  │ implementa             │ implementa
         ┌────────▼────────┐   ┌──────────▼───────────┐
         │ InMemoryRepo    │   │  TxtReporteAdapter    │
         └─────────────────┘   └───────────────────────┘
```

> 🔑 El **dominio nunca depende de la infraestructura**. Las dependencias siempre apuntan hacia adentro (hacia el dominio).

---

## 🧠 Conceptos aplicados

| Concepto | Implementación |
|---|---|
| **Abstracción** | Clases abstractas (`ABC`) para todos los puertos de entrada y salida |
| **Encapsulamiento** | Atributos privados (`_nombre`, `_cargo`) con propiedades de solo lectura en `Empleado` |
| **Herencia** | Adaptadores concretos extienden los puertos abstractos del dominio |
| **Polimorfismo** | Cualquier adaptador que implemente el puerto es intercambiable sin tocar el dominio |
| **Inyección de dependencias** | `NominaService` recibe sus dependencias por constructor sin concretarlas |
| **SOLID — D (DIP)** | `main.py` inyecta implementaciones; el servicio solo conoce interfaces abstractas |
| **SOLID — S (SRP)** | Cada clase tiene una única responsabilidad bien definida |
| **SOLID — O (OCP)** | Añadir un nuevo adaptador (p. ej. API REST) no modifica el dominio |
| **Enum tipado** | `Cargo` como tipo seguro con datos (descripción + salario) encapsulados |
| **Separación de capas** | Domain / Application / Infrastructure completamente desacopladas |

---

## 🛠️ Requisitos

- **Python** 3.10 o superior
- **Tkinter** (incluido en la instalación estándar de Python)
- Sin dependencias externas adicionales

---

## 🚀 Instalación y ejecución

### Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd abstraccion_y_diseño
```

### Ejecutar directamente

```bash
python main.py
```

### Con entorno virtual (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\Scripts\activate         # Windows

python main.py
```

---

## 👨‍💻 Autor

**Santiago Villa Ramos**

- 🏫 Universidad Nacional Abierta y a Distancia — **UNAD**
- 📚 Asignatura: Estructuras de Datos
- 📅 Quinto Semestre · Marzo 2026

---

*Proyecto académico · Arquitectura Hexagonal · Python · UNAD 2026*

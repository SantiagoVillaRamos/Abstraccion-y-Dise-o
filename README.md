# Sistema de Nómina - Constructora Mejor

## 📋 Descripción

Sistema de gestión de nómina para constructoras desarrollado en Python, implementando **Arquitectura Hexagonal (Ports & Adapters)** con principios SOLID, encapsulamiento y diseño orientado a objetos.

---

## 🏗 Arquitectura Hexagonal

```
abstraccion_y_diseño/
├── main.py                                    ← Composition Root (DI)
│
├── domain/                                    ← NÚCLEO (sin dependencias externas)
│   ├── entities/
│   │   ├── cargo.py                           ← Enum Cargo con salario diario
│   │   └── empleado.py                        ← Entidad con lógica de negocio
│   └── ports/
│       ├── input/
│       │   └── nomina_service_port.py         ← Puerto de ENTRADA (ABC)
│       └── output/
│           ├── empleado_repository_port.py    ← Puerto de SALIDA (ABC)
│           └── reporte_port.py                ← Puerto de SALIDA (ABC)
│
├── application/                               ← CASOS DE USO
│   └── services/
│       └── nomina_service.py                  ← Implementa NominaServicePort
│
└── infrastructure/                            ← ADAPTADORES (detalles técnicos)
    └── adapters/
        ├── input/
        │   └── tkinter_adapter.py             ← UI Tkinter (adaptador de entrada)
        └── output/
            ├── in_memory_repository.py        ← Repositorio en memoria
            └── txt_reporte_adapter.py         ← Exporta reporte a .txt
```

### Flujo de dependencias

```
[TkinterAdapter] ──► [NominaServicePort]
                           ▲
                    [NominaService] ──► [EmpleadoRepositoryPort] ◄── [InMemoryRepository]
                                   ──► [ReportePort]             ◄── [TxtReporteAdapter]
```

> El dominio **nunca** depende de infraestructura. Las dependencias apuntan hacia adentro.

---

## ✨ Conceptos aplicados

| Concepto | Implementación |
|---|---|
| **Abstracción** | Clases abstractas (ABC) para todos los puertos |
| **Encapsulamiento** | Propiedades privadas en `Empleado`, copia defensiva en repositorio |
| **Herencia / Polimorfismo** | Adaptadores concretos extienden puertos abstractos |
| **Inyección de dependencias** | `NominaService` recibe puertos por constructor |
| **SOLID - D** | Main.py inyecta implementaciones; el servicio solo conoce interfaces |
| **Enum** | `Cargo` como tipo seguro con salario encapsulado |
| **Separación de capas** | Domain / Application / Infrastructure / UI completamente separadas |

---

## 🛠️ Requisitos

- Python 3.10+
- Tkinter (incluido en Python estándar)

## 🚀 Ejecución

```bash
python main.py
```

## 👨‍💼 Autor

- **Nombre**: Santiago Villa Ramos
- **Asignatura**: Estructuras de Datos - Quinto Semestre UNAD

---
*Última actualización: Marzo 2026*

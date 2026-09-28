---
title: "CU-04: Módulo de Servicios, Agenda y Calendario Operativo"
type: Caso_de_Uso
tags:
  - casos-de-uso
  - servicios
  - agenda
  - festivos
  - operacion
aliases:
  - Modulo de Servicios
  - CU Servicios y Operacion
related:
  - "[[00_MOC_Casos_de_Uso]]"
  - "[[RN_Festivos_y_Agenda]]"
  - "[[DB_Tabla_Agenda]]"
  - "[[PROC_Registro_y_Venta]]"
---
# 📌 CU-04: Módulo de Servicios y Operación

## 📌 Descripción General
Administración de categorías y tipos de servicios (almuerzos, catering), y parametrización del calendario operativo.

---

## 📋 Subprocesos y Especificación Funcional

### Subproceso 1: CATEGORIA DE SERVICIOS (5 Casos de Uso)
* **Actor Principal:** `Gestor Comercial`
* **Nodo Principal:** `Gestión de categorías de servicios`

![Diagrama de Casos de Uso - CATEGORIA DE SERVICIOS](../Diagramas_PNG/CATEGORIA_DE_SERVICIOS.png)

#### Casos de Uso Oficiales:
1. **Crear categoría de servicios**
2. **Listar categorías de servicios**
3. **Editar categoría de servicios**
4. **Cambiar estado de la categoría de servicios**
5. **Eliminar categoría de servicios**

---

### Subproceso 2: SERVICIO (7 Casos de Uso)
* **Actor Principal:** `Gestor Comercial`
* **Nodo Principal:** `Gestión de servicios`

![Diagrama de Casos de Uso - SERVICIO](../Diagramas_PNG/SERVICIO.png)

#### Casos de Uso Oficiales:
1. **Crear servicio**
2. **Listar servicios**
3. **Ver detalle del servicio**
4. **Editar servicio**
5. **Cambiar estado del servicio**
6. **Filtrar servicios**
7. **Eliminar servicio**

---

### Subproceso 3: CALENDARIO (4 Casos de Uso)
* **Actor Principal:** `Administrador`
* **Nodo Principal:** `Gestión de calendario`

![Diagrama de Casos de Uso - CALENDARIO](../Diagramas_PNG/CALENDARIO.png)

#### Casos de Uso Oficiales:
1. **Parametrizar calendario**
2. **Listar calendario**
3. **Ver detalle del calendario**
4. **Generar reporte de calendario**

---

---
title: "CU-02: Módulo de Compras, Insumos y Proveedores"
type: Caso_de_Uso
tags:
  - casos-de-uso
  - compras
  - inventario
  - insumos
  - proveedores
aliases:
  - Modulo de Compras
  - CU Compras e Inventario
related:
  - "[[00_MOC_Casos_de_Uso]]"
  - "[[DB_Tablas_Inventario_Compras]]"
  - "[[PROC_Planeacion_Cocina_y_Recetas]]"
---
# 📌 CU-02: Módulo de Compras e Inventario

## 📌 Descripción General
Gestión del catálogo de insumos, categorías de materia prima, proveedores y órdenes de compra.

---

## 📋 Subprocesos y Especificación Funcional

### Subproceso 1: CATEGORIA DE INSUMOS (7 Casos de Uso)
* **Actor Principal:** `Administrador`
* **Nodo Principal:** `Gestión de categorías de insumos`

![Diagrama de Casos de Uso - CATEGORIA DE INSUMOS](../Diagramas_PNG/CATEGORIA_DE_INSUMOS.png)

#### Casos de Uso Oficiales:
1. **Crear categoría de insumo**
2. **Listar categorías de insumos**
3. **Ver detalle de la categoría**
4. **Editar categoría**
5. **Cambiar estado de la categoría**
6. **Eliminar categoría**
7. **Filtrar/Buscar categoría de insumo**

---

### Subproceso 2: INSUMOS (8 Casos de Uso)
* **Actor Principal:** `Administrador`
* **Nodo Principal:** `Gestión de insumos`

![Diagrama de Casos de Uso - INSUMOS](../Diagramas_PNG/INSUMOS.png)

#### Casos de Uso Oficiales:
1. **Crear insumo**
2. **Listar insumos**
3. **Ver detalle del insumo**
4. **Editar insumo**
5. **Cambiar estado del insumo**
6. **Generar reporte de insumos**
7. **Buscar Insumos**
8. **Eliminar insumo**

---

### Subproceso 3: PROVEEDORES (7 Casos de Uso)
* **Actor Principal:** `Administrador`
* **Nodo Principal:** `Gestión de proveedores`

![Diagrama de Casos de Uso - PROVEEDORES](../Diagramas_PNG/PROVEEDORES.png)

#### Casos de Uso Oficiales:
1. **Crear proveedor**
2. **Listar proveedores**
3. **Ver detalle del proveedor**
4. **Editar proveedor**
5. **Cambiar estado del proveedor**
6. **Buscar proveedores**
7. **Eliminar proveedor**

---

### Subproceso 4: COMPRAS (8 Casos de Uso)
* **Actor Principal:** `Administrador`
* **Nodo Principal:** `Gestión de compras`

![Diagrama de Casos de Uso - COMPRAS](../Diagramas_PNG/COMPRAS.png)

#### Casos de Uso Oficiales:
1. **Crear compra**
2. **Listar compras**
3. **Ver detalle de compra**
4. **Editar compra**
5. **Cambiar estado de compra**
6. **Anular compra**
7. **Generar reporte de compras**
8. **Buscar compras**

---

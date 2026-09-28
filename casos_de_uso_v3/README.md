# Especificación General de Casos de Uso - JackSoft (Versión Canónica v3)

**Total de Subprocesos:** 22  
**Total de Casos de Uso Oficiales:** 146  
**Diseño y Estandarización:** Sistema de Diseño Corporativo JackSoft (La Coca de Jacks)

| Nº | Subproceso | Macro-Proceso | Actor Principal | Cantidad de Casos de Uso |
| :--- | :--- | :--- | :--- | :---: |
| 1 | **ROLES** | Configuración y Seguridad | `Administrador` | 7 |
| 2 | **USUARIOS** | Configuración y Seguridad | `Administrador` | 8 |
| 3 | **ACCESO** | Configuración y Seguridad | `Usuario / Admin` | 5 |
| 4 | **CATEGORIA DE INSUMOS** | Compras e Inventario | `Administrador` | 7 |
| 5 | **INSUMOS** | Compras e Inventario | `Administrador` | 8 |
| 6 | **CATEGORIA PRODUCTOS** | Producción y Recetas | `Jefe de Cocina` | 7 |
| 7 | **PRODUCTOS** | Producción y Recetas | `Jefe de Cocina` | 7 |
| 8 | **PROVEEDORES** | Compras e Inventario | `Administrador` | 7 |
| 9 | **COMPRAS** | Compras e Inventario | `Administrador` | 8 |
| 10 | **EMPLEADOS** | Producción y Recetas | `Administrador` | 8 |
| 11 | **PRODUCCION** | Producción y Recetas | `Jefe de Cocina` | 7 |
| 12 | **FICHA TECNICA "PRODUCTO"** | Producción y Recetas | `Jefe de Cocina` | 7 |
| 13 | **PRODUCTO TERMINADO** | Producción y Recetas | `Jefe de Cocina` | 6 |
| 14 | **CATEGORIA DE SERVICIOS** | Servicios y Operación | `Gestor Comercial` | 5 |
| 15 | **SERVICIO** | Servicios y Operación | `Gestor Comercial` | 7 |
| 16 | **CALENDARIO** | Servicios y Operación | `Administrador` | 4 |
| 17 | **CLIENTES** | Clientes y Ventas | `Gestor Comercial` | 7 |
| 18 | **SUSCRIPCIONES** | Clientes y Ventas | `Gestor Comercial` | 9 |
| 19 | **RUTA Y DOMICILIARIOS** | Logística y Domicilios | `Domiciliario` | 5 |
| 20 | **MONITOREO DE ENTREGA "TIEMPO REAL"** | Logística y Domicilios | `Logística` | 7 |
| 21 | **INCIDENCIAS** | Logística y Domicilios | `Logística` | 6 |
| 22 | **DASHBOARD** | Analítica y Métricas | `Administrador` | 4 |

---

## Subproceso: ROLES
* **Macro-Proceso:** Configuración y Seguridad (SEGURIDAD Y ACCESO)
* **Actor:** Administrador
* **Nodo Principal:** Gestión de roles

### Casos de Uso:
1. Crear rol
2. Listar roles
3. Ver detalle del rol
4. Editar rol
5. Asignar permisos
6. Cambiar estado
7. Eliminar rol

---

## Subproceso: USUARIOS
* **Macro-Proceso:** Configuración y Seguridad (SEGURIDAD Y ACCESO)
* **Actor:** Administrador
* **Nodo Principal:** Gestión de usuarios

### Casos de Uso:
1. Crear usuario
2. Listar usuarios
3. Generar reporte
4. Ver detalle del usuario
5. Editar usuario
6. Cambiar estado
7. Eliminar usuario
8. Filtrar/Buscar usuario

---

## Subproceso: ACCESO
* **Macro-Proceso:** Configuración y Seguridad (SEGURIDAD Y ACCESO)
* **Actor:** Usuario / Admin
* **Nodo Principal:** Acceso al sistema

### Casos de Uso:
1. Iniciar sesión
2. Recuperar/Restablecer contraseña
3. Consultar estado de la cuenta
4. Cerrar sesión
5. Generar reporte

---

## Subproceso: CATEGORIA DE INSUMOS
* **Macro-Proceso:** Compras e Inventario (COMPRAS E INVENTARIO)
* **Actor:** Administrador
* **Nodo Principal:** Gestión de categorías de insumos

### Casos de Uso:
1. Crear categoría de insumo
2. Listar categorías de insumos
3. Ver detalle de la categoría
4. Editar categoría
5. Cambiar estado de la categoría
6. Eliminar categoría
7. Filtrar/Buscar categoría de insumo

---

## Subproceso: INSUMOS
* **Macro-Proceso:** Compras e Inventario (COMPRAS E INVENTARIO)
* **Actor:** Administrador
* **Nodo Principal:** Gestión de insumos

### Casos de Uso:
1. Crear insumo
2. Listar insumos
3. Ver detalle del insumo
4. Editar insumo
5. Cambiar estado del insumo
6. Generar reporte de insumos
7. Buscar Insumos
8. Eliminar insumo

---

## Subproceso: CATEGORIA PRODUCTOS
* **Macro-Proceso:** Producción y Recetas (PRODUCCIÓN Y RECETAS)
* **Actor:** Jefe de Cocina
* **Nodo Principal:** Gestión de categorías de productos

### Casos de Uso:
1. Crear categoría de productos
2. Listar categorías de productos
3. Ver detalle de la categoría de productos
4. Editar categoría de productos
5. Cambiar estado de la categoría de productos
6. Eliminar categoría de productos
7. Buscar/Filtrar categorías de productos

---

## Subproceso: PRODUCTOS
* **Macro-Proceso:** Producción y Recetas (PRODUCCIÓN Y RECETAS)
* **Actor:** Jefe de Cocina
* **Nodo Principal:** Gestión de productos

### Casos de Uso:
1. Crear producto
2. Listar productos
3. Ver detalle del producto
4. Editar producto
5. Cambiar estado del producto
6. Buscar productos
7. Eliminar producto

---

## Subproceso: PROVEEDORES
* **Macro-Proceso:** Compras e Inventario (COMPRAS E INVENTARIO)
* **Actor:** Administrador
* **Nodo Principal:** Gestión de proveedores

### Casos de Uso:
1. Crear proveedor
2. Listar proveedores
3. Ver detalle del proveedor
4. Editar proveedor
5. Cambiar estado del proveedor
6. Buscar proveedores
7. Eliminar proveedor

---

## Subproceso: COMPRAS
* **Macro-Proceso:** Compras e Inventario (COMPRAS E INVENTARIO)
* **Actor:** Administrador
* **Nodo Principal:** Gestión de compras

### Casos de Uso:
1. Crear compra
2. Listar compras
3. Ver detalle de compra
4. Editar compra
5. Cambiar estado de compra
6. Anular compra
7. Generar reporte de compras
8. Buscar compras

---

## Subproceso: EMPLEADOS
* **Macro-Proceso:** Producción y Recetas (PRODUCCIÓN Y RECETAS)
* **Actor:** Administrador
* **Nodo Principal:** Gestión de empleados

### Casos de Uso:
1. Crear empleado
2. Listar empleados
3. Generar reporte de empleados
4. Ver detalle del empleado
5. Editar empleado
6. Cambiar estado del empleado
7. Eliminar empleado
8. Buscar empleados

---

## Subproceso: PRODUCCION
* **Macro-Proceso:** Producción y Recetas (PRODUCCIÓN Y RECETAS)
* **Actor:** Jefe de Cocina
* **Nodo Principal:** Gestión de producción

### Casos de Uso:
1. Crear orden de producción
2. Listar órdenes de producción
3. Ver detalle de la orden de producción
4. Editar orden de producción
5. Cambiar estado de la orden de producción
6. Programar producción
7. Buscar producción

---

## Subproceso: FICHA TECNICA "PRODUCTO"
* **Macro-Proceso:** Producción y Recetas (PRODUCCIÓN Y RECETAS)
* **Actor:** Jefe de Cocina
* **Nodo Principal:** Gestión de fichas técnicas

### Casos de Uso:
1. Crear ficha técnica de producto
2. Listar fichas técnicas de producto
3. Ver detalle de la ficha técnica de producto
4. Editar ficha técnica de producto
5. Buscar fichas técnicas de producto
6. Generar reporte de fichas técnicas
7. Eliminar ficha técnica de producto

---

## Subproceso: PRODUCTO TERMINADO
* **Macro-Proceso:** Producción y Recetas (PRODUCCIÓN Y RECETAS)
* **Actor:** Jefe de Cocina
* **Nodo Principal:** Gestión de producto terminado

### Casos de Uso:
1. Registrar producto terminado
2. Listar productos terminados
3. Ver detalle del producto terminado
4. Editar producto terminado
5. Buscar productos terminados
6. Generar reporte de producto terminado

---

## Subproceso: CATEGORIA DE SERVICIOS
* **Macro-Proceso:** Servicios y Operación (SERVICIOS Y OPERACIÓN)
* **Actor:** Gestor Comercial
* **Nodo Principal:** Gestión de categorías de servicios

### Casos de Uso:
1. Crear categoría de servicios
2. Listar categorías de servicios
3. Editar categoría de servicios
4. Cambiar estado de la categoría de servicios
5. Eliminar categoría de servicios

---

## Subproceso: SERVICIO
* **Macro-Proceso:** Servicios y Operación (SERVICIOS Y OPERACIÓN)
* **Actor:** Gestor Comercial
* **Nodo Principal:** Gestión de servicios

### Casos de Uso:
1. Crear servicio
2. Listar servicios
3. Ver detalle del servicio
4. Editar servicio
5. Cambiar estado del servicio
6. Filtrar servicios
7. Eliminar servicio

---

## Subproceso: CALENDARIO
* **Macro-Proceso:** Servicios y Operación (SERVICIOS Y OPERACIÓN)
* **Actor:** Administrador
* **Nodo Principal:** Gestión de calendario

### Casos de Uso:
1. Parametrizar calendario
2. Listar calendario
3. Ver detalle del calendario
4. Generar reporte de calendario

---

## Subproceso: CLIENTES
* **Macro-Proceso:** Clientes y Ventas (CLIENTES Y VENTAS)
* **Actor:** Gestor Comercial
* **Nodo Principal:** Gestión de clientes

### Casos de Uso:
1. Crear cliente
2. Listar clientes
3. Generar reporte de clientes
4. Ver detalle del cliente
5. Editar cliente
6. Cambiar estado del cliente
7. Buscar/Filtrar clientes

---

## Subproceso: SUSCRIPCIONES
* **Macro-Proceso:** Clientes y Ventas (CLIENTES Y VENTAS)
* **Actor:** Gestor Comercial
* **Nodo Principal:** Gestión de suscripciones

### Casos de Uso:
1. Cotizar suscripción
2. Registrar suscripción
3. Listar suscripciones
4. Ver detalle de la suscripción
5. Editar suscripción
6. Cambiar estado de la suscripción
7. Subir comprobante de suscripción
8. Consultar comprobante de suscripción
9. Buscar/Filtrar suscripciones

---

## Subproceso: RUTA Y DOMICILIARIOS
* **Macro-Proceso:** Logística y Domicilios (LOGÍSTICA Y DOMICILIOS)
* **Actor:** Domiciliario
* **Nodo Principal:** Gestión de rutas y domiciliarios

### Casos de Uso:
1. Crear asignacion de zonas
2. Listar domiciliarios
3. Ver detalle del domiciliario
4. Ver estado
5. Buscar/Filtrar domiciliarios

---

## Subproceso: MONITOREO DE ENTREGA "TIEMPO REAL"
* **Macro-Proceso:** Logística y Domicilios (LOGÍSTICA Y DOMICILIOS)
* **Actor:** Logística
* **Nodo Principal:** Monitoreo de entregas

### Casos de Uso:
1. Ver ubicación de domiciliarios en tiempo real
2. Consultar avance de entregas en tiempo real
3. Consultar estado de cocas en tiempo real
4. Buscar entregas en tiempo real
5. Generar reporte de entregas en tiempo real
6. Crear zonas
7. Editar zonas

---

## Subproceso: INCIDENCIAS
* **Macro-Proceso:** Logística y Domicilios (LOGÍSTICA Y DOMICILIOS)
* **Actor:** Logística
* **Nodo Principal:** Gestión de incidencias

### Casos de Uso:
1. Registrar incidencia
2. Listar incidencias
3. Ver detalle de la incidencia
4. Editar incidencia
5. Gestionar incidencia
6. Filtrar incidencias

---

## Subproceso: DASHBOARD
* **Macro-Proceso:** Analítica y Métricas (ANALÍTICA Y MÉTRICAS)
* **Actor:** Administrador
* **Nodo Principal:** Dashboard

### Casos de Uso:
1. Consultar indicadores del dashboard
2. Visualizar gráficos del dashboard
3. Filtrar datos del dashboard
4. Generar reporte del dashboard

---

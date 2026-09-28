# Macro-Proceso: Compras e Inventario

Gestión del catálogo de insumos, categorías de materia prima, proveedores y órdenes de compra.

## Subprocesos Integrados

### Subproceso: CATEGORIA DE INSUMOS
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Administrador
- **Nodo Principal:** Gestión de categorías de insumos

#### Listado de Casos de Uso
1. Crear categoría de insumo
2. Listar categorías de insumos
3. Ver detalle de la categoría
4. Editar categoría
5. Cambiar estado de la categoría
6. Eliminar categoría
7. Filtrar/Buscar categoría de insumo

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
skinparam nodesep 50
skinparam ranksep 70
skinparam shadowing true
skinparam defaultFontName "Inter, Arial, sans-serif"

skinparam actor {
  BorderColor #0f172a
  BackgroundColor #fff7ed
}

skinparam usecase {
  BackgroundColor #ffffff
  BorderColor #0f172a
  ArrowColor #ea580c
}

skinparam usecase<<hub>> {
  BackgroundColor #fff7ed
  BorderColor #ea580c
}

actor "Administrador" as actor_user

rectangle "SISTEMA JACKSOFT — COMPRAS E INVENTARIO (CATEGORIA DE INSUMOS)" {
  usecase "Gestión de categorías de insumos" as UC_Hub <<hub>>
  usecase "Listar categorías de insumos" as UC_Central <<hub>>
  usecase "Crear categoría de insumo" as UC_Top1
  usecase "Filtrar/Buscar categoría de insumo" as UC_Bot1
  usecase "Ver detalle de la categoría" as UC_R1
  usecase "Editar categoría" as UC_R2
  usecase "Cambiar estado de la categoría" as UC_R3
  usecase "Eliminar categoría" as UC_R4
}

actor_user --> UC_Hub
UC_Hub .> UC_Central : <<include>>
UC_Top1 ..> UC_Hub : <<extend>>
UC_Top1 .> UC_Central : <<include>>
UC_Bot1 ..> UC_Hub : <<extend>>
UC_Bot1 .> UC_Central : <<include>>
UC_R1 ..> UC_Central : <<extend>>
UC_R2 ..> UC_Central : <<extend>>
UC_R3 ..> UC_Central : <<extend>>
UC_R4 ..> UC_Central : <<extend>>
@enduml
```

---

### Subproceso: INSUMOS
- **Total de Casos de Uso / Acciones:** 8
- **Actor Principal:** Administrador
- **Nodo Principal:** Gestión de insumos

#### Listado de Casos de Uso
1. Crear insumo
2. Listar insumos
3. Ver detalle del insumo
4. Editar insumo
5. Cambiar estado del insumo
6. Generar reporte de insumos
7. Buscar Insumos
8. Eliminar insumo

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
skinparam nodesep 50
skinparam ranksep 70
skinparam shadowing true
skinparam defaultFontName "Inter, Arial, sans-serif"

skinparam actor {
  BorderColor #0f172a
  BackgroundColor #fff7ed
}

skinparam usecase {
  BackgroundColor #ffffff
  BorderColor #0f172a
  ArrowColor #ea580c
}

skinparam usecase<<hub>> {
  BackgroundColor #fff7ed
  BorderColor #ea580c
}

actor "Administrador" as actor_user

rectangle "SISTEMA JACKSOFT — COMPRAS E INVENTARIO (INSUMOS)" {
  usecase "Gestión de insumos" as UC_Hub <<hub>>
  usecase "Listar insumos" as UC_Central <<hub>>
  usecase "Crear insumo" as UC_Top1
  usecase "Generar reporte de insumos" as UC_Top2
  usecase "Buscar Insumos" as UC_Bot1
  usecase "Ver detalle del insumo" as UC_R1
  usecase "Editar insumo" as UC_R2
  usecase "Cambiar estado del insumo" as UC_R3
  usecase "Eliminar insumo" as UC_R4
}

actor_user --> UC_Hub
UC_Hub .> UC_Central : <<include>>
UC_Top1 ..> UC_Hub : <<extend>>
UC_Top1 .> UC_Central : <<include>>
UC_Top2 .> UC_Central : <<include>>
UC_Bot1 ..> UC_Hub : <<extend>>
UC_Bot1 .> UC_Central : <<include>>
UC_R1 ..> UC_Central : <<extend>>
UC_R2 ..> UC_Central : <<extend>>
UC_R3 ..> UC_Central : <<extend>>
UC_R4 ..> UC_Central : <<extend>>
@enduml
```

---

### Subproceso: PROVEEDORES
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Administrador
- **Nodo Principal:** Gestión de proveedores

#### Listado de Casos de Uso
1. Crear proveedor
2. Listar proveedores
3. Ver detalle del proveedor
4. Editar proveedor
5. Cambiar estado del proveedor
6. Buscar proveedores
7. Eliminar proveedor

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
skinparam nodesep 50
skinparam ranksep 70
skinparam shadowing true
skinparam defaultFontName "Inter, Arial, sans-serif"

skinparam actor {
  BorderColor #0f172a
  BackgroundColor #fff7ed
}

skinparam usecase {
  BackgroundColor #ffffff
  BorderColor #0f172a
  ArrowColor #ea580c
}

skinparam usecase<<hub>> {
  BackgroundColor #fff7ed
  BorderColor #ea580c
}

actor "Administrador" as actor_user

rectangle "SISTEMA JACKSOFT — COMPRAS E INVENTARIO (PROVEEDORES)" {
  usecase "Gestión de proveedores" as UC_Hub <<hub>>
  usecase "Listar proveedores" as UC_Central <<hub>>
  usecase "Crear proveedor" as UC_Top1
  usecase "Buscar proveedores" as UC_Bot1
  usecase "Ver detalle del proveedor" as UC_R1
  usecase "Editar proveedor" as UC_R2
  usecase "Cambiar estado del proveedor" as UC_R3
  usecase "Eliminar proveedor" as UC_R4
}

actor_user --> UC_Hub
UC_Hub .> UC_Central : <<include>>
UC_Top1 ..> UC_Hub : <<extend>>
UC_Top1 .> UC_Central : <<include>>
UC_Bot1 ..> UC_Hub : <<extend>>
UC_Bot1 .> UC_Central : <<include>>
UC_R1 ..> UC_Central : <<extend>>
UC_R2 ..> UC_Central : <<extend>>
UC_R3 ..> UC_Central : <<extend>>
UC_R4 ..> UC_Central : <<extend>>
@enduml
```

---

### Subproceso: COMPRAS
- **Total de Casos de Uso / Acciones:** 8
- **Actor Principal:** Administrador
- **Nodo Principal:** Gestión de compras

#### Listado de Casos de Uso
1. Crear compra
2. Listar compras
3. Ver detalle de compra
4. Editar compra
5. Cambiar estado de compra
6. Anular compra
7. Generar reporte de compras
8. Buscar compras

#### Diagrama PlantUML
```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
skinparam nodesep 50
skinparam ranksep 70
skinparam shadowing true
skinparam defaultFontName "Inter, Arial, sans-serif"

skinparam actor {
  BorderColor #0f172a
  BackgroundColor #fff7ed
}

skinparam usecase {
  BackgroundColor #ffffff
  BorderColor #0f172a
  ArrowColor #ea580c
}

skinparam usecase<<hub>> {
  BackgroundColor #fff7ed
  BorderColor #ea580c
}

actor "Administrador" as actor_user

rectangle "SISTEMA JACKSOFT — COMPRAS E INVENTARIO (COMPRAS)" {
  usecase "Gestión de compras" as UC_Hub <<hub>>
  usecase "Listar compras" as UC_Central <<hub>>
  usecase "Crear compra" as UC_Top1
  usecase "Generar reporte de compras" as UC_Top2
  usecase "Buscar compras" as UC_Bot1
  usecase "Ver detalle de compra" as UC_R1
  usecase "Editar compra" as UC_R2
  usecase "Cambiar estado de compra" as UC_R3
  usecase "Anular compra" as UC_R4
}

actor_user --> UC_Hub
UC_Hub .> UC_Central : <<include>>
UC_Top1 ..> UC_Hub : <<extend>>
UC_Top1 .> UC_Central : <<include>>
UC_Top2 .> UC_Central : <<include>>
UC_Bot1 ..> UC_Hub : <<extend>>
UC_Bot1 .> UC_Central : <<include>>
UC_R1 ..> UC_Central : <<extend>>
UC_R2 ..> UC_Central : <<extend>>
UC_R3 ..> UC_Central : <<extend>>
UC_R4 ..> UC_Central : <<extend>>
@enduml
```

---

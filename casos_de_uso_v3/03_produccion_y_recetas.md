# Macro-Proceso: Producción y Recetas

Control de personal de cocina, categorías y catálogo de productos, fichas técnicas (recetas), órdenes de producción y producto terminado.

## Subprocesos Integrados

### Subproceso: CATEGORIA PRODUCTOS
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Jefe de Cocina
- **Nodo Principal:** Gestión de categorías de productos

#### Listado de Casos de Uso
1. Crear categoría de productos
2. Listar categorías de productos
3. Ver detalle de la categoría de productos
4. Editar categoría de productos
5. Cambiar estado de la categoría de productos
6. Eliminar categoría de productos
7. Buscar/Filtrar categorías de productos

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

actor "Jefe de Cocina" as actor_user

rectangle "SISTEMA JACKSOFT — PRODUCCIÓN Y RECETAS (CATEGORIA PRODUCTOS)" {
  usecase "Gestión de categorías de productos" as UC_Hub <<hub>>
  usecase "Listar categorías de productos" as UC_Central <<hub>>
  usecase "Crear categoría de productos" as UC_Top1
  usecase "Buscar/Filtrar categorías de productos" as UC_Bot1
  usecase "Ver detalle de la categoría de productos" as UC_R1
  usecase "Editar categoría de productos" as UC_R2
  usecase "Cambiar estado de la categoría de productos" as UC_R3
  usecase "Eliminar categoría de productos" as UC_R4
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

### Subproceso: PRODUCTOS
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Jefe de Cocina
- **Nodo Principal:** Gestión de productos

#### Listado de Casos de Uso
1. Crear producto
2. Listar productos
3. Ver detalle del producto
4. Editar producto
5. Cambiar estado del producto
6. Buscar productos
7. Eliminar producto

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

actor "Jefe de Cocina" as actor_user

rectangle "SISTEMA JACKSOFT — PRODUCCIÓN Y RECETAS (PRODUCTOS)" {
  usecase "Gestión de productos" as UC_Hub <<hub>>
  usecase "Listar productos" as UC_Central <<hub>>
  usecase "Crear producto" as UC_Top1
  usecase "Buscar productos" as UC_Bot1
  usecase "Ver detalle del producto" as UC_R1
  usecase "Editar producto" as UC_R2
  usecase "Cambiar estado del producto" as UC_R3
  usecase "Eliminar producto" as UC_R4
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

### Subproceso: EMPLEADOS
- **Total de Casos de Uso / Acciones:** 8
- **Actor Principal:** Administrador
- **Nodo Principal:** Gestión de empleados

#### Listado de Casos de Uso
1. Crear empleado
2. Listar empleados
3. Generar reporte de empleados
4. Ver detalle del empleado
5. Editar empleado
6. Cambiar estado del empleado
7. Eliminar empleado
8. Buscar empleados

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

rectangle "SISTEMA JACKSOFT — PRODUCCIÓN Y RECETAS (EMPLEADOS)" {
  usecase "Gestión de empleados" as UC_Hub <<hub>>
  usecase "Listar empleados" as UC_Central <<hub>>
  usecase "Crear empleado" as UC_Top1
  usecase "Generar reporte de empleados" as UC_Top2
  usecase "Buscar empleados" as UC_Bot1
  usecase "Ver detalle del empleado" as UC_R1
  usecase "Editar empleado" as UC_R2
  usecase "Cambiar estado del empleado" as UC_R3
  usecase "Eliminar empleado" as UC_R4
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

### Subproceso: PRODUCCION
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Jefe de Cocina
- **Nodo Principal:** Gestión de producción

#### Listado de Casos de Uso
1. Crear orden de producción
2. Listar órdenes de producción
3. Ver detalle de la orden de producción
4. Editar orden de producción
5. Cambiar estado de la orden de producción
6. Programar producción
7. Buscar producción

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

actor "Jefe de Cocina" as actor_user

rectangle "SISTEMA JACKSOFT — PRODUCCIÓN Y RECETAS (PRODUCCION)" {
  usecase "Gestión de producción" as UC_Hub <<hub>>
  usecase "Listar órdenes de producción" as UC_Central <<hub>>
  usecase "Crear orden de producción" as UC_Top1
  usecase "Buscar producción" as UC_Bot1
  usecase "Ver detalle de la orden de producción" as UC_R1
  usecase "Editar orden de producción" as UC_R2
  usecase "Cambiar estado de la orden de producción" as UC_R3
  usecase "Programar producción" as UC_R4
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

### Subproceso: FICHA TECNICA "PRODUCTO"
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Jefe de Cocina
- **Nodo Principal:** Gestión de fichas técnicas

#### Listado de Casos de Uso
1. Crear ficha técnica de producto
2. Listar fichas técnicas de producto
3. Ver detalle de la ficha técnica de producto
4. Editar ficha técnica de producto
5. Buscar fichas técnicas de producto
6. Generar reporte de fichas técnicas
7. Eliminar ficha técnica de producto

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

actor "Jefe de Cocina" as actor_user

rectangle "SISTEMA JACKSOFT — PRODUCCIÓN Y RECETAS (FICHA TECNICA PRODUCTO)" {
  usecase "Gestión de fichas técnicas" as UC_Hub <<hub>>
  usecase "Listar fichas técnicas de producto" as UC_Central <<hub>>
  usecase "Crear ficha técnica de producto" as UC_Top1
  usecase "Generar reporte de fichas técnicas" as UC_Top2
  usecase "Buscar fichas técnicas de producto" as UC_Bot1
  usecase "Ver detalle de la ficha técnica de producto" as UC_R1
  usecase "Editar ficha técnica de producto" as UC_R2
  usecase "Eliminar ficha técnica de producto" as UC_R3
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
@enduml
```

---

### Subproceso: PRODUCTO TERMINADO
- **Total de Casos de Uso / Acciones:** 6
- **Actor Principal:** Jefe de Cocina
- **Nodo Principal:** Gestión de producto terminado

#### Listado de Casos de Uso
1. Registrar producto terminado
2. Listar productos terminados
3. Ver detalle del producto terminado
4. Editar producto terminado
5. Buscar productos terminados
6. Generar reporte de producto terminado

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

actor "Jefe de Cocina" as actor_user

rectangle "SISTEMA JACKSOFT — PRODUCCIÓN Y RECETAS (PRODUCTO TERMINADO)" {
  usecase "Gestión de producto terminado" as UC_Hub <<hub>>
  usecase "Listar productos terminados" as UC_Central <<hub>>
  usecase "Registrar producto terminado" as UC_Top1
  usecase "Generar reporte de producto terminado" as UC_Top2
  usecase "Buscar productos terminados" as UC_Bot1
  usecase "Ver detalle del producto terminado" as UC_R1
  usecase "Editar producto terminado" as UC_R2
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
@enduml
```

---

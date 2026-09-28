# Macro-Proceso: Servicios y Operación

Administración de categorías y tipos de servicios (almuerzos, catering), y parametrización del calendario operativo.

## Subprocesos Integrados

### Subproceso: CATEGORIA DE SERVICIOS
- **Total de Casos de Uso / Acciones:** 5
- **Actor Principal:** Gestor Comercial
- **Nodo Principal:** Gestión de categorías de servicios

#### Listado de Casos de Uso
1. Crear categoría de servicios
2. Listar categorías de servicios
3. Editar categoría de servicios
4. Cambiar estado de la categoría de servicios
5. Eliminar categoría de servicios

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

actor "Gestor Comercial" as actor_user

rectangle "SISTEMA JACKSOFT — SERVICIOS Y OPERACIÓN (CATEGORIA DE SERVICIOS)" {
  usecase "Gestión de categorías de servicios" as UC_Hub <<hub>>
  usecase "Listar categorías de servicios" as UC_Central <<hub>>
  usecase "Crear categoría de servicios" as UC_Top1
  usecase "Editar categoría de servicios" as UC_R1
  usecase "Cambiar estado de la categoría de servicios" as UC_R2
  usecase "Eliminar categoría de servicios" as UC_R3
}

actor_user --> UC_Hub
UC_Hub .> UC_Central : <<include>>
UC_Top1 ..> UC_Hub : <<extend>>
UC_Top1 .> UC_Central : <<include>>
UC_R1 ..> UC_Central : <<extend>>
UC_R2 ..> UC_Central : <<extend>>
UC_R3 ..> UC_Central : <<extend>>
@enduml
```

---

### Subproceso: SERVICIO
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Gestor Comercial
- **Nodo Principal:** Gestión de servicios

#### Listado de Casos de Uso
1. Crear servicio
2. Listar servicios
3. Ver detalle del servicio
4. Editar servicio
5. Cambiar estado del servicio
6. Filtrar servicios
7. Eliminar servicio

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

actor "Gestor Comercial" as actor_user

rectangle "SISTEMA JACKSOFT — SERVICIOS Y OPERACIÓN (SERVICIO)" {
  usecase "Gestión de servicios" as UC_Hub <<hub>>
  usecase "Listar servicios" as UC_Central <<hub>>
  usecase "Crear servicio" as UC_Top1
  usecase "Filtrar servicios" as UC_Bot1
  usecase "Ver detalle del servicio" as UC_R1
  usecase "Editar servicio" as UC_R2
  usecase "Cambiar estado del servicio" as UC_R3
  usecase "Eliminar servicio" as UC_R4
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

### Subproceso: CALENDARIO
- **Total de Casos de Uso / Acciones:** 4
- **Actor Principal:** Administrador
- **Nodo Principal:** Gestión de calendario

#### Listado de Casos de Uso
1. Parametrizar calendario
2. Listar calendario
3. Ver detalle del calendario
4. Generar reporte de calendario

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

rectangle "SISTEMA JACKSOFT — SERVICIOS Y OPERACIÓN (CALENDARIO)" {
  usecase "Gestión de calendario" as UC_Hub <<hub>>
  usecase "Listar calendario" as UC_Central <<hub>>
  usecase "Parametrizar calendario" as UC_Top1
  usecase "Generar reporte de calendario" as UC_Top2
  usecase "Ver detalle del calendario" as UC_R1
}

actor_user --> UC_Hub
UC_Hub .> UC_Central : <<include>>
UC_Top1 ..> UC_Hub : <<extend>>
UC_Top1 .> UC_Central : <<include>>
UC_Top2 .> UC_Central : <<include>>
UC_R1 ..> UC_Central : <<extend>>
@enduml
```

---

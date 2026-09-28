# Macro-Proceso: Logística y Domicilios

Asignación de zonas de reparto, gestión de domiciliarios, monitoreo en tiempo real de entregas y gestión de incidencias operativas.

## Subprocesos Integrados

### Subproceso: RUTA Y DOMICILIARIOS
- **Total de Casos de Uso / Acciones:** 5
- **Actor Principal:** Domiciliario
- **Nodo Principal:** Gestión de rutas y domiciliarios

#### Listado de Casos de Uso
1. Crear asignacion de zonas
2. Listar domiciliarios
3. Ver detalle del domiciliario
4. Ver estado
5. Buscar/Filtrar domiciliarios

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

actor "Domiciliario" as actor_user

rectangle "SISTEMA JACKSOFT — LOGÍSTICA Y DOMICILIOS (RUTA Y DOMICILIARIOS)" {
  usecase "Gestión de rutas y domiciliarios" as UC_Hub <<hub>>
  usecase "Listar domiciliarios" as UC_Central <<hub>>
  usecase "Crear asignacion de zonas" as UC_Top1
  usecase "Buscar/Filtrar domiciliarios" as UC_Bot1
  usecase "Ver detalle del domiciliario" as UC_R1
  usecase "Ver estado" as UC_R2
}

actor_user --> UC_Hub
UC_Hub .> UC_Central : <<include>>
UC_Top1 ..> UC_Hub : <<extend>>
UC_Top1 .> UC_Central : <<include>>
UC_Bot1 ..> UC_Hub : <<extend>>
UC_Bot1 .> UC_Central : <<include>>
UC_R1 ..> UC_Central : <<extend>>
UC_R2 ..> UC_Central : <<extend>>
@enduml
```

---

### Subproceso: MONITOREO DE ENTREGA "TIEMPO REAL"
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Logística
- **Nodo Principal:** Monitoreo de entregas

#### Listado de Casos de Uso
1. Ver ubicación de domiciliarios en tiempo real
2. Consultar avance de entregas en tiempo real
3. Consultar estado de cocas en tiempo real
4. Buscar entregas en tiempo real
5. Generar reporte de entregas en tiempo real
6. Crear zonas
7. Editar zonas

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

actor "Logística" as actor_user

rectangle "SISTEMA JACKSOFT — LOGÍSTICA Y DOMICILIOS (MONITOREO DE ENTREGA TIEMPO REAL)" {
  usecase "Monitoreo de entregas" as UC_Hub <<hub>>
  usecase "Consultar avance de entregas en tiempo real" as UC_Central <<hub>>
  usecase "Crear zonas" as UC_Top1
  usecase "Generar reporte de entregas en tiempo real" as UC_Top2
  usecase "Buscar entregas en tiempo real" as UC_Bot1
  usecase "Ver ubicación de domiciliarios en tiempo real" as UC_R1
  usecase "Consultar estado de cocas en tiempo real" as UC_R2
  usecase "Editar zonas" as UC_R3
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

### Subproceso: INCIDENCIAS
- **Total de Casos de Uso / Acciones:** 6
- **Actor Principal:** Logística
- **Nodo Principal:** Gestión de incidencias

#### Listado de Casos de Uso
1. Registrar incidencia
2. Listar incidencias
3. Ver detalle de la incidencia
4. Editar incidencia
5. Gestionar incidencia
6. Filtrar incidencias

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

actor "Logística" as actor_user

rectangle "SISTEMA JACKSOFT — LOGÍSTICA Y DOMICILIOS (INCIDENCIAS)" {
  usecase "Gestión de incidencias" as UC_Hub <<hub>>
  usecase "Listar incidencias" as UC_Central <<hub>>
  usecase "Registrar incidencia" as UC_Top1
  usecase "Filtrar incidencias" as UC_Bot1
  usecase "Ver detalle de la incidencia" as UC_R1
  usecase "Editar incidencia" as UC_R2
  usecase "Gestionar incidencia" as UC_R3
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
@enduml
```

---

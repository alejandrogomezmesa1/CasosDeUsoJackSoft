# Macro-Proceso: Clientes y Ventas

Gestión de clientes, cotización, registro y administración de suscripciones corporativas e individuales.

## Subprocesos Integrados

### Subproceso: CLIENTES
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Gestor Comercial
- **Nodo Principal:** Gestión de clientes

#### Listado de Casos de Uso
1. Crear cliente
2. Listar clientes
3. Generar reporte de clientes
4. Ver detalle del cliente
5. Editar cliente
6. Cambiar estado del cliente
7. Buscar/Filtrar clientes

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

rectangle "SISTEMA JACKSOFT — CLIENTES Y VENTAS (CLIENTES)" {
  usecase "Gestión de clientes" as UC_Hub <<hub>>
  usecase "Listar clientes" as UC_Central <<hub>>
  usecase "Crear cliente" as UC_Top1
  usecase "Generar reporte de clientes" as UC_Top2
  usecase "Buscar/Filtrar clientes" as UC_Bot1
  usecase "Ver detalle del cliente" as UC_R1
  usecase "Editar cliente" as UC_R2
  usecase "Cambiar estado del cliente" as UC_R3
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

### Subproceso: SUSCRIPCIONES
- **Total de Casos de Uso / Acciones:** 9
- **Actor Principal:** Gestor Comercial
- **Nodo Principal:** Gestión de suscripciones

#### Listado de Casos de Uso
1. Cotizar suscripción
2. Registrar suscripción
3. Listar suscripciones
4. Ver detalle de la suscripción
5. Editar suscripción
6. Cambiar estado de la suscripción
7. Subir comprobante de suscripción
8. Consultar comprobante de suscripción
9. Buscar/Filtrar suscripciones

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

rectangle "SISTEMA JACKSOFT — CLIENTES Y VENTAS (SUSCRIPCIONES)" {
  usecase "Gestión de suscripciones" as UC_Hub <<hub>>
  usecase "Listar suscripciones" as UC_Central <<hub>>
  usecase "Cotizar suscripción" as UC_Top1
  usecase "Registrar suscripción" as UC_Top2
  usecase "Buscar/Filtrar suscripciones" as UC_Bot1
  usecase "Ver detalle de la suscripción" as UC_R1
  usecase "Editar suscripción" as UC_R2
  usecase "Cambiar estado de la suscripción" as UC_R3
  usecase "Subir comprobante de suscripción" as UC_R4
  usecase "Consultar comprobante de suscripción" as UC_R5
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
UC_R5 ..> UC_Central : <<extend>>
@enduml
```

---

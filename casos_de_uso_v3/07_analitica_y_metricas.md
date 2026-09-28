# Macro-Proceso: Analítica y Métricas

Consulta de indicadores clave de rendimiento (KPIs), visualización gráfica de métricas y generación de reportes de gestión.

## Subprocesos Integrados

### Subproceso: DASHBOARD
- **Total de Casos de Uso / Acciones:** 4
- **Actor Principal:** Administrador
- **Nodo Principal:** Dashboard

#### Listado de Casos de Uso
1. Consultar indicadores del dashboard
2. Visualizar gráficos del dashboard
3. Filtrar datos del dashboard
4. Generar reporte del dashboard

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

rectangle "SISTEMA JACKSOFT — ANALÍTICA Y MÉTRICAS (DASHBOARD)" {
  usecase "Dashboard" as UC_Hub <<hub>>
  usecase "Consultar indicadores del dashboard" as UC_Central <<hub>>
  usecase "Visualizar gráficos del dashboard" as UC_Top1
  usecase "Generar reporte del dashboard" as UC_Top2
  usecase "Filtrar datos del dashboard" as UC_Bot1
}

actor_user --> UC_Hub
UC_Hub .> UC_Central : <<include>>
UC_Top1 ..> UC_Hub : <<extend>>
UC_Top1 .> UC_Central : <<include>>
UC_Top2 .> UC_Central : <<include>>
UC_Bot1 ..> UC_Hub : <<extend>>
UC_Bot1 .> UC_Central : <<include>>
@enduml
```

---

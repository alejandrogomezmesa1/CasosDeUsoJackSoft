# Macro-Proceso: Configuración y Seguridad

Gestión de roles, permisos, usuarios y mecanismos de autenticación y acceso al sistema.

## Subprocesos Integrados

### Subproceso: ROLES
- **Total de Casos de Uso / Acciones:** 7
- **Actor Principal:** Administrador
- **Nodo Principal:** Gestión de roles

#### Listado de Casos de Uso
1. Crear rol
2. Listar roles
3. Ver detalle del rol
4. Editar rol
5. Asignar permisos
6. Cambiar estado
7. Eliminar rol

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

rectangle "SISTEMA JACKSOFT — SEGURIDAD Y ACCESO (ROLES)" {
  usecase "Gestión de roles" as UC_Hub <<hub>>
  usecase "Listar roles" as UC_Central <<hub>>
  usecase "Crear rol" as UC_Top1
  usecase "Ver detalle del rol" as UC_R1
  usecase "Editar rol" as UC_R2
  usecase "Asignar permisos" as UC_R3
  usecase "Cambiar estado" as UC_R4
  usecase "Eliminar rol" as UC_R5
}

actor_user --> UC_Hub
UC_Hub .> UC_Central : <<include>>
UC_Top1 ..> UC_Hub : <<extend>>
UC_Top1 .> UC_Central : <<include>>
UC_R1 ..> UC_Central : <<extend>>
UC_R2 ..> UC_Central : <<extend>>
UC_R3 ..> UC_Central : <<extend>>
UC_R4 ..> UC_Central : <<extend>>
UC_R5 ..> UC_Central : <<extend>>
@enduml
```

---

### Subproceso: USUARIOS
- **Total de Casos de Uso / Acciones:** 8
- **Actor Principal:** Administrador
- **Nodo Principal:** Gestión de usuarios

#### Listado de Casos de Uso
1. Crear usuario
2. Listar usuarios
3. Generar reporte
4. Ver detalle del usuario
5. Editar usuario
6. Cambiar estado
7. Eliminar usuario
8. Filtrar/Buscar usuario

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

rectangle "SISTEMA JACKSOFT — SEGURIDAD Y ACCESO (USUARIOS)" {
  usecase "Gestión de usuarios" as UC_Hub <<hub>>
  usecase "Listar usuarios" as UC_Central <<hub>>
  usecase "Crear usuario" as UC_Top1
  usecase "Generar reporte" as UC_Top2
  usecase "Filtrar/Buscar usuario" as UC_Bot1
  usecase "Ver detalle del usuario" as UC_R1
  usecase "Editar usuario" as UC_R2
  usecase "Cambiar estado" as UC_R3
  usecase "Eliminar usuario" as UC_R4
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

### Subproceso: ACCESO
- **Total de Casos de Uso / Acciones:** 5
- **Actor Principal:** Usuario / Admin
- **Nodo Principal:** Acceso al sistema

#### Listado de Casos de Uso
1. Iniciar sesión
2. Recuperar/Restablecer contraseña
3. Consultar estado de la cuenta
4. Cerrar sesión
5. Generar reporte

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

actor "Usuario / Admin" as actor_user

rectangle "SISTEMA JACKSOFT — SEGURIDAD Y ACCESO (ACCESO)" {
  usecase "Acceso al sistema" as UC_Hub <<hub>>
  usecase "Iniciar sesión" as UC_Login <<hub>>
  usecase "Recuperar/Restablecer contraseña" as UC_Recup
  usecase "Consultar estado de la cuenta" as UC_Estado
  usecase "Cerrar sesión" as UC_Logout
  usecase "Generar reporte" as UC_Reporte
}

actor_user --> UC_Hub
UC_Hub .> UC_Login : <<include>>
UC_Recup ..> UC_Hub : <<extend>>
UC_Estado ..> UC_Login : <<extend>>
UC_Logout ..> UC_Login : <<extend>>
UC_Reporte ..> UC_Hub : <<extend>>
UC_Reporte .> UC_Login : <<include>>
@enduml
```

---

import csv
import json
import os
import re

csv_file = "/Users/alejo/Proyectos/MapaMental/Tablero Kanban + Matriz HU (Agosto 21)) - Story Mapping.csv"
output_dir = "/Users/alejo/Proyectos/MapaMental/diagramas_casos_uso"
os.makedirs(output_dir, exist_ok=True)

subprocesses = []

with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = list(csv.reader(f))
    headers = reader[5]
    
    start_col = 0
    for i, h in enumerate(headers):
        if h.strip() == "ROLES":
            start_col = i
            break
            
    for col in range(start_col, len(headers)):
        name = headers[col].strip()
        if not name:
            continue
            
        actions = []
        for r in range(6, len(reader)):
            if col < len(reader[r]):
                val = reader[r][col].strip()
                if val and not val.isdigit():
                    clean_val = val.replace('"', '').replace('\n', ' ').strip()
                    actions.append(clean_val)
                    
        if actions:
            subprocesses.append({
                "title": name,
                "actions": actions
            })

def build_puml(sp):
    raw_title = sp["title"]
    clean_title = raw_title.replace('"', '').strip()
    actions = sp["actions"]
    
    if clean_title.upper() == "DASHBOARD":
        puml = []
        puml.append("@startuml")
        puml.append("left to right direction")
        puml.append("skinparam packageStyle rectangle")
        puml.append("skinparam nodesep 40")
        puml.append("skinparam ranksep 60")
        puml.append("")
        puml.append('actor "Admin" as admin')
        puml.append("")
        puml.append('package "DASHBOARD" {')
        puml.append('  usecase "Dashboard" as UC_Hub')
        
        create_action = None
        search_action = None
        right_actions = []
        for name in actions:
            name_lower = name.lower()
            if name_lower.startswith("exportar"):
                create_action = name
            elif name_lower.startswith("filtrar"):
                search_action = name
            else:
                right_actions.append(name)
                
        if create_action:
            puml.append(f'  usecase "{create_action}" as UC_Create')
        if search_action:
            puml.append(f'  usecase "{search_action}" as UC_Search')
        for idx, name in enumerate(right_actions):
            puml.append(f'  usecase "{name}" as UC_R{idx+1}')
            
        puml.append("}")
        puml.append("")
        puml.append("admin -right-> UC_Hub")
        if create_action:
            puml.append("UC_Create ..> UC_Hub : <<extends>>")
        if search_action:
            puml.append("UC_Search ..> UC_Hub : <<extends>>")
        for idx in range(len(right_actions)):
            puml.append(f"UC_R{idx+1} ..> UC_Hub : <<extends>>")
            
        puml.append("@enduml")
        return "\n".join(puml)

    if clean_title.upper() == "ACCESO":
        hub_name = "Acceso al sistema"
    elif clean_title.upper() == "DASHBOARD":
        hub_name = "Dashboard"
    elif clean_title.upper() == "CALENDARIO":
        hub_name = "Gestión de calendario"
    elif clean_title.upper() == "MONITOREO DE ENTREGA TIEMPO REAL":
        hub_name = "Monitoreo de entregas"
    elif clean_title.upper().startswith("CATEGORIA"):
        hub_name = f"Gestión de {clean_title.lower()}"
    elif clean_title.upper().startswith("FICHA"):
        hub_name = "Gestión de fichas técnicas"
    elif clean_title.upper().startswith("RUTA"):
        hub_name = "Gestión de rutas y domiciliarios"
    else:
        hub_name = f"Gestión de {clean_title.lower()}"

    central_action = None
    create_action = None
    search_action = None
    right_actions = []
    
    for name in actions:
        if name.lower().startswith("listar"):
            central_action = name
            break
    if not central_action:
        for name in actions:
            if name.lower().startswith("consultar") or name.lower().startswith("generar reportes"):
                central_action = name
                break

    for name in actions:
        if name == central_action:
            continue
        name_lower = name.lower()
        if not create_action and (name_lower.startswith("crear") or name_lower.startswith("registrar") or name_lower.startswith("exportar") or name_lower.startswith("parametrizar") or name_lower.startswith("cotizar")):
            create_action = name
        elif not search_action and (name_lower.startswith("buscar") or name_lower.startswith("filtrar") or name_lower.startswith("iniciar sesión")):
            search_action = name
        else:
            right_actions.append(name)
        
    puml = []
    puml.append("@startuml")
    puml.append("left to right direction")
    puml.append("skinparam packageStyle rectangle")
    puml.append("skinparam nodesep 40")
    puml.append("skinparam ranksep 60")
    puml.append("")
    puml.append('actor "Admin" as admin')
    puml.append("")
    puml.append(f'package "{clean_title}" {{')
    puml.append(f'  usecase "{hub_name}" as UC_Hub')
    
    # Central UC (only action name, no HU code)
    puml.append(f'  usecase "{central_action}" as UC_Central')
    
    # Top (Create) UC
    if create_action and create_action != central_action:
        puml.append(f'  usecase "{create_action}" as UC_Create')
        
    # Bottom (Search) UC
    if search_action and search_action != central_action and search_action != create_action:
        puml.append(f'  usecase "{search_action}" as UC_Search')
        
    # Right column UCs
    for idx, name in enumerate(right_actions):
        puml.append(f'  usecase "{name}" as UC_R{idx+1}')
        
    puml.append("}")
    puml.append("")
    
    # Connections
    puml.append("admin -right-> UC_Hub")
    puml.append("UC_Hub -right-> UC_Central : <<include>>")
    
    if create_action and create_action != central_action:
        puml.append("UC_Create -down-> UC_Hub : <<extends>>")
        puml.append("UC_Create -down-> UC_Central : <<include>>")
        
    if search_action and search_action != central_action and search_action != create_action:
        puml.append("UC_Search -up-> UC_Hub : <<extends>>")
        puml.append("UC_Search -up-> UC_Central : <<include>>")
        
    for idx in range(len(right_actions)):
        puml.append(f"UC_R{idx+1} -left-> UC_Central : <<extends>>")
        
    puml.append("@enduml")
    return "\n".join(puml)

# Generate files
for sp in subprocesses:
    puml_content = build_puml(sp)
    safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', sp["title"]) + ".puml"
    path = os.path.join(output_dir, safe_name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(puml_content)
    print(f"Cleaned HU text from {safe_name}")

print("All 23 diagrams generated without HU labels.")

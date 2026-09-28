import csv
import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
project_root = os.path.dirname(base_dir)

csv_file = os.path.join(project_root, "06_Gestion_de_Proyecto_Scrum", "Historias_de_Usuario_y_Kanban", "Tablero Kanban + Matriz HU (Agosto 21)) - Story Mapping.csv")
output_dir = os.path.join(base_dir, "Diagramas_SVG")
os.makedirs(output_dir, exist_ok=True)

macro_mapping = {
    "ROLES": "SEGURIDAD Y ACCESO",
    "PERMISOS": "SEGURIDAD Y ACCESO",
    "USUARIOS": "SEGURIDAD Y ACCESO",
    "ACCESO": "SEGURIDAD Y ACCESO",
    "CATEGORIA DE INSUMOS": "COMPRAS E INVENTARIO",
    "INSUMOS": "COMPRAS E INVENTARIO",
    "PROVEEDORES": "COMPRAS E INVENTARIO",
    "COMPRAS": "COMPRAS E INVENTARIO",
    "EMPLEADOS": "PRODUCCIÓN Y RECETAS",
    "CATEGORIA PRODUCTOS": "PRODUCCIÓN Y RECETAS",
    "PRODUCTOS": "PRODUCCIÓN Y RECETAS",
    "FICHA TECNICA \"PRODUCTO\"": "PRODUCCIÓN Y RECETAS",
    "PRODUCTO TERMINADO": "PRODUCCIÓN Y RECETAS",
    "PRODUCCION": "PRODUCCIÓN Y RECETAS",
    "CATEGORIA DE SERVICIOS": "SERVICIOS Y OPERACIÓN",
    "SERVICIO": "SERVICIOS Y OPERACIÓN",
    "CALENDARIO": "SERVICIOS Y OPERACIÓN",
    "CLIENTES": "CLIENTES Y VENTAS",
    "SUSCRIPCIONES": "CLIENTES Y VENTAS",
    "RUTA Y DOMICILIARIOS": "LOGÍSTICA Y DOMICILIOS",
    "MONITOREO DE ENTREGA \"TIEMPO REAL\"": "LOGÍSTICA Y DOMICILIOS",
    "INCIDENCIAS": "LOGÍSTICA Y DOMICILIOS",
    "DASHBOARD": "ANALÍTICA Y MÉTRICAS"
}

actor_mapping = {
    "ROLES": "Administrador",
    "PERMISOS": "Administrador",
    "USUARIOS": "Administrador",
    "ACCESO": "Usuario / Admin",
    "CATEGORIA DE INSUMOS": "Administrador",
    "INSUMOS": "Administrador",
    "PROVEEDORES": "Administrador",
    "COMPRAS": "Administrador",
    "EMPLEADOS": "Administrador",
    "CATEGORIA PRODUCTOS": "Jefe de Cocina",
    "PRODUCTOS": "Jefe de Cocina",
    "FICHA TECNICA \"PRODUCTO\"": "Jefe de Cocina",
    "PRODUCTO TERMINADO": "Jefe de Cocina",
    "PRODUCCION": "Jefe de Cocina",
    "CATEGORIA DE SERVICIOS": "Gestor Comercial",
    "SERVICIO": "Gestor Comercial",
    "CALENDARIO": "Administrador",
    "CLIENTES": "Gestor Comercial",
    "SUSCRIPCIONES": "Gestor Comercial",
    "RUTA Y DOMICILIARIOS": "Domiciliario",
    "MONITOREO DE ENTREGA \"TIEMPO REAL\"": "Logística",
    "INCIDENCIAS": "Logística",
    "DASHBOARD": "Administrador"
}

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
                    
                    if name.upper() == "ACCESO" and "consultar estado de la cuenta" in clean_val.lower():
                        continue
                    if name.upper() == "INSUMOS" and clean_val.lower() == "registrar salida de inventario":
                        continue
                    actions.append(clean_val)

        # For ROLES: strictly use the canonical 7 actions from the photo/matrix
        if name.upper() == "ROLES":
            actions = [
                "Crear rol",
                "Listar roles",
                "Ver detalle del rol",
                "Editar rol",
                "Asignar permisos",
                "Cambiar estado",
                "Eliminar rol"
            ]

        if actions:
            subprocesses.append({
                "title": name,
                "actions": actions
            })

def wrap_text(text, max_chars=22):
    words = text.split(' ')
    lines = []
    current_line = []
    current_len = 0
    for w in words:
        if current_len + len(w) > max_chars and current_line:
            lines.append(" ".join(current_line))
            current_line = [w]
            current_len = len(w)
        else:
            current_line.append(w)
            current_len += len(w) + 1
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def generate_svg_diagram(sp):
    raw_title = sp["title"]
    clean_title = raw_title.replace('"', '').strip()
    actions = sp["actions"]
    macro_name = macro_mapping.get(raw_title, macro_mapping.get(clean_title, "GESTIÓN GENERAL"))
    actor_name = actor_mapping.get(raw_title, actor_mapping.get(clean_title, "Administrador"))

    # Determine hub name
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

    # Custom layout for ACCESO
    if clean_title.upper() == "ACCESO":
        width = 1000
        height = 620
        actor_y = height / 2

        svg = []
        svg.append(f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">')
        svg.append(f'''  <defs>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="hubUcGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#fff7ed" />
    </linearGradient>
    <linearGradient id="ucGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#f8fafc" />
    </linearGradient>
    <marker id="extendArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ea580c" />
    </marker>
    <marker id="includeArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb" />
    </marker>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
    <filter id="pillShadow" x="-10%" y="-10%" width="120%" height="130%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.05" />
    </filter>
  </defs>

  <rect width="100%" height="100%" fill="#f8fafc" />
  <rect x="195" y="20" width="785" height="{height - 40}" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" filter="url(#cardShadow)" />
  <path d="M 195 36 Q 195 20 211 20 L 964 20 Q 980 20 980 36 L 980 72 L 195 72 Z" fill="url(#headerGrad)" />
  <text x="220" y="52" font-family="'Inter', -apple-system, sans-serif" font-size="15" font-weight="700" fill="#f8fafc" letter-spacing="0.5">
    SISTEMA JACKSOFT — {macro_name}
  </text>
  <rect x="805" y="33" width="155" height="26" rx="13" fill="#ea580c" />
  <text x="882" y="50" font-family="'Inter', -apple-system, sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">
    Subproceso: {clean_title}
  </text>

  <!-- Actor -->
  <rect x="20" y="{actor_y - 120}" width="155" height="240" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#cardShadow)" />
  <rect x="20" y="{actor_y - 120}" width="155" height="30" rx="12" fill="#f8fafc" />
  <text x="97" y="{actor_y - 100}" font-family="'Inter', -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle" letter-spacing="0.5">
    ACTOR PRINCIPAL
  </text>
  <circle cx="97" cy="{actor_y - 55}" r="18" fill="#fff7ed" stroke="#ea580c" stroke-width="2.2" />
  <line x1="97" y1="{actor_y - 37}" x2="97" y2="{actor_y + 15}" stroke="#0f172a" stroke-width="2.2" />
  <line x1="62" y1="{actor_y - 18}" x2="132" y2="{actor_y - 18}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" />
  <line x1="97" y1="{actor_y + 15}" x2="72" y2="{actor_y + 65}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" />
  <line x1="97" y1="{actor_y + 15}" x2="122" y2="{actor_y + 65}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" />
  <rect x="28" y="{actor_y + 78}" width="139" height="26" rx="13" fill="#ea580c" />
  <text x="97" y="{actor_y + 95}" font-family="'Inter', -apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#ffffff" text-anchor="middle">
    {actor_name}
  </text>
''')

        def draw_oval(cx, cy, text, rx=85, ry=26, is_hub=False):
            lines = wrap_text(text)
            grad = "url(#hubUcGrad)" if is_hub else "url(#ucGrad)"
            stroke = "#ea580c" if is_hub else "#0f172a"
            stroke_w = "2.2" if is_hub else "1.6"
            weight = "700" if is_hub else "600"
            svg.append(f'  <g filter="url(#pillShadow)"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{grad}" stroke="{stroke}" stroke-width="{stroke_w}" />')
            line_height = 14
            start_y = cy - ((len(lines) - 1) * line_height / 2) + 4
            for idx, line in enumerate(lines):
                ly = start_y + (idx * line_height)
                svg.append(f'  <text x="{cx}" y="{ly}" font-family="\'Inter\', sans-serif" font-size="12" font-weight="{weight}" fill="#0f172a" text-anchor="middle">{line}</text>')
            svg.append('  </g>')

        hub_x, hub_y = 320, actor_y
        login_x, login_y = 540, actor_y
        valid_x, valid_y = 780, actor_y
        recup_x, recup_y = 540, actor_y - 150
        close_x, close_y = 780, actor_y + 150

        draw_oval(hub_x, hub_y, "Acceso al sistema", rx=88, ry=30, is_hub=True)
        draw_oval(login_x, login_y, "Iniciar sesión", rx=82, ry=28, is_hub=True)
        draw_oval(valid_x, valid_y, "Validar credenciales", rx=88, ry=26)
        draw_oval(recup_x, recup_y, "Recuperar / restablecer contraseña", rx=105, ry=28)
        draw_oval(close_x, close_y, "Cerrar sesión", rx=82, ry=26)

        # Lines
        svg.append(f'  <line x1="175" y1="{actor_y}" x2="{hub_x - 88}" y2="{hub_y}" stroke="#0f172a" stroke-width="2" />')
        
        svg.append(f'  <line x1="{hub_x + 88}" y1="{hub_y}" x2="{login_x - 82}" y2="{login_y}" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
        svg.append(f'  <rect x="{(hub_x + login_x)/2 - 27}" y="{hub_y - 20}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
        svg.append(f'  <text x="{(hub_x + login_x)/2}" y="{hub_y - 8}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')

        svg.append(f'  <line x1="{login_x + 82}" y1="{login_y}" x2="{valid_x - 88}" y2="{valid_y}" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
        svg.append(f'  <rect x="{(login_x + valid_x)/2 - 27}" y="{login_y - 20}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
        svg.append(f'  <text x="{(login_x + valid_x)/2}" y="{login_y - 8}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')

        svg.append(f'  <line x1="{recup_x - 65}" y1="{recup_y + 22}" x2="{hub_x + 50}" y2="{hub_y - 25}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
        svg.append(f'  <rect x="{(recup_x + hub_x)/2 - 30}" y="{(recup_y + hub_y)/2 - 15}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
        svg.append(f'  <text x="{(recup_x + hub_x)/2 - 2}" y="{(recup_y + hub_y)/2 - 3}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')

        svg.append(f'  <line x1="{close_x - 60}" y1="{close_y - 20}" x2="{login_x + 60}" y2="{login_y + 22}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
        svg.append(f'  <rect x="{(close_x + login_x)/2 - 28}" y="{(close_y + login_y)/2 - 8}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
        svg.append(f'  <text x="{(close_x + login_x)/2}" y="{(close_y + login_y)/2 + 4}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')

        svg.append('</svg>')
        return "\n".join(svg)

    # Standard layout for all other subprocesses
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
            if name.lower().startswith("consultar") or name.lower().startswith("generar reportes") or name.lower().startswith("identificar"):
                central_action = name
                break

    for name in actions:
        if name == central_action:
            continue
        name_lower = name.lower()
        if not create_action and (name_lower.startswith("crear") or name_lower.startswith("registrar") or name_lower.startswith("exportar") or name_lower.startswith("parametrizar") or name_lower.startswith("cotizar")):
            create_action = name
        elif not search_action and (name_lower.startswith("buscar") or name_lower.startswith("filtrar")):
            search_action = name
        else:
            right_actions.append(name)

    num_right = len(right_actions)
    
    min_height = 660
    item_step = 62 if num_right > 6 else 75
    content_height = max(min_height, num_right * item_step + 170)
    
    width = 1000
    height = content_height

    actor_y = height / 2
    hub_x, hub_y = 320, height / 2
    central_x, central_y = 530, height / 2
    top_x, top_y = 530, 140
    right_x = 820

    svg = []
    svg.append(f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">')
    svg.append(f'''  <defs>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="hubUcGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#fff7ed" />
    </linearGradient>
    <linearGradient id="ucGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#f8fafc" />
    </linearGradient>
    <marker id="extendArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ea580c" />
    </marker>
    <marker id="includeArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb" />
    </marker>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
    <filter id="pillShadow" x="-10%" y="-10%" width="120%" height="130%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.05" />
    </filter>
  </defs>

  <rect width="100%" height="100%" fill="#f8fafc" />
  <rect x="195" y="20" width="785" height="{height - 40}" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" filter="url(#cardShadow)" />
  <path d="M 195 36 Q 195 20 211 20 L 964 20 Q 980 20 980 36 L 980 72 L 195 72 Z" fill="url(#headerGrad)" />
  <text x="220" y="52" font-family="'Inter', -apple-system, sans-serif" font-size="15" font-weight="700" fill="#f8fafc" letter-spacing="0.5">
    SISTEMA JACKSOFT — {macro_name}
  </text>
  <rect x="785" y="33" width="175" height="26" rx="13" fill="#ea580c" />
  <text x="872" y="50" font-family="'Inter', -apple-system, sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">
    Subproceso: {clean_title}
  </text>

  <!-- Actor -->
  <rect x="20" y="{actor_y - 120}" width="155" height="240" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#cardShadow)" />
  <rect x="20" y="{actor_y - 120}" width="155" height="30" rx="12" fill="#f8fafc" />
  <text x="97" y="{actor_y - 100}" font-family="'Inter', -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle" letter-spacing="0.5">
    ACTOR PRINCIPAL
  </text>
  <circle cx="97" cy="{actor_y - 55}" r="18" fill="#fff7ed" stroke="#ea580c" stroke-width="2.2" />
  <line x1="97" y1="{actor_y - 37}" x2="97" y2="{actor_y + 15}" stroke="#0f172a" stroke-width="2.2" />
  <line x1="62" y1="{actor_y - 18}" x2="132" y2="{actor_y - 18}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" />
  <line x1="97" y1="{actor_y + 15}" x2="72" y2="{actor_y + 65}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" />
  <line x1="97" y1="{actor_y + 15}" x2="122" y2="{actor_y + 65}" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" />
  <rect x="28" y="{actor_y + 78}" width="139" height="26" rx="13" fill="#ea580c" />
  <text x="97" y="{actor_y + 95}" font-family="'Inter', -apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#ffffff" text-anchor="middle">
    {actor_name}
  </text>
''')

    def draw_oval(cx, cy, text, rx=88, ry=26, is_hub=False):
        lines = wrap_text(text)
        grad = "url(#hubUcGrad)" if is_hub else "url(#ucGrad)"
        stroke = "#ea580c" if is_hub else "#0f172a"
        stroke_w = "2.2" if is_hub else "1.6"
        weight = "700" if is_hub else "600"
        svg.append(f'  <g filter="url(#pillShadow)"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{grad}" stroke="{stroke}" stroke-width="{stroke_w}" />')
        line_height = 14
        start_y = cy - ((len(lines) - 1) * line_height / 2) + 4
        for idx, line in enumerate(lines):
            ly = start_y + (idx * line_height)
            svg.append(f'  <text x="{cx}" y="{ly}" font-family="\'Inter\', sans-serif" font-size="12" font-weight="{weight}" fill="#0f172a" text-anchor="middle">{line}</text>')
        svg.append('  </g>')

    # Hub
    draw_oval(hub_x, hub_y, hub_name, rx=88, ry=30, is_hub=True)
    svg.append(f'  <line x1="175" y1="{actor_y}" x2="{hub_x - 88}" y2="{hub_y}" stroke="#0f172a" stroke-width="2" />')

    # Central Action
    if central_action:
        draw_oval(central_x, central_y, central_action, rx=84, ry=28, is_hub=True)
        svg.append(f'  <line x1="{hub_x + 88}" y1="{hub_y}" x2="{central_x - 84}" y2="{central_y}" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
        svg.append(f'  <rect x="{(hub_x + central_x)/2 - 27}" y="{hub_y - 24}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
        svg.append(f'  <text x="{(hub_x + central_x)/2}" y="{hub_y - 12}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')

    # Top Action (Crear)
    if create_action:
        draw_oval(top_x, top_y, create_action, rx=82, ry=26)
        svg.append(f'  <line x1="{top_x - 65}" y1="{top_y + 16}" x2="{hub_x + 45}" y2="{hub_y - 26}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
        svg.append(f'  <rect x="{(top_x + hub_x)/2 - 22}" y="{(top_y + hub_y)/2 - 24}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
        svg.append(f'  <text x="{(top_x + hub_x)/2 + 6}" y="{(top_y + hub_y)/2 - 12}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')

        if central_action:
            svg.append(f'  <line x1="{top_x}" y1="{top_y + 26}" x2="{central_x}" y2="{central_y - 28}" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
            svg.append(f'  <rect x="{top_x + 10}" y="{(top_y + central_y)/2 - 8}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
            svg.append(f'  <text x="{top_x + 37}" y="{(top_y + central_y)/2 + 4}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')

    # Right Actions
    if num_right > 0:
        start_y = 140
        end_y = height - 100
        step_y = (end_y - start_y) / max(1, num_right - 1) if num_right > 1 else (start_y + end_y)/2

        for idx, act_name in enumerate(right_actions):
            ry = start_y + (idx * step_y) if num_right > 1 else (start_y + end_y)/2
            draw_oval(right_x, ry, act_name, rx=88, ry=26)
            target_x = central_x if central_action else hub_x
            target_y = central_y if central_action else hub_y

            svg.append(f'  <line x1="{right_x - 88}" y1="{ry}" x2="{target_x + 84}" y2="{target_y}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
            
            t = 0.38
            lx = (right_x - 88) + t * ((target_x + 84) - (right_x - 88))
            ly = ry + t * (target_y - ry)
            svg.append(f'  <rect x="{lx - 28}" y="{ly - 8}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
            svg.append(f'  <text x="{lx}" y="{ly + 4}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')

    svg.append('</svg>')
    return "\n".join(svg)

for sp in subprocesses:
    svg_content = generate_svg_diagram(sp)
    safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', sp["title"]) + ".svg"
    path = os.path.join(output_dir, safe_name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Regenerated JackSoft SVG: {safe_name}")

print("All SVG diagrams successfully upgraded to JackSoft Design System!")

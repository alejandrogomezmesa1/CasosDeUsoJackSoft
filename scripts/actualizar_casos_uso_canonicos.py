import os
import re
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
svg_dir = os.path.join(base_dir, "Diagramas_SVG")
puml_dir = os.path.join(base_dir, "Diagramas_PUML")
png_dir = os.path.join(base_dir, "Diagramas_PNG")
html_path = os.path.join(base_dir, "Visor_Interactivo", "mapa_interactivo.html")

os.makedirs(svg_dir, exist_ok=True)
os.makedirs(puml_dir, exist_ok=True)
os.makedirs(png_dir, exist_ok=True)

canonical_subprocesses = [
    {
        "title": "ROLES",
        "safe_title": "ROLES",
        "macro": "Configuración y Seguridad",
        "macro_full": "SEGURIDAD Y ACCESO",
        "actor": "Administrador",
        "hub": "Gestión de roles",
        "actions": [
            "Crear rol",
            "Listar roles",
            "Ver detalle del rol",
            "Editar rol",
            "Asignar permisos",
            "Cambiar estado",
            "Eliminar rol"
        ]
    },
    {
        "title": "USUARIOS",
        "safe_title": "USUARIOS",
        "macro": "Configuración y Seguridad",
        "macro_full": "SEGURIDAD Y ACCESO",
        "actor": "Administrador",
        "hub": "Gestión de usuarios",
        "actions": [
            "Crear usuario",
            "Listar usuarios",
            "Generar reporte",
            "Ver detalle del usuario",
            "Editar usuario",
            "Cambiar estado",
            "Eliminar usuario",
            "Filtrar/Buscar usuario"
        ]
    },
    {
        "title": "ACCESO",
        "safe_title": "ACCESO",
        "macro": "Configuración y Seguridad",
        "macro_full": "SEGURIDAD Y ACCESO",
        "actor": "Usuario / Admin",
        "hub": "Acceso al sistema",
        "actions": [
            "Iniciar sesión",
            "Recuperar/Restablecer contraseña",
            "Consultar estado de la cuenta",
            "Cerrar sesión",
            "Generar reporte"
        ]
    },
    {
        "title": "CATEGORIA DE INSUMOS",
        "safe_title": "CATEGORIA_DE_INSUMOS",
        "macro": "Compras e Inventario",
        "macro_full": "COMPRAS E INVENTARIO",
        "actor": "Administrador",
        "hub": "Gestión de categorías de insumos",
        "actions": [
            "Crear categoría de insumo",
            "Listar categorías de insumos",
            "Ver detalle de la categoría",
            "Editar categoría",
            "Cambiar estado de la categoría",
            "Eliminar categoría",
            "Filtrar/Buscar categoría de insumo"
        ]
    },
    {
        "title": "INSUMOS",
        "safe_title": "INSUMOS",
        "macro": "Compras e Inventario",
        "macro_full": "COMPRAS E INVENTARIO",
        "actor": "Administrador",
        "hub": "Gestión de insumos",
        "actions": [
            "Crear insumo",
            "Listar insumos",
            "Ver detalle del insumo",
            "Editar insumo",
            "Cambiar estado del insumo",
            "Generar reporte de insumos",
            "Buscar Insumos",
            "Eliminar insumo"
        ]
    },
    {
        "title": "CATEGORIA PRODUCTOS",
        "safe_title": "CATEGORIA_PRODUCTOS",
        "macro": "Producción y Recetas",
        "macro_full": "PRODUCCIÓN Y RECETAS",
        "actor": "Jefe de Cocina",
        "hub": "Gestión de categorías de productos",
        "actions": [
            "Crear categoría de productos",
            "Listar categorías de productos",
            "Ver detalle de la categoría de productos",
            "Editar categoría de productos",
            "Cambiar estado de la categoría de productos",
            "Eliminar categoría de productos",
            "Buscar/Filtrar categorías de productos"
        ]
    },
    {
        "title": "PRODUCTOS",
        "safe_title": "PRODUCTOS",
        "macro": "Producción y Recetas",
        "macro_full": "PRODUCCIÓN Y RECETAS",
        "actor": "Jefe de Cocina",
        "hub": "Gestión de productos",
        "actions": [
            "Crear producto",
            "Listar productos",
            "Ver detalle del producto",
            "Editar producto",
            "Cambiar estado del producto",
            "Buscar productos",
            "Eliminar producto"
        ]
    },
    {
        "title": "PROVEEDORES",
        "safe_title": "PROVEEDORES",
        "macro": "Compras e Inventario",
        "macro_full": "COMPRAS E INVENTARIO",
        "actor": "Administrador",
        "hub": "Gestión de proveedores",
        "actions": [
            "Crear proveedor",
            "Listar proveedores",
            "Ver detalle del proveedor",
            "Editar proveedor",
            "Cambiar estado del proveedor",
            "Buscar proveedores",
            "Eliminar proveedor"
        ]
    },
    {
        "title": "COMPRAS",
        "safe_title": "COMPRAS",
        "macro": "Compras e Inventario",
        "macro_full": "COMPRAS E INVENTARIO",
        "actor": "Administrador",
        "hub": "Gestión de compras",
        "actions": [
            "Crear compra",
            "Listar compras",
            "Ver detalle de compra",
            "Editar compra",
            "Cambiar estado de compra",
            "Anular compra",
            "Generar reporte de compras",
            "Buscar compras"
        ]
    },
    {
        "title": "EMPLEADOS",
        "safe_title": "EMPLEADOS",
        "macro": "Producción y Recetas",
        "macro_full": "PRODUCCIÓN Y RECETAS",
        "actor": "Administrador",
        "hub": "Gestión de empleados",
        "actions": [
            "Crear empleado",
            "Listar empleados",
            "Generar reporte de empleados",
            "Ver detalle del empleado",
            "Editar empleado",
            "Cambiar estado del empleado",
            "Eliminar empleado",
            "Buscar empleados"
        ]
    },
    {
        "title": "PRODUCCION",
        "safe_title": "PRODUCCION",
        "macro": "Producción y Recetas",
        "macro_full": "PRODUCCIÓN Y RECETAS",
        "actor": "Jefe de Cocina",
        "hub": "Gestión de producción",
        "actions": [
            "Crear orden de producción",
            "Listar órdenes de producción",
            "Ver detalle de la orden de producción",
            "Editar orden de producción",
            "Cambiar estado de la orden de producción",
            "Programar producción",
            "Buscar producción"
        ]
    },
    {
        "title": "FICHA TECNICA \"PRODUCTO\"",
        "safe_title": "FICHA_TECNICA__PRODUCTO_",
        "macro": "Producción y Recetas",
        "macro_full": "PRODUCCIÓN Y RECETAS",
        "actor": "Jefe de Cocina",
        "hub": "Gestión de fichas técnicas",
        "actions": [
            "Crear ficha técnica de producto",
            "Listar fichas técnicas de producto",
            "Ver detalle de la ficha técnica de producto",
            "Editar ficha técnica de producto",
            "Buscar fichas técnicas de producto",
            "Generar reporte de fichas técnicas",
            "Eliminar ficha técnica de producto"
        ]
    },
    {
        "title": "PRODUCTO TERMINADO",
        "safe_title": "PRODUCTO_TERMINADO",
        "macro": "Producción y Recetas",
        "macro_full": "PRODUCCIÓN Y RECETAS",
        "actor": "Jefe de Cocina",
        "hub": "Gestión de producto terminado",
        "actions": [
            "Registrar producto terminado",
            "Listar productos terminados",
            "Ver detalle del producto terminado",
            "Editar producto terminado",
            "Buscar productos terminados",
            "Generar reporte de producto terminado"
        ]
    },
    {
        "title": "CATEGORIA DE SERVICIOS",
        "safe_title": "CATEGORIA_DE_SERVICIOS",
        "macro": "Servicios y Operación",
        "macro_full": "SERVICIOS Y OPERACIÓN",
        "actor": "Gestor Comercial",
        "hub": "Gestión de categorías de servicios",
        "actions": [
            "Crear categoría de servicios",
            "Listar categorías de servicios",
            "Editar categoría de servicios",
            "Cambiar estado de la categoría de servicios",
            "Eliminar categoría de servicios"
        ]
    },
    {
        "title": "SERVICIO",
        "safe_title": "SERVICIO",
        "macro": "Servicios y Operación",
        "macro_full": "SERVICIOS Y OPERACIÓN",
        "actor": "Gestor Comercial",
        "hub": "Gestión de servicios",
        "actions": [
            "Crear servicio",
            "Listar servicios",
            "Ver detalle del servicio",
            "Editar servicio",
            "Cambiar estado del servicio",
            "Filtrar servicios",
            "Eliminar servicio"
        ]
    },
    {
        "title": "CALENDARIO",
        "safe_title": "CALENDARIO",
        "macro": "Servicios y Operación",
        "macro_full": "SERVICIOS Y OPERACIÓN",
        "actor": "Administrador",
        "hub": "Gestión de calendario",
        "actions": [
            "Parametrizar calendario",
            "Listar calendario",
            "Ver detalle del calendario",
            "Generar reporte de calendario"
        ]
    },
    {
        "title": "CLIENTES",
        "safe_title": "CLIENTES",
        "macro": "Clientes y Ventas",
        "macro_full": "CLIENTES Y VENTAS",
        "actor": "Gestor Comercial",
        "hub": "Gestión de clientes",
        "actions": [
            "Crear cliente",
            "Listar clientes",
            "Generar reporte de clientes",
            "Ver detalle del cliente",
            "Editar cliente",
            "Cambiar estado del cliente",
            "Buscar/Filtrar clientes"
        ]
    },
    {
        "title": "SUSCRIPCIONES",
        "safe_title": "SUSCRIPCIONES",
        "macro": "Clientes y Ventas",
        "macro_full": "CLIENTES Y VENTAS",
        "actor": "Gestor Comercial",
        "hub": "Gestión de suscripciones",
        "actions": [
            "Cotizar suscripción",
            "Registrar suscripción",
            "Listar suscripciones",
            "Ver detalle de la suscripción",
            "Editar suscripción",
            "Cambiar estado de la suscripción",
            "Subir comprobante de suscripción",
            "Consultar comprobante de suscripción",
            "Buscar/Filtrar suscripciones"
        ]
    },
    {
        "title": "RUTA Y DOMICILIARIOS",
        "safe_title": "RUTA_Y_DOMICILIARIOS",
        "macro": "Logística y Domicilios",
        "macro_full": "LOGÍSTICA Y DOMICILIOS",
        "actor": "Domiciliario",
        "hub": "Gestión de rutas y domiciliarios",
        "actions": [
            "Crear asignacion de zonas",
            "Listar domiciliarios",
            "Ver detalle del domiciliario",
            "Ver estado",
            "Buscar/Filtrar domiciliarios"
        ]
    },
    {
        "title": "MONITOREO DE ENTREGA \"TIEMPO REAL\"",
        "safe_title": "MONITOREO_DE_ENTREGA__TIEMPO_REAL_",
        "macro": "Logística y Domicilios",
        "macro_full": "LOGÍSTICA Y DOMICILIOS",
        "actor": "Logística",
        "hub": "Monitoreo de entregas",
        "actions": [
            "Ver ubicación de domiciliarios en tiempo real",
            "Consultar avance de entregas en tiempo real",
            "Consultar estado de cocas en tiempo real",
            "Buscar entregas en tiempo real",
            "Generar reporte de entregas en tiempo real",
            "Crear zonas",
            "Editar zonas"
        ]
    },
    {
        "title": "INCIDENCIAS",
        "safe_title": "INCIDENCIAS",
        "macro": "Logística y Domicilios",
        "macro_full": "LOGÍSTICA Y DOMICILIOS",
        "actor": "Logística",
        "hub": "Gestión de incidencias",
        "actions": [
            "Registrar incidencia",
            "Listar incidencias",
            "Ver detalle de la incidencia",
            "Editar incidencia",
            "Gestionar incidencia",
            "Filtrar incidencias"
        ]
    },
    {
        "title": "DASHBOARD",
        "safe_title": "DASHBOARD",
        "macro": "Analítica y Métricas",
        "macro_full": "ANALÍTICA Y MÉTRICAS",
        "actor": "Administrador",
        "hub": "Dashboard",
        "actions": [
            "Consultar indicadores del dashboard",
            "Visualizar gráficos del dashboard",
            "Filtrar datos del dashboard",
            "Generar reporte del dashboard"
        ]
    }
]

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

def generate_svg(sp):
    title = sp["title"]
    clean_title = title.replace('"', '').strip()
    actions = sp["actions"]
    macro_name = sp["macro_full"]
    actor_name = sp["actor"]
    hub_name = sp["hub"]

    # Special handling for ACCESO
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

        hub_x, hub_y = 320, actor_y
        login_x, login_y = 540, actor_y
        valid_x, valid_y = 780, actor_y
        recup_x, recup_y = 540, actor_y - 150
        report_x, report_y = 540, actor_y + 150
        close_x, close_y = 780, actor_y + 150

        draw_oval(hub_x, hub_y, "Acceso al sistema", rx=88, ry=30, is_hub=True)
        draw_oval(login_x, login_y, "Iniciar sesión", rx=82, ry=28, is_hub=True)
        draw_oval(valid_x, valid_y, "Consultar estado de la cuenta", rx=98, ry=26)
        draw_oval(recup_x, recup_y, "Recuperar/Restablecer contraseña", rx=105, ry=28)
        draw_oval(report_x, report_y, "Generar reporte", rx=82, ry=26)
        draw_oval(close_x, close_y, "Cerrar sesión", rx=82, ry=26)

        # Lines
        svg.append(f'  <line x1="175" y1="{actor_y}" x2="{hub_x - 88}" y2="{hub_y}" stroke="#0f172a" stroke-width="2" />')
        
        svg.append(f'  <line x1="{hub_x + 88}" y1="{hub_y}" x2="{login_x - 82}" y2="{login_y}" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
        svg.append(f'  <rect x="{(hub_x + login_x)/2 - 27}" y="{hub_y - 20}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
        svg.append(f'  <text x="{(hub_x + login_x)/2}" y="{hub_y - 8}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')

        svg.append(f'  <line x1="{login_x + 82}" y1="{login_y}" x2="{valid_x - 98}" y2="{valid_y}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
        svg.append(f'  <rect x="{(login_x + valid_x)/2 - 28}" y="{login_y - 20}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
        svg.append(f'  <text x="{(login_x + valid_x)/2}" y="{login_y - 8}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')

        svg.append(f'  <line x1="{recup_x - 65}" y1="{recup_y + 22}" x2="{hub_x + 50}" y2="{hub_y - 25}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
        svg.append(f'  <rect x="{(recup_x + hub_x)/2 - 30}" y="{(recup_y + hub_y)/2 - 15}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
        svg.append(f'  <text x="{(recup_x + hub_x)/2 - 2}" y="{(recup_y + hub_y)/2 - 3}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')

        svg.append(f'  <line x1="{report_x - 65}" y1="{report_y - 20}" x2="{hub_x + 50}" y2="{hub_y + 25}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
        svg.append(f'  <rect x="{(report_x + hub_x)/2 - 30}" y="{(report_y + hub_y)/2 - 2}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
        svg.append(f'  <text x="{(report_x + hub_x)/2 - 2}" y="{(report_y + hub_y)/2 + 10}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')

        svg.append(f'  <line x1="{report_x}" y1="{report_y - 26}" x2="{login_x}" y2="{login_y + 28}" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
        svg.append(f'  <rect x="{report_x - 27}" y="{(report_y + login_y)/2 - 8}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
        svg.append(f'  <text x="{report_x}" y="{(report_y + login_y)/2 + 4}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')

        svg.append(f'  <line x1="{close_x - 60}" y1="{close_y - 20}" x2="{login_x + 60}" y2="{login_y + 22}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
        svg.append(f'  <rect x="{(close_x + login_x)/2 - 28}" y="{(close_y + login_y)/2 - 8}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
        svg.append(f'  <text x="{(close_x + login_x)/2}" y="{(close_y + login_y)/2 + 4}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')

        svg.append('</svg>')
        return "\n".join(svg)

    # Standard & Generalized Layout for all subprocesses (except ACCESO)
    central_action = None
    top_actions = []
    bottom_actions = []
    right_actions = []
    report_actions = []

    for name in actions:
        if name.lower().startswith("listar"):
            central_action = name
            break
    if not central_action:
        for name in actions:
            if name.lower().startswith("consultar") or name.lower().startswith("visualizar"):
                central_action = name
                break

    for name in actions:
        if name == central_action:
            continue
        nl = name.lower()
        if "buscar" in nl or "filtrar" in nl:
            bottom_actions.append(name)
        elif "reporte" in nl or "exportar" in nl:
            report_actions.append(name)
        elif nl.startswith("crear") or nl.startswith("registrar") or nl.startswith("parametrizar") or nl.startswith("cotizar") or nl.startswith("visualizar"):
            top_actions.append(name)
        else:
            right_actions.append(name)

    # Distribute report / export actions
    for r in report_actions:
        if len(top_actions) < 2:
            top_actions.append(r)
        else:
            bottom_actions.append(r)

    num_right = len(right_actions)
    min_height = 660
    item_step = 62 if num_right > 6 else 75
    content_height = max(min_height, num_right * item_step + 170)

    width = 1000
    height = content_height

    actor_y = height / 2
    hub_x, hub_y = 320, height / 2
    central_x, central_y = 530, height / 2

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

    # Top Actions (Crear, Reportes, Exportar)
    if len(top_actions) == 1:
        top_x, top_y = 530, 130
        draw_oval(top_x, top_y, top_actions[0], rx=82, ry=26)
        # To Hub
        svg.append(f'  <line x1="{top_x - 65}" y1="{top_y + 16}" x2="{hub_x + 45}" y2="{hub_y - 26}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
        svg.append(f'  <rect x="{(top_x + hub_x)/2 - 22}" y="{(top_y + hub_y)/2 - 24}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
        svg.append(f'  <text x="{(top_x + hub_x)/2 + 6}" y="{(top_y + hub_y)/2 - 12}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')
        # To Central
        if central_action:
            svg.append(f'  <line x1="{top_x}" y1="{top_y + 26}" x2="{central_x}" y2="{central_y - 28}" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
            svg.append(f'  <rect x="{top_x + 10}" y="{(top_y + central_y)/2 - 8}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
            svg.append(f'  <text x="{top_x + 37}" y="{(top_y + central_y)/2 + 4}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')
    elif len(top_actions) >= 2:
        cx0, cy0 = 440, 130
        cx1, cy1 = 625, 130
        draw_oval(cx0, cy0, top_actions[0], rx=82, ry=26)
        draw_oval(cx1, cy1, top_actions[1], rx=82, ry=26)
        # Action 0 to Hub
        svg.append(f'  <line x1="{cx0 - 55}" y1="{cy0 + 16}" x2="{hub_x + 40}" y2="{hub_y - 26}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
        svg.append(f'  <rect x="{(cx0 + hub_x)/2 - 24}" y="{(cy0 + hub_y)/2 - 24}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
        svg.append(f'  <text x="{(cx0 + hub_x)/2 + 4}" y="{(cy0 + hub_y)/2 - 12}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')
        # Action 0 to Central
        if central_action:
            svg.append(f'  <line x1="{cx0 + 25}" y1="{cy0 + 24}" x2="{central_x - 20}" y2="{central_y - 26}" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
            svg.append(f'  <rect x="{(cx0 + central_x)/2 - 27}" y="{(cy0 + central_y)/2 - 8}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
            svg.append(f'  <text x="{(cx0 + central_x)/2}" y="{(cy0 + central_y)/2 + 4}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')
        # Action 1 to Central
        if central_action:
            svg.append(f'  <line x1="{cx1 - 25}" y1="{cy1 + 24}" x2="{central_x + 20}" y2="{central_y - 26}" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
            svg.append(f'  <rect x="{(cx1 + central_x)/2 - 27}" y="{(cy1 + central_y)/2 - 8}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
            svg.append(f'  <text x="{(cx1 + central_x)/2}" y="{(cy1 + central_y)/2 + 4}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')

    # Bottom Actions (Buscar, Filtrar)
    if len(bottom_actions) == 1:
        bot_x, bot_y = 530, height - 130
        draw_oval(bot_x, bot_y, bottom_actions[0], rx=88, ry=26)
        # To Hub
        svg.append(f'  <line x1="{bot_x - 65}" y1="{bot_y - 16}" x2="{hub_x + 45}" y2="{hub_y + 26}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
        svg.append(f'  <rect x="{(bot_x + hub_x)/2 - 22}" y="{(bot_y + hub_y)/2 + 8}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
        svg.append(f'  <text x="{(bot_x + hub_x)/2 + 6}" y="{(bot_y + hub_y)/2 + 20}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')
        # To Central
        if central_action:
            svg.append(f'  <line x1="{bot_x}" y1="{bot_y - 26}" x2="{central_x}" y2="{central_y + 28}" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
            svg.append(f'  <rect x="{bot_x + 10}" y="{(bot_y + central_y)/2 - 8}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
            svg.append(f'  <text x="{bot_x + 37}" y="{(bot_y + central_y)/2 + 4}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')
    elif len(bottom_actions) >= 2:
        cx0, cy0 = 440, height - 130
        cx1, cy1 = 625, height - 130
        draw_oval(cx0, cy0, bottom_actions[0], rx=88, ry=26)
        draw_oval(cx1, cy1, bottom_actions[1], rx=88, ry=26)
        # Action 0 to Hub
        svg.append(f'  <line x1="{cx0 - 55}" y1="{cy0 - 16}" x2="{hub_x + 40}" y2="{hub_y + 26}" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#extendArrow)" />')
        svg.append(f'  <rect x="{(cx0 + hub_x)/2 - 24}" y="{(cy0 + hub_y)/2 + 8}" width="56" height="17" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="1" />')
        svg.append(f'  <text x="{(cx0 + hub_x)/2 + 4}" y="{(cy0 + hub_y)/2 + 20}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#c2410c" text-anchor="middle">«extend»</text>')
        # Action 0 to Central
        if central_action:
            svg.append(f'  <line x1="{cx0 + 25}" y1="{cy0 - 24}" x2="{central_x - 20}" y2="{central_y + 26}" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
            svg.append(f'  <rect x="{(cx0 + central_x)/2 - 27}" y="{(cy0 + central_y)/2 - 8}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
            svg.append(f'  <text x="{(cx0 + central_x)/2}" y="{(cy0 + central_y)/2 + 4}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')
        # Action 1 to Central
        if central_action:
            svg.append(f'  <line x1="{cx1 - 25}" y1="{cy1 - 24}" x2="{central_x + 20}" y2="{central_y + 26}" stroke="#2563eb" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#includeArrow)" />')
            svg.append(f'  <rect x="{(cx1 + central_x)/2 - 27}" y="{(cy1 + central_y)/2 - 8}" width="54" height="17" rx="8" fill="#ffffff" stroke="#bfdbfe" stroke-width="1" />')
            svg.append(f'  <text x="{(cx1 + central_x)/2}" y="{(cy1 + central_y)/2 + 4}" font-family="\'Inter\', sans-serif" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">«include»</text>')

    # Right Actions (strictly row-level operations)
    if num_right > 0:
        right_x = 820
        start_y = 150
        end_y = height - 130
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

def generate_puml(sp):
    title = sp["title"]
    clean_title = title.replace('"', '').strip()
    actions = sp["actions"]
    macro_name = sp["macro_full"]
    actor_name = sp["actor"]
    hub_name = sp["hub"]

    puml = []
    puml.append("@startuml")
    puml.append("left to right direction")
    puml.append("skinparam packageStyle rectangle")
    puml.append("skinparam nodesep 50")
    puml.append("skinparam ranksep 70")
    puml.append("skinparam shadowing true")
    puml.append('skinparam defaultFontName "Inter, Arial, sans-serif"')
    puml.append("")
    puml.append("skinparam actor {")
    puml.append("  BorderColor #0f172a")
    puml.append("  BackgroundColor #fff7ed")
    puml.append("}")
    puml.append("")
    puml.append("skinparam usecase {")
    puml.append("  BackgroundColor #ffffff")
    puml.append("  BorderColor #0f172a")
    puml.append("  ArrowColor #ea580c")
    puml.append("}")
    puml.append("")
    puml.append("skinparam usecase<<hub>> {")
    puml.append("  BackgroundColor #fff7ed")
    puml.append("  BorderColor #ea580c")
    puml.append("}")
    puml.append("")
    puml.append(f'actor "{actor_name}" as actor_user')
    puml.append("")
    puml.append(f'rectangle "SISTEMA JACKSOFT — {macro_name} ({clean_title})" {{')
    puml.append(f'  usecase "{hub_name}" as UC_Hub <<hub>>')

    if clean_title.upper() == "ACCESO":
        puml.append('  usecase "Iniciar sesión" as UC_Login <<hub>>')
        puml.append('  usecase "Recuperar/Restablecer contraseña" as UC_Recup')
        puml.append('  usecase "Consultar estado de la cuenta" as UC_Estado')
        puml.append('  usecase "Cerrar sesión" as UC_Logout')
        puml.append('  usecase "Generar reporte" as UC_Reporte')
        puml.append("}")
        puml.append("")
        puml.append("actor_user --> UC_Hub")
        puml.append("UC_Hub .> UC_Login : <<include>>")
        puml.append("UC_Recup ..> UC_Hub : <<extend>>")
        puml.append("UC_Estado ..> UC_Login : <<extend>>")
        puml.append("UC_Logout ..> UC_Login : <<extend>>")
        puml.append("UC_Reporte ..> UC_Hub : <<extend>>")
        puml.append("UC_Reporte .> UC_Login : <<include>>")
        puml.append("@enduml")
        return "\n".join(puml)

    central_action = None
    top_actions = []
    bottom_actions = []
    right_actions = []
    report_actions = []

    for name in actions:
        if name.lower().startswith("listar"):
            central_action = name
            break
    if not central_action:
        for name in actions:
            if name.lower().startswith("consultar") or name.lower().startswith("visualizar"):
                central_action = name
                break

    for name in actions:
        if name == central_action:
            continue
        nl = name.lower()
        if "buscar" in nl or "filtrar" in nl:
            bottom_actions.append(name)
        elif "reporte" in nl or "exportar" in nl:
            report_actions.append(name)
        elif nl.startswith("crear") or nl.startswith("registrar") or nl.startswith("parametrizar") or nl.startswith("cotizar") or nl.startswith("visualizar"):
            top_actions.append(name)
        else:
            right_actions.append(name)

    for r in report_actions:
        if len(top_actions) < 2:
            top_actions.append(r)
        else:
            bottom_actions.append(r)

    if central_action:
        puml.append(f'  usecase "{central_action}" as UC_Central <<hub>>')
    for idx, act in enumerate(top_actions):
        puml.append(f'  usecase "{act}" as UC_Top{idx+1}')
    for idx, act in enumerate(bottom_actions):
        puml.append(f'  usecase "{act}" as UC_Bot{idx+1}')
    for idx, act in enumerate(right_actions):
        puml.append(f'  usecase "{act}" as UC_R{idx+1}')

    puml.append("}")
    puml.append("")
    puml.append("actor_user --> UC_Hub")
    if central_action:
        puml.append("UC_Hub .> UC_Central : <<include>>")
    for idx in range(len(top_actions)):
        if idx == 0:
            puml.append(f"UC_Top{idx+1} ..> UC_Hub : <<extend>>")
        if central_action:
            puml.append(f"UC_Top{idx+1} .> UC_Central : <<include>>")
    for idx in range(len(bottom_actions)):
        if idx == 0:
            puml.append(f"UC_Bot{idx+1} ..> UC_Hub : <<extend>>")
        if central_action:
            puml.append(f"UC_Bot{idx+1} .> UC_Central : <<include>>")
    for idx in range(len(right_actions)):
        target = "UC_Central" if central_action else "UC_Hub"
        puml.append(f"UC_R{idx+1} ..> {target} : <<extend>>")

    puml.append("@enduml")
    return "\n".join(puml)

# Generate SVGs and PUMLs
svg_map = {}
for sp in canonical_subprocesses:
    safe_name = sp["safe_title"]
    
    # SVG
    svg_content = generate_svg(sp)
    svg_file = os.path.join(svg_dir, safe_name + ".svg")
    with open(svg_file, "w", encoding="utf-8") as f:
        f.write(svg_content)
    svg_map[sp["title"]] = svg_content
    
    # PUML
    puml_content = generate_puml(sp)
    puml_file = os.path.join(puml_dir, safe_name + ".puml")
    with open(puml_file, "w", encoding="utf-8") as f:
        f.write(puml_content)
        
    print(f"Generated SVG & PUML for: {safe_name}")

# Remove obsolete PERMISOS files if present
for obsolete in ["PERMISOS.svg", "PERMISOS.puml", "PERMISOS.png"]:
    fpath = os.path.join(base_dir, "Diagramas_" + obsolete.split('.')[1].upper(), obsolete)
    if os.path.exists(fpath):
        os.remove(fpath)
        print(f"Removed deprecated: {obsolete}")

print("All 22 canonical subprocesses successfully generated!")

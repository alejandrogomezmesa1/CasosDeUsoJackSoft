import json
import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
svg_dir = os.path.join(base_dir, "Diagramas_SVG")
png_dir = os.path.join(base_dir, "Diagramas_PNG")
output_html = os.path.join(base_dir, "Visor_Interactivo", "mapa_interactivo.html")

# Grouping Subprocesses by Macro-Process
macro_processes = {
    "Configuración y Seguridad": [
        "ROLES", "USUARIOS", "ACCESO"
    ],
    "Compras e Inventario": [
        "CATEGORIA DE INSUMOS", "INSUMOS", "PROVEEDORES", "COMPRAS"
    ],
    "Producción y Recetas": [
        "EMPLEADOS", "CATEGORIA PRODUCTOS", "PRODUCTOS", 
        "FICHA TECNICA \"PRODUCTO\"", "PRODUCTO TERMINADO", "PRODUCCION"
    ],
    "Servicios y Operación": [
        "CATEGORIA DE SERVICIOS", "SERVICIO", "CALENDARIO"
    ],
    "Clientes y Ventas": [
        "CLIENTES", "SUSCRIPCIONES"
    ],
    "Logística y Domicilios": [
        "RUTA Y DOMICILIARIOS", "MONITOREO DE ENTREGA \"TIEMPO REAL\"", "INCIDENCIAS"
    ],
    "Analítica y Métricas": [
        "DASHBOARD"
    ]
}

# Read SVG contents and build PNG maps
svg_map = {}
png_map = {}

for macro, sub_list in macro_processes.items():
    for sub in sub_list:
        safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', sub)
        clean_k = sub.replace('"', '').strip()
        
        # PNG mapping (filename only, path resolved dynamically in JS)
        png_filename = safe_name + ".png"
        
        png_map[sub] = png_filename
        png_map[clean_k] = png_filename
        png_map[safe_name] = png_filename
        png_map[clean_k.replace(' ', '_')] = png_filename

        # SVG mapping
        svg_path = os.path.join(svg_dir, safe_name + ".svg")
        if os.path.exists(svg_path):
            with open(svg_path, "r", encoding="utf-8") as f:
                content = f.read()
                svg_map[sub] = content
                svg_map[clean_k] = content
                svg_map[safe_name] = content
                svg_map[clean_k.replace(' ', '_')] = content
        else:
            print(f"Warning: SVG not found for {sub} at {svg_path}")

# Master Interactive Macro-Process SVG with Sober Brand Colors (Café y Blanco Cálido La Coca)
master_svg = '''
<svg width="860" height="520" viewBox="0 0 860 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="soberCardShadow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#2a170f" flood-opacity="0.12"/>
    </filter>
    <linearGradient id="masterHeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2a170f" />
      <stop offset="100%" stop-color="#422214" />
    </linearGradient>
  </defs>

  <!-- Container Box -->
  <rect x="20" y="20" width="820" height="480" rx="16" fill="#FFFDFB" stroke="#E2D7CC" stroke-width="2" filter="url(#soberCardShadow)"/>
  
  <!-- Header Bar -->
  <rect x="20" y="20" width="820" height="60" rx="16" fill="url(#masterHeaderGrad)"/>
  <rect x="20" y="64" width="820" height="16" fill="url(#masterHeaderGrad)"/>
  <text x="430" y="58" font-family="'Outfit', 'Inter', sans-serif" font-size="18" font-weight="700" fill="#FFF8F0" text-anchor="middle" letter-spacing="1">MAPA GENERAL DE MACRO-PROCESOS — LA COCA DE JACKS</text>

  <!-- Actor Admin -->
  <g transform="translate(90, 280)">
    <circle cx="0" cy="-45" r="22" fill="#FFFDFB" stroke="#C05621" stroke-width="3"/>
    <line x1="0" y1="-23" x2="0" y2="30" stroke="#2A170F" stroke-width="3"/>
    <line x1="-30" y1="-6" x2="30" y2="-6" stroke="#2A170F" stroke-width="3"/>
    <line x1="0" y1="30" x2="-25" y2="75" stroke="#2A170F" stroke-width="3"/>
    <line x1="0" y1="30" x2="25" y2="75" stroke="#2A170F" stroke-width="3"/>
    <rect x="-60" y="90" width="120" height="26" rx="13" fill="#C05621"/>
    <text x="0" y="107" font-family="'Outfit', 'Inter', sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">Administrador</text>
  </g>

  <!-- Connecting Lines -->
  <path d="M 120 280 L 250 135" fill="none" stroke="#D1C3B7" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 120 280 L 250 195" fill="none" stroke="#D1C3B7" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 120 280 L 250 255" fill="none" stroke="#D1C3B7" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 120 280 L 250 315" fill="none" stroke="#D1C3B7" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 120 280 L 250 375" fill="none" stroke="#D1C3B7" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M 120 280 L 250 435" fill="none" stroke="#D1C3B7" stroke-width="2" stroke-dasharray="4,4"/>

  <!-- Macro Process Cards (Clickable) -->
  <g class="macro-node" cursor="pointer" onclick="openDiagram('ROLES')">
    <rect x="230" y="112" width="310" height="46" rx="8" fill="#FAF6F0" stroke="#C05621" stroke-width="1.8" filter="url(#soberCardShadow)"/>
    <rect x="230" y="112" width="8" height="46" rx="4" fill="#C05621"/>
    <text x="248" y="140" font-family="'Outfit', 'Inter', sans-serif" font-size="12" font-weight="700" fill="#2A170F">1. Configuración y Seguridad</text>
    <text x="525" y="140" font-family="'Outfit', 'Inter', sans-serif" font-size="11" font-weight="600" fill="#C05621" text-anchor="end">3 C.U. ➔</text>
  </g>

  <g class="macro-node" cursor="pointer" onclick="openDiagram('COMPRAS')">
    <rect x="230" y="172" width="310" height="46" rx="8" fill="#FAF6F0" stroke="#8C4A28" stroke-width="1.8" filter="url(#soberCardShadow)"/>
    <rect x="230" y="172" width="8" height="46" rx="4" fill="#8C4A28"/>
    <text x="248" y="200" font-family="'Outfit', 'Inter', sans-serif" font-size="12" font-weight="700" fill="#2A170F">2. Compras e Inventario</text>
    <text x="525" y="200" font-family="'Outfit', 'Inter', sans-serif" font-size="11" font-weight="600" fill="#8C4A28" text-anchor="end">4 C.U. ➔</text>
  </g>

  <g class="macro-node" cursor="pointer" onclick="openDiagram('PRODUCCION')">
    <rect x="230" y="232" width="310" height="46" rx="8" fill="#FAF6F0" stroke="#A0522D" stroke-width="1.8" filter="url(#soberCardShadow)"/>
    <rect x="230" y="232" width="8" height="46" rx="4" fill="#A0522D"/>
    <text x="248" y="260" font-family="'Outfit', 'Inter', sans-serif" font-size="12" font-weight="700" fill="#2A170F">3. Producción y Recetas</text>
    <text x="525" y="260" font-family="'Outfit', 'Inter', sans-serif" font-size="11" font-weight="600" fill="#A0522D" text-anchor="end">6 C.U. ➔</text>
  </g>

  <g class="macro-node" cursor="pointer" onclick="openDiagram('CALENDARIO')">
    <rect x="230" y="292" width="310" height="46" rx="8" fill="#FAF6F0" stroke="#7A3E1D" stroke-width="1.8" filter="url(#soberCardShadow)"/>
    <rect x="230" y="292" width="8" height="46" rx="4" fill="#7A3E1D"/>
    <text x="248" y="320" font-family="'Outfit', 'Inter', sans-serif" font-size="12" font-weight="700" fill="#2A170F">4. Servicios y Operación</text>
    <text x="525" y="320" font-family="'Outfit', 'Inter', sans-serif" font-size="11" font-weight="600" fill="#7A3E1D" text-anchor="end">3 C.U. ➔</text>
  </g>

  <g class="macro-node" cursor="pointer" onclick="openDiagram('CLIENTES')">
    <rect x="230" y="352" width="310" height="46" rx="8" fill="#FAF6F0" stroke="#C05621" stroke-width="1.8" filter="url(#soberCardShadow)"/>
    <rect x="230" y="352" width="8" height="46" rx="4" fill="#C05621"/>
    <text x="248" y="380" font-family="'Outfit', 'Inter', sans-serif" font-size="12" font-weight="700" fill="#2A170F">5. Clientes y Ventas</text>
    <text x="525" y="380" font-family="'Outfit', 'Inter', sans-serif" font-size="11" font-weight="600" fill="#C05621" text-anchor="end">2 C.U. ➔</text>
  </g>

  <g class="macro-node" cursor="pointer" onclick="openDiagram('RUTA Y DOMICILIARIOS')">
    <rect x="230" y="412" width="310" height="46" rx="8" fill="#FAF6F0" stroke="#663319" stroke-width="1.8" filter="url(#soberCardShadow)"/>
    <rect x="230" y="412" width="8" height="46" rx="4" fill="#663319"/>
    <text x="248" y="440" font-family="'Outfit', 'Inter', sans-serif" font-size="12" font-weight="700" fill="#2A170F">6. Logística y Domicilios</text>
    <text x="525" y="440" font-family="'Outfit', 'Inter', sans-serif" font-size="11" font-weight="600" fill="#663319" text-anchor="end">3 C.U. ➔</text>
  </g>

  <!-- Right side: Central Intelligence Dashboard Card -->
  <path d="M 540 270 L 590 270" fill="none" stroke="#C05621" stroke-width="2" stroke-dasharray="4,4"/>
  <g class="macro-node" cursor="pointer" onclick="openDiagram('DASHBOARD')">
    <rect x="590" y="235" width="220" height="75" rx="12" fill="#2A170F" stroke="#C05621" stroke-width="2.2" filter="url(#soberCardShadow)"/>
    <text x="700" y="265" font-family="'Outfit', 'Inter', sans-serif" font-size="14" font-weight="800" fill="#FFF8F0" text-anchor="middle">7. DASHBOARD</text>
    <text x="700" y="285" font-family="'Outfit', 'Inter', sans-serif" font-size="11" font-weight="500" fill="#E2D7CC" text-anchor="middle">Analítica, Métricas & KPIs</text>
    <text x="700" y="300" font-family="'Outfit', 'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#C05621" text-anchor="middle">EXPLORAR INDICADORES ➔</text>
  </g>
</svg>
'''

# Build Interactive HTML Dashboard
html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JackSoft — Visor Canónico de Casos de Uso | La Coca de Jacks</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      /* Paleta Corporativa La Coca de Jacks (Sobria: Café y Blanco Cálido) */
      --bg-cream: #FAF6F0;          /* Blanco cálido con baño crema / marfil */
      --bg-cream-light: #FFFDFB;    /* Blanco casi puro cálido */
      --bg-cream-soft: #F4ECE1;     /* Crema suave / beige cálido */
      
      --coffee-black: #1E100A;      /* Café profundo de acento */
      --coffee-dark: #2A170F;       /* Café espresso corporativo */
      --coffee-medium: #4A2818;     /* Café tostado medio */
      --coffee-muted: #7A6658;      /* Café grisáceo para subtítulos */
      
      --coca-orange: #C05621;       /* Terracota / naranja tostado oficial */
      --coca-orange-light: #D5511A; /* Acento activo */
      --coca-orange-soft: rgba(192, 86, 33, 0.08);
      
      --border-warm: #E2D7CC;       /* Borde beige cálido */
      --border-light: #EFE6DC;      /* Borde suave */
      
      --shadow-sober: 0 10px 30px rgba(42, 23, 15, 0.07);
      --shadow-header: 0 4px 20px rgba(30, 16, 10, 0.15);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    body {{
      background: var(--bg-cream);
      color: var(--coffee-dark);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* Header Corporativo Sobrio */
    header {{
      background: linear-gradient(135deg, var(--coffee-dark) 0%, #381E13 100%);
      border-bottom: 2px solid var(--coca-orange);
      padding: 14px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-header);
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    /* Botón Plegar / Desplegar Menú */
    .toggle-sidebar-btn {{
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 248, 240, 0.25);
      border-radius: 8px;
      padding: 8px 14px;
      color: #FFF8F0;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}

    .toggle-sidebar-btn:hover {{
      background: var(--coca-orange);
      border-color: var(--coca-orange);
      transform: translateY(-1px);
    }}

    .brand-title {{
      display: flex;
      flex-direction: column;
    }}

    .brand-title h1 {{
      font-family: 'Outfit', sans-serif;
      font-size: 18px;
      font-weight: 700;
      color: #FFF8F0;
      letter-spacing: -0.01em;
    }}

    .brand-title .subtitle {{
      font-size: 12px;
      color: #D6C2B4;
      font-weight: 400;
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .btn-sober {{
      background: #FFFDFB;
      color: var(--coffee-dark);
      border: 1px solid var(--border-warm);
      border-radius: 8px;
      padding: 8px 14px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }}

    .btn-sober:hover {{
      background: var(--bg-cream-soft);
      border-color: var(--coca-orange);
      color: var(--coca-orange);
    }}

    /* Layout Principal */
    .app-container {{
      display: flex;
      flex: 1;
      height: calc(100vh - 66px);
      position: relative;
      overflow: hidden;
    }}

    /* Sidebar Plegable */
    .sidebar {{
      width: 320px;
      min-width: 320px;
      max-width: 320px;
      background: var(--bg-cream-light);
      border-right: 1px solid var(--border-warm);
      padding: 16px 14px;
      overflow-y: auto;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      z-index: 40;
      box-shadow: 2px 0 12px rgba(42, 23, 15, 0.03);
    }}

    /* Estado Colapsado */
    .sidebar.collapsed {{
      width: 0 !important;
      min-width: 0 !important;
      max-width: 0 !important;
      padding: 0 !important;
      border-right: none !important;
      opacity: 0;
      pointer-events: none;
    }}

    /* Botón flotante para reabrir menú cuando está colapsado */
    .floating-expand-btn {{
      position: absolute;
      bottom: 28px;
      left: 28px;
      z-index: 60;
      background: var(--coffee-dark);
      color: #FFF8F0;
      border: 1px solid var(--coca-orange);
      border-radius: 20px;
      padding: 9px 18px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      box-shadow: 0 6px 16px rgba(42, 23, 15, 0.22);
      display: none;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}

    .floating-expand-btn:hover {{
      background: var(--coca-orange);
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(192, 86, 33, 0.3);
    }}

    .sidebar.collapsed ~ .main-canvas .floating-expand-btn {{
      display: flex;
    }}

    /* Agrupaciones de Macroprocesos */
    .macro-group {{
      margin-bottom: 16px;
    }}

    .macro-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 8px;
      margin-bottom: 6px;
      font-family: 'Outfit', sans-serif;
      font-size: 11.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--coffee-medium);
      border-bottom: 1px dashed var(--border-warm);
    }}

    .sub-item {{
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: 6px;
      padding: 9px 12px;
      margin-bottom: 5px;
      font-size: 12.5px;
      font-weight: 500;
      color: var(--coffee-dark);
      cursor: pointer;
      transition: all 0.15s ease;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .sub-item:hover {{
      background: var(--bg-cream-soft);
      border-color: var(--border-warm);
      transform: translateX(2px);
    }}

    .sub-item.active {{
      background: var(--coca-orange-soft);
      border-color: var(--coca-orange);
      color: var(--coca-orange);
      font-weight: 700;
      border-left: 4px solid var(--coca-orange);
    }}

    .sub-item .pill-badge {{
      font-size: 10px;
      font-weight: 700;
      background: var(--bg-cream-soft);
      color: var(--coffee-medium);
      padding: 2px 6px;
      border-radius: 10px;
    }}

    .sub-item.active .pill-badge {{
      background: var(--coca-orange);
      color: #FFFFFF;
    }}

    /* Área Principal (Canvas del Visor) */
    .main-canvas {{
      flex: 1;
      display: flex;
      flex-direction: column;
      padding: 18px 22px;
      background: radial-gradient(circle at 50% 30%, #FFFDFB 0%, var(--bg-cream) 70%);
      overflow: hidden;
      position: relative;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .viewer-card {{
      background: #FFFFFF;
      border: 1px solid var(--border-warm);
      border-radius: 12px;
      width: 100%;
      height: 100%;
      box-shadow: var(--shadow-sober);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    /* Barra Superior del Visor */
    .viewer-toolbar {{
      background: #FAF6F0;
      border-bottom: 1px solid var(--border-warm);
      padding: 10px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}

    .viewer-title-box h2 {{
      font-family: 'Outfit', sans-serif;
      font-size: 15px;
      font-weight: 700;
      color: var(--coffee-dark);
    }}

    .viewer-title-box .viewer-desc {{
      font-size: 11.5px;
      color: var(--coffee-muted);
    }}

    /* Controles de Vista e Imagen */
    .viewer-controls {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .view-switch {{
      display: flex;
      background: var(--border-light);
      border-radius: 6px;
      padding: 2px;
    }}

    .switch-btn {{
      background: transparent;
      border: none;
      padding: 5px 10px;
      font-size: 11.5px;
      font-weight: 600;
      border-radius: 5px;
      cursor: pointer;
      color: var(--coffee-muted);
      transition: all 0.2s;
    }}

    .switch-btn.active {{
      background: #FFFFFF;
      color: var(--coffee-dark);
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}

    .zoom-group {{
      display: flex;
      gap: 4px;
    }}

    .zoom-btn {{
      background: #FFFFFF;
      border: 1px solid var(--border-warm);
      border-radius: 6px;
      width: 28px;
      height: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 13px;
      font-weight: 700;
      color: var(--coffee-dark);
      cursor: pointer;
      transition: background 0.15s;
    }}

    .zoom-btn:hover {{
      background: var(--bg-cream-soft);
      border-color: var(--coca-orange);
      color: var(--coca-orange);
    }}

    /* Contenedor del Diagrama */
    .viewer-content-area {{
      flex: 1;
      overflow: auto;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      padding: 24px;
      background: #FFFFFF;
      position: relative;
    }}

    /* Foto Oficial (PNG HD) */
    .diagram-photo {{
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
      border-radius: 8px;
      box-shadow: 0 4px 20px rgba(42, 23, 15, 0.05);
      transition: transform 0.2s ease;
      transform-origin: top center;
    }}

    /* Render Vectorial SVG */
    .viewer-content-area svg {{
      width: 100%;
      max-width: 1050px;
      height: auto;
      display: block;
      margin: 0 auto;
      transition: transform 0.2s ease;
      transform-origin: top center;
    }}

    .sidebar-edge-toggle {{
      position: absolute;
      top: 14px;
      right: -13px;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: #FFFFFF;
      border: 1px solid var(--border-warm);
      box-shadow: 0 2px 6px rgba(42, 23, 15, 0.12);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: var(--coffee-dark);
      z-index: 50;
      transition: all 0.2s ease;
    }}

    .sidebar-edge-toggle:hover {{
      background: var(--coca-orange);
      color: #FFFFFF;
      border-color: var(--coca-orange);
      transform: scale(1.1);
    }}

    .sidebar.collapsed .sidebar-edge-toggle {{
      display: none;
    }}

    /* Scrollbars elegantes y sobrios */
    ::-webkit-scrollbar {{
      width: 7px;
      height: 7px;
    }}
    ::-webkit-scrollbar-track {{
      background: var(--bg-cream);
    }}
    ::-webkit-scrollbar-thumb {{
      background: #D8CCC0;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
    }}
  </style>
</head>
<body>

  <!-- Header Superior Corporativo -->
  <header>
    <div class="header-left">
      <button class="toggle-sidebar-btn" id="header-toggle-btn" onclick="toggleSidebar()" title="Plegar / Desplegar barra de navegación">
        <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 6h16M4 12h16M4 18h16"></path></svg>
        <span id="toggle-label">Ocultar Menú</span>
      </button>

      <div class="brand-title">
        <h1>Sistema JackSoft — La Coca de Jacks</h1>
        <div class="subtitle">Visor Canónico de Procesos y Diagramas de Casos de Uso</div>
      </div>
    </div>

    <div class="header-right">
      <button class="btn-sober" onclick="showMasterMap()" title="Ver la arquitectura general del sistema">
        <svg width="15" height="15" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
        Mapa General
      </button>
      <a id="btn-open-external" href="#" target="_blank" class="btn-sober" title="Abrir imagen en resolución completa">
        <svg width="15" height="15" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
        Abrir HD
      </a>
    </div>
  </header>

  <!-- Contenedor Principal -->
  <div class="app-container">

    <!-- Sidebar de Navegación Plegable -->
    <aside class="sidebar" id="app-sidebar">
      <!-- Pestaña lateral para plegar -->
      <button class="sidebar-edge-toggle" onclick="toggleSidebar()" title="Plegar barra de menú">
        <svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"></path></svg>
      </button>
'''

for macro, sub_list in macro_processes.items():
    html_content += f'''
      <div class="macro-group">
        <div class="macro-header">
          <span>{macro}</span>
          <span style="font-size: 10px; opacity: 0.7;">{len(sub_list)}</span>
        </div>
'''
    for sub in sub_list:
        clean_sub = sub.replace('"', '').strip()
        safe_id = 'btn-' + clean_sub.replace(' ', '_')
        html_content += f'''
        <div class="sub-item" onclick="openDiagram('{clean_sub}')" id="{safe_id}">
          <span>{clean_sub}</span>
          <span class="pill-badge">UML</span>
        </div>
'''
    html_content += '      </div>'

html_content += f'''
    </aside>

    <!-- Canvas Principal del Visor -->
    <main class="main-canvas">
      
      <!-- Botón Flotante para reabrir cuando esté colapsado -->
      <button class="floating-expand-btn" id="floating-reopen-btn" onclick="toggleSidebar()">
        <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 6h16M4 12h16M4 18h16"></path></svg>
        <span>Mostrar Subprocesos</span>
      </button>

      <div class="viewer-card">
        <!-- Toolbar Superior -->
        <div class="viewer-toolbar">
          <div class="viewer-title-box">
            <h2 id="current-diagram-title">Diagrama de Casos de Uso</h2>
            <div class="viewer-desc" id="current-diagram-desc">Visualizando especificación oficial JackSoft</div>
          </div>

          <div class="viewer-controls">
            <!-- Alternador de Vista (Foto PNG vs Vectorial SVG) -->
            <div class="view-switch">
              <button class="switch-btn active" id="mode-btn-img" onclick="setMode('img')" title="Ver la foto del diagrama en alta definición">
                🖼️ Foto Oficial (PNG)
              </button>
              <button class="switch-btn" id="mode-btn-svg" onclick="setMode('svg')" title="Ver versión vectorial interactiva">
                📐 Vectorial (SVG)
              </button>
            </div>

            <!-- Controles de Zoom -->
            <div class="zoom-group">
              <button class="zoom-btn" onclick="adjustZoom(-0.15)" title="Reducir zoom">-</button>
              <button class="zoom-btn" onclick="resetZoom()" title="Restablecer tamaño">100%</button>
              <button class="zoom-btn" onclick="adjustZoom(0.15)" title="Aumentar zoom">+</button>
            </div>
          </div>
        </div>

        <!-- Área de Contenido -->
        <div class="viewer-content-area" id="viewer-container">
          <div class="macro-map-container" id="macro-map-content">
            {master_svg}
          </div>
        </div>
      </div>
    </main>
  </div>

  <script>
    // Almacén de Diagramas y Fotos
    const svgStore = {json.dumps(svg_map, ensure_ascii=False)};
    const pngStore = {json.dumps(png_map, ensure_ascii=False)};
    const masterMapSVG = `{master_svg}`;

    // Detección dinámica de la ruta base (raíz para GitHub Pages o subdirectorio)
    const isSubdir = window.location.pathname.includes('/Visor_Interactivo/');
    const pngBasePath = isSubdir ? '../Diagramas_PNG/' : './Diagramas_PNG/';

    function getPngPath(name) {{
      if (!name) return null;
      const clean = name.replace(/["']/g, '').trim();
      const fn = pngStore[name] || pngStore[clean] || pngStore[clean.replace(/ /g, '_')];
      return fn ? (pngBasePath + fn) : null;
    }}

    let currentSubprocess = 'ROLES';
    let currentMode = 'img'; // 'img' (usa las fotos) o 'svg'
    let currentZoom = 1.0;
    let isSidebarCollapsed = false;

    // Toggle para Plegar / Desplegar el Navbar
    function toggleSidebar() {{
      const sidebar = document.getElementById('app-sidebar');
      const toggleLabel = document.getElementById('toggle-label');
      isSidebarCollapsed = !isSidebarCollapsed;

      if (isSidebarCollapsed) {{
        sidebar.classList.add('collapsed');
        if (toggleLabel) toggleLabel.innerText = 'Mostrar Menú';
      }} else {{
        sidebar.classList.remove('collapsed');
        if (toggleLabel) toggleLabel.innerText = 'Ocultar Menú';
      }}
    }}

    // Cambiar modo entre Foto PNG y SVG Vectorial
    function setMode(mode) {{
      currentMode = mode;
      document.getElementById('mode-btn-img').classList.toggle('active', mode === 'img');
      document.getElementById('mode-btn-svg').classList.toggle('active', mode === 'svg');
      renderCurrentView();
    }}

    // Ajustar Zoom
    function adjustZoom(delta) {{
      currentZoom = Math.max(0.5, Math.min(2.5, currentZoom + delta));
      applyZoom();
    }}

    function resetZoom() {{
      currentZoom = 1.0;
      applyZoom();
    }}

    function applyZoom() {{
      const img = document.getElementById('active-diagram-photo');
      const svg = document.querySelector('#viewer-container svg');
      if (img) img.style.transform = `scale(${{currentZoom}})`;
      if (svg) svg.style.transform = `scale(${{currentZoom}})`;
    }}

    // Abrir un Subproceso específico
    function openDiagram(subName) {{
      currentSubprocess = subName;
      const cleanName = subName.replace(/["']/g, '').trim();
      const safeId = 'btn-' + cleanName.replace(/ /g, '_');

      // Actualizar botón activo en la barra lateral
      document.querySelectorAll('.sub-item').forEach(el => el.classList.remove('active'));
      const activeBtn = document.getElementById(safeId) || document.getElementById('btn-' + subName.replace(/ /g, '_'));
      if (activeBtn) activeBtn.classList.add('active');

      // Actualizar títulos
      document.getElementById('current-diagram-title').innerText = 'Subproceso: ' + cleanName;
      document.getElementById('current-diagram-desc').innerText = 'Especificación y diagrama oficial de casos de uso — La Coca de Jacks';

      // Actualizar link a imagen HD
      const pngPath = getPngPath(subName) || getPngPath(cleanName);
      if (pngPath) {{
        document.getElementById('btn-open-external').href = pngPath;
      }}

      // Resetear zoom y renderizar
      currentZoom = 1.0;
      renderCurrentView();
      
      // Actualizar hash en URL sin recargar
      window.location.hash = encodeURIComponent(cleanName);
    }}

    // Renderizar según el modo seleccionado (Foto PNG o SVG)
    function renderCurrentView() {{
      const container = document.getElementById('viewer-container');
      const cleanName = currentSubprocess.replace(/["']/g, '').trim();

      if (currentSubprocess === 'MASTER_MAP') {{
        container.innerHTML = masterMapSVG;
        return;
      }}

      const pngPath = getPngPath(currentSubprocess) || getPngPath(cleanName);
      const svgContent = svgStore[currentSubprocess] || svgStore[cleanName] || svgStore[cleanName.replace(/ /g, '_')];

      if (currentMode === 'img' && pngPath) {{
        // "Usa las mismas fotos" (renderizado HD en PNG)
        container.innerHTML = `<img src="${{pngPath}}" alt="${{cleanName}}" class="diagram-photo" id="active-diagram-photo" />`;
      }} else if (svgContent) {{
        // Render vectorial
        container.innerHTML = svgContent;
      }} else if (pngPath) {{
        container.innerHTML = `<img src="${{pngPath}}" alt="${{cleanName}}" class="diagram-photo" id="active-diagram-photo" />`;
      }} else {{
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--coffee-muted);"><p>Diagrama no encontrado.</p></div>';
      }}

      applyZoom();
    }}

    // Mostrar el Mapa General
    function showMasterMap() {{
      currentSubprocess = 'MASTER_MAP';
      document.querySelectorAll('.sub-item').forEach(el => el.classList.remove('active'));
      document.getElementById('current-diagram-title').innerText = 'Mapa General de Macro-Procesos';
      document.getElementById('current-diagram-desc').innerText = 'Vista panorámica de la arquitectura del sistema JackSoft';
      document.getElementById('btn-open-external').href = pngBasePath + 'MAPA_GENERAL_CASOS_DE_USO.png';
      window.location.hash = 'MASTER_MAP';
      renderCurrentView();
    }}

    // Carga inicial
    window.addEventListener('DOMContentLoaded', () => {{
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.get('collapsed') === 'true') {{
        toggleSidebar();
      }}

      const hash = decodeURIComponent(window.location.hash.substring(1));
      if (hash === 'MASTER_MAP') {{
        showMasterMap();
      }} else if (hash && (svgStore[hash] || pngStore[hash])) {{
        openDiagram(hash);
      }} else {{
        openDiagram('ROLES');
      }}
    }});

    // Atajo de teclado: presionar 'm' o 'p' para plegar/desplegar menú
    window.addEventListener('keydown', (e) => {{
      if ((e.key === 'm' || e.key === 'M' || e.key === 'p' || e.key === 'P') && !e.target.matches('input, textarea')) {{
        toggleSidebar();
      }}
    }});
  </script>
</body>
</html>
'''

targets = [
    os.path.join(base_dir, "index.html"),
    os.path.join(base_dir, "Visor_Interactivo", "index.html"),
    os.path.join(base_dir, "Visor_Interactivo", "mapa_interactivo.html"),
]

for target_file in targets:
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Interactive Dashboard created at {target_file}")

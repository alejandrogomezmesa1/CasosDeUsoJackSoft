import csv
import os
import re

csv_file = "/Users/alejo/Proyectos/MapaMental/Tablero Kanban + Matriz HU (Agosto 21)) - Story Mapping.csv"
output_svg = "/Users/alejo/Proyectos/MapaMental/mapa_interactivo.svg"
svg_dir = "/Users/alejo/Proyectos/MapaMental/diagramas_casos_uso_svg"

# Títulos EXACTOS como están en 'formato ficha proyecto 14agosto.md' (Línea 28)
macro_processes = {
    "configuracion": {
        "title": "Proceso de Configuración",
        "subs": ["ROLES", "PERMISOS"]
    },
    "usuarios": {
        "title": "Proceso de Usuarios",
        "subs": ["USUARIOS", "ACCESO"]
    },
    "compras": {
        "title": "Proceso de Compras",
        "subs": ["CATEGORIA DE INSUMOS", "INSUMOS", "CATEGORIA PRODUCTOS", "PRODUCTOS", "PROVEEDORES", "COMPRAS"]
    },
    "produccion": {
        "title": "Proceso de Producción",
        "subs": ["EMPLEADOS", "PRODUCCION", "FICHA TECNICA \"PRODUCTO\"", "PRODUCTO TERMINADO"]
    },
    "servicios": {
        "title": "Proceso de Servicios",
        "subs": ["CATEGORIA DE SERVICIOS", "SERVICIO", "CALENDARIO"]
    },
    "ventas": {
        "title": "Proceso de Ventas",
        "subs": ["CLIENTES", "SUSCRIPCIONES"]
    },
    "logistica": {
        "title": "Proceso de Logística (Servicios Web)",
        "subs": ["RUTA Y DOMICILIARIOS", "MONITOREO DE ENTREGA \"TIEMPO REAL\"", "INCIDENCIAS"]
    },
    "analitica": {
        "title": "Proceso de medición y desempeño de los procesos (dashboard)",
        "subs": ["DASHBOARD"]
    }
}

# Read Phase 3 SVGs and their actual height attributes
phase3_svgs = {}
phase3_heights = {}

for macro, data in macro_processes.items():
    for sub in data["subs"]:
        safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', sub) + ".svg"
        path = os.path.join(svg_dir, safe_name)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                
                # Extract height attribute
                h_match = re.search(r'height="(\d+)"', content)
                h_val = int(h_match.group(1)) if h_match else 650
                phase3_heights[sub] = h_val
                
                # Extract inner content
                inner = re.sub(r'^<svg[^>]*>', '', content)
                inner = re.sub(r'</svg>\s*$', '', inner)
                phase3_svgs[sub] = inner

# Dynamic canvas height based on max height required across diagrams
max_diag_height = max(phase3_heights.values()) if phase3_heights else 1500
master_height = max(800, max_diag_height + 100)
width = 1050

svg = []
svg.append(f'<svg width="{width}" height="{master_height}" viewBox="0 0 {width} {master_height}" xmlns="http://www.w3.org/2000/svg">')

svg.append('''
  <defs>
    <marker id="arrow-master" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#333333" />
    </marker>
    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.12"/>
    </filter>
  </defs>

  <style>
    .bg { fill: #f8fafc; }
    .title-main { font-family: Arial, sans-serif; font-size: 17px; font-weight: bold; fill: #0f172a; text-anchor: middle; }
    .subtitle-main { font-family: Arial, sans-serif; font-size: 12px; fill: #64748b; text-anchor: middle; }
    .boundary { fill: #ffffff; stroke: #cbd5e1; stroke-width: 2; rx: 12; }
    
    .actor { fill: none; stroke: #1e293b; stroke-width: 2.5; }
    .actor-text { font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; fill: #0f172a; text-anchor: middle; }
    
    .btn-proc { fill: #ffffff; stroke: #2563eb; stroke-width: 2; rx: 8; cursor: pointer; }
    .btn-proc:hover { fill: #eff6ff; stroke: #1d4ed8; }
    .btn-proc-text { font-family: Arial, sans-serif; font-size: 12.5px; font-weight: bold; fill: #1e40af; text-anchor: middle; dominant-baseline: middle; cursor: pointer; }
    
    .btn-sub { fill: #ffffff; stroke: #7c3aed; stroke-width: 2; rx: 8; cursor: pointer; }
    .btn-sub:hover { fill: #f5f3ff; stroke: #6d28d9; }
    .btn-sub-text { font-family: Arial, sans-serif; font-size: 13px; font-weight: bold; fill: #5b21b6; text-anchor: middle; dominant-baseline: middle; cursor: pointer; }
    
    .nav-btn { fill: #0f172a; rx: 6; cursor: pointer; }
    .nav-btn:hover { fill: #1e293b; }
    .nav-btn-text { font-family: Arial, sans-serif; font-size: 12px; font-weight: bold; fill: #ffffff; text-anchor: middle; dominant-baseline: middle; cursor: pointer; }
    
    .solid-line { stroke: #64748b; stroke-width: 2; }
    .dashed-line { stroke: #64748b; stroke-width: 1.5; stroke-dasharray: 4,4; marker-end: url(#arrow-master); }
    .rel-text { font-family: Arial, sans-serif; font-size: 11px; fill: #475569; text-anchor: middle; dominant-baseline: middle; }
  </style>

  <script type="text/javascript">
    <![CDATA[
    function showPhase(phaseId) {
      var groups = document.querySelectorAll('.phase-group');
      for (var i = 0; i < groups.length; i++) {
        groups[i].style.display = 'none';
      }
      var target = document.getElementById(phaseId);
      if (target) {
        target.style.display = 'inline';
      }
    }
    ]]>
  </script>

  <rect width="100%" height="100%" class="bg" />
''')

# ==============================================================================
# FASE 1: PROCESOS PRINCIPALES
# ==============================================================================
svg.append('  <!-- FASE 1: PROCESOS PRINCIPALES -->')
svg.append('  <g id="phase1" class="phase-group" style="display: inline;">')

svg.append('    <rect x="170" y="50" width="840" height="680" class="boundary" filter="url(#card-shadow)" />')
svg.append('    <text x="590" y="85" class="title-main">FASE 1: PROCESOS DEL PROYECTO (FICHA TÉCNICA)</text>')
svg.append('    <text x="590" y="105" class="subtitle-main">(Haz clic en cualquiera de los procesos para ver sus subprocesos asociadas)</text>')

actor_x = 80
actor_y = 390
svg.append(f'    <circle cx="{actor_x}" cy="{actor_y - 35}" r="18" class="actor" />')
svg.append(f'    <line x1="{actor_x}" y1="{actor_y - 17}" x2="{actor_x}" y2="{actor_y + 25}" class="actor" />')
svg.append(f'    <line x1="{actor_x - 25}" y1="{actor_y - 5}" x2="{actor_x + 25}" y2="{actor_y - 5}" class="actor" />')
svg.append(f'    <line x1="{actor_x}" y1="{actor_y + 25}" x2="{actor_x - 20}" y2="{actor_y + 60}" class="actor" />')
svg.append(f'    <line x1="{actor_x}" y1="{actor_y + 25}" x2="{actor_x + 20}" y2="{actor_y + 60}" class="actor" />')
svg.append(f'    <text x="{actor_x}" y="{actor_y + 85}" class="actor-text">Admin</text>')

m_keys = list(macro_processes.keys())
m_start_y = 135
m_step_y = 68

for idx, m_key in enumerate(m_keys):
    m_data = macro_processes[m_key]
    my = m_start_y + (idx * m_step_y)
    
    svg.append(f'    <line x1="{actor_x + 35}" y1="{actor_y}" x2="230" y2="{my + 20}" class="solid-line" />')
    svg.append(f'''    <g onclick="showPhase('phase2_{m_key}')">
      <rect x="230" y="{my}" width="440" height="42" class="btn-proc" filter="url(#card-shadow)" />
      <text x="450" y="{my + 21}" class="btn-proc-text">{m_data["title"]}</text>
    </g>''')

svg.append('  </g>')

# ==============================================================================
# FASE 2: SUBPROCESOS POR PROCESO
# ==============================================================================
svg.append('  <!-- FASE 2: SUBPROCESOS POR PROCESO -->')

for m_key, m_data in macro_processes.items():
    svg.append(f'  <g id="phase2_{m_key}" class="phase-group" style="display: none;">')
    
    svg.append('    <rect x="170" y="80" width="840" height="650" class="boundary" filter="url(#card-shadow)" />')
    svg.append(f'    <text x="590" y="115" class="title-main">FASE 2: SUBPROCESOS DE {m_data["title"].upper()}</text>')
    svg.append('    <text x="590" y="135" class="subtitle-main">(Haz clic en un subproceso para abrir su diagrama de Casos de Uso completo)</text>')
    
    svg.append('''    <g onclick="showPhase('phase1')">
      <rect x="25" y="25" width="160" height="36" class="nav-btn" />
      <text x="105" y="43" class="nav-btn-text">&#8592; Volver a Procesos</text>
    </g>''')
    
    svg.append(f'    <circle cx="{actor_x}" cy="{actor_y - 35}" r="18" class="actor" />')
    svg.append(f'    <line x1="{actor_x}" y1="{actor_y - 17}" x2="{actor_x}" y2="{actor_y + 25}" class="actor" />')
    svg.append(f'    <line x1="{actor_x - 25}" y1="{actor_y - 5}" x2="{actor_x + 25}" y2="{actor_y - 5}" class="actor" />')
    svg.append(f'    <line x1="{actor_x}" y1="{actor_y + 25}" x2="{actor_x - 20}" y2="{actor_y + 60}" class="actor" />')
    svg.append(f'    <line x1="{actor_x}" y1="{actor_y + 25}" x2="{actor_x + 20}" y2="{actor_y + 60}" class="actor" />')
    svg.append(f'    <text x="{actor_x}" y="{actor_y + 85}" class="actor-text">Admin</text>')
    
    subs = m_data["subs"]
    s_count = len(subs)
    s_start_y = 180
    s_step_y = 75 if s_count <= 4 else (450 / s_count)
    
    for s_idx, sub_name in enumerate(subs):
        sy = s_start_y + (s_idx * s_step_y)
        clean_sub = sub_name.replace('"', '')
        safe_sub_key = re.sub(r'[^a-zA-Z0-9_]', '_', clean_sub)
        
        svg.append(f'    <line x1="{actor_x + 35}" y1="{actor_y}" x2="250" y2="{sy + 20}" class="solid-line" />')
        svg.append(f'''    <g onclick="showPhase('phase3_{safe_sub_key}')">
      <rect x="250" y="{sy}" width="340" height="42" class="btn-sub" filter="url(#card-shadow)" />
      <text x="420" y="{sy + 21}" class="btn-sub-text">{clean_sub}</text>
    </g>''')

    svg.append('  </g>')

# ==============================================================================
# FASE 3: DIAGRAMA DE CASOS DE USO ESPECÍFICO
# ==============================================================================
svg.append('  <!-- FASE 3: DIAGRAMA DE CASOS DE USO ESPECÍFICO -->')

for m_key, m_data in macro_processes.items():
    for sub_name in m_data["subs"]:
        clean_sub = sub_name.replace('"', '')
        safe_sub_key = re.sub(r'[^a-zA-Z0-9_]', '_', clean_sub)
        
        svg.append(f'  <g id="phase3_{safe_sub_key}" class="phase-group" style="display: none;">')
        
        svg.append(f'''    <g onclick="showPhase('phase2_{m_key}')">
      <rect x="25" y="15" width="200" height="34" class="nav-btn" />
      <text x="125" y="32" class="nav-btn-text">&#8592; Volver a Subprocesos</text>
    </g>''')
        
        svg.append('''    <g onclick="showPhase('phase1')">
      <rect x="240" y="15" width="160" height="34" class="nav-btn" />
      <text x="320" y="32" class="nav-btn-text">&#8962; Inicio (Procesos)</text>
    </g>''')
        
        if sub_name in phase3_svgs:
            svg.append('    <g transform="translate(10, 60)">')
            svg.append(phase3_svgs[sub_name])
            svg.append('    </g>')
            
        svg.append('  </g>')

svg.append('</svg>')

final_svg_content = "\n".join(svg)

with open(output_svg, "w", encoding="utf-8") as f:
    f.write(final_svg_content)

print(f"Dynamic height standalone 3-Phase Interactive SVG updated at {output_svg}")

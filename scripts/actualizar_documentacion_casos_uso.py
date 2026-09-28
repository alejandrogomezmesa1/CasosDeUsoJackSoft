import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
v3_dir = os.path.join(base_dir, "casos_de_uso_v3")
espec_dir = os.path.join(base_dir, "Especificaciones")
puml_dir = os.path.join(base_dir, "Diagramas_PUML")

from actualizar_casos_uso_canonicos import canonical_subprocesses

# Group canonical subprocesses by Macro
macro_groups = {
    "01_configuracion_y_seguridad.md": {
        "title": "Configuración y Seguridad",
        "desc": "Gestión de roles, permisos, usuarios y mecanismos de autenticación y acceso al sistema.",
        "subs": ["ROLES", "USUARIOS", "ACCESO"],
        "espec_file": "CU_01_Configuracion_y_Seguridad.md"
    },
    "02_compras_e_inventario.md": {
        "title": "Compras e Inventario",
        "desc": "Gestión del catálogo de insumos, categorías de materia prima, proveedores y órdenes de compra.",
        "subs": ["CATEGORIA DE INSUMOS", "INSUMOS", "PROVEEDORES", "COMPRAS"],
        "espec_file": "CU_02_Compras_e_Inventario.md"
    },
    "03_produccion_y_recetas.md": {
        "title": "Producción y Recetas",
        "desc": "Control de personal de cocina, categorías y catálogo de productos, fichas técnicas (recetas), órdenes de producción y producto terminado.",
        "subs": ["CATEGORIA PRODUCTOS", "PRODUCTOS", "EMPLEADOS", "PRODUCCION", "FICHA TECNICA \"PRODUCTO\"", "PRODUCTO TERMINADO"],
        "espec_file": "CU_03_Produccion_y_Recetas.md"
    },
    "04_servicios_y_operacion.md": {
        "title": "Servicios y Operación",
        "desc": "Administración de categorías y tipos de servicios (almuerzos, catering), y parametrización del calendario operativo.",
        "subs": ["CATEGORIA DE SERVICIOS", "SERVICIO", "CALENDARIO"],
        "espec_file": "CU_04_Servicios_y_Operacion.md"
    },
    "05_clientes_y_ventas.md": {
        "title": "Clientes y Ventas",
        "desc": "Gestión de clientes, cotización, registro y administración de suscripciones corporativas e individuales.",
        "subs": ["CLIENTES", "SUSCRIPCIONES"],
        "espec_file": "CU_05_Clientes_y_Ventas.md"
    },
    "06_logistica_y_domicilios.md": {
        "title": "Logística y Domicilios",
        "desc": "Asignación de zonas de reparto, gestión de domiciliarios, monitoreo en tiempo real de entregas y gestión de incidencias operativas.",
        "subs": ["RUTA Y DOMICILIARIOS", "MONITOREO DE ENTREGA \"TIEMPO REAL\"", "INCIDENCIAS"],
        "espec_file": "CU_06_Logistica_y_Domicilios.md"
    },
    "07_analitica_y_metricas.md": {
        "title": "Analítica y Métricas",
        "desc": "Consulta de indicadores clave de rendimiento (KPIs), visualización gráfica de métricas y generación de reportes de gestión.",
        "subs": ["DASHBOARD"],
        "espec_file": "CU_07_Analitica_y_Metricas.md"
    }
}

sub_dict = {sp["title"]: sp for sp in canonical_subprocesses}

for v3_file, mdata in macro_groups.items():
    # 1. Generate casos_de_uso_v3 file
    lines = []
    lines.append(f"# Macro-Proceso: {mdata['title']}\n")
    lines.append(f"{mdata['desc']}\n")
    lines.append("## Subprocesos Integrados\n")
    
    for sub_title in mdata["subs"]:
        sp = sub_dict[sub_title]
        puml_file = os.path.join(puml_dir, sp["safe_title"] + ".puml")
        puml_code = ""
        if os.path.exists(puml_file):
            with open(puml_file, "r", encoding="utf-8") as pf:
                puml_code = pf.read().strip()
                
        lines.append(f"### Subproceso: {sp['title']}")
        lines.append(f"- **Total de Casos de Uso / Acciones:** {len(sp['actions'])}")
        lines.append(f"- **Actor Principal:** {sp['actor']}")
        lines.append(f"- **Nodo Principal:** {sp['hub']}\n")
        lines.append("#### Listado de Casos de Uso")
        for idx, act in enumerate(sp["actions"], 1):
            lines.append(f"{idx}. {act}")
        lines.append("\n#### Diagrama PlantUML")
        lines.append("```plantuml")
        lines.append(puml_code)
        lines.append("```\n")
        lines.append("---\n")
        
    v3_path = os.path.join(v3_dir, v3_file)
    with open(v3_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Updated v3 doc: {v3_file}")

    # 2. Update Especificaciones file
    espec_file = mdata["espec_file"]
    espec_path = os.path.join(espec_dir, espec_file)
    
    # Read existing frontmatter if present
    frontmatter = ""
    if os.path.exists(espec_path):
        with open(espec_path, "r", encoding="utf-8") as ef:
            content = ef.read()
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    frontmatter = f"---{parts[1]}---\n\n"
                    
    esp_lines = []
    if frontmatter:
        esp_lines.append(frontmatter.strip())
        
    cu_code = v3_file.split("_")[0]
    esp_lines.append(f"# 📌 CU-{cu_code}: Módulo de {mdata['title']}\n")
    esp_lines.append("## 📌 Descripción General")
    esp_lines.append(f"{mdata['desc']}\n")
    esp_lines.append("---\n")
    esp_lines.append("## 📋 Subprocesos y Especificación Funcional\n")
    
    for idx_s, sub_title in enumerate(mdata["subs"], 1):
        sp = sub_dict[sub_title]
        safe_name = sp["safe_title"]
        png_rel = f"../Diagramas_PNG/{safe_name}.png"
        
        esp_lines.append(f"### Subproceso {idx_s}: {sp['title']} ({len(sp['actions'])} Casos de Uso)")
        esp_lines.append(f"* **Actor Principal:** `{sp['actor']}`")
        esp_lines.append(f"* **Nodo Principal:** `{sp['hub']}`\n")
        esp_lines.append(f"![Diagrama de Casos de Uso - {sp['title']}]({png_rel})\n")
        esp_lines.append("#### Casos de Uso Oficiales:")
        for idx, act in enumerate(sp["actions"], 1):
            esp_lines.append(f"{idx}. **{act}**")
        esp_lines.append("\n---\n")
        
    with open(espec_path, "w", encoding="utf-8") as f:
        f.write("\n".join(esp_lines))
    print(f"Updated Especificación: {espec_file}")

# Update master summary casos_de_uso_v3.md and README.md
total_cus = sum(len(sp["actions"]) for sp in canonical_subprocesses)
summary_lines = []
summary_lines.append(f"# Especificación General de Casos de Uso - JackSoft (Versión Canónica v3)")
summary_lines.append(f"\n**Total de Subprocesos:** {len(canonical_subprocesses)}  ")
summary_lines.append(f"**Total de Casos de Uso Oficiales:** {total_cus}  ")
summary_lines.append(f"**Diseño y Estandarización:** Sistema de Diseño Corporativo JackSoft (La Coca de Jacks)\n")
summary_lines.append("| Nº | Subproceso | Macro-Proceso | Actor Principal | Cantidad de Casos de Uso |")
summary_lines.append("| :--- | :--- | :--- | :--- | :---: |")

for idx, sp in enumerate(canonical_subprocesses, 1):
    summary_lines.append(f"| {idx} | **{sp['title']}** | {sp['macro']} | `{sp['actor']}` | {len(sp['actions'])} |")

summary_lines.append("\n---\n")

for sp in canonical_subprocesses:
    summary_lines.append(f"## Subproceso: {sp['title']}")
    summary_lines.append(f"* **Macro-Proceso:** {sp['macro']} ({sp['macro_full']})")
    summary_lines.append(f"* **Actor:** {sp['actor']}")
    summary_lines.append(f"* **Nodo Principal:** {sp['hub']}\n")
    summary_lines.append("### Casos de Uso:")
    for i, a in enumerate(sp["actions"], 1):
        summary_lines.append(f"{i}. {a}")
    summary_lines.append("\n---\n")

master_text = "\n".join(summary_lines)
with open(os.path.join(v3_dir, "casos_de_uso_v3.md"), "w", encoding="utf-8") as f:
    f.write(master_text)
with open(os.path.join(v3_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(master_text)

print("Master README and summary files updated successfully!")

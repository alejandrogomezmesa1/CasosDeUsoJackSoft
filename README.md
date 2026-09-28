# CasosDeUsoJackSoft

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Viewer-brightgreen?logo=github)](https://alejandrogomezmesa1.github.io/CasosDeUsoJackSoft/)
[![JackSoft](https://img.shields.io/badge/Sistema-JackSoft%20%7C%20La%20Coca%20de%20Jacks-2A170F)](https://alejandrogomezmesa1.github.io/CasosDeUsoJackSoft/)
[![Version](https://img.shields.io/badge/Versi%C3%B3n-Can%C3%B3nica%20v3.0-C05621)](https://alejandrogomezmesa1.github.io/CasosDeUsoJackSoft/)

Repositorio oficial y visor interactivo de la especificación funcional, arquitectura de software y diagramas de casos de uso del sistema **JackSoft** para la empresa **La Coca de Jacks**.

---

## 🌐 Visor Interactivo en Vivo (GitHub Pages)

Accede al visor interactivo desplegado en GitHub Pages con diseño corporativo sobrio (paleta café espresso y crema cálida), barra lateral plegable y soporte para fotos HD y render vectorial SVG:

👉 **[https://alejandrogomezmesa1.github.io/CasosDeUsoJackSoft/](https://alejandrogomezmesa1.github.io/CasosDeUsoJackSoft/)**

### Características del Visor:
- **Navbar Plegable / Desplegable**: Botón en cabecera y atajo de teclado (`M` o `P`) para maximizar el área de trabajo al 100%.
- **Renderizado Dual**: Visualización de fotos HD (`.png`) de alta fidelidad y modo vectorial escalable (`.svg`).
- **Zoom Dinámico**: Controles de acercar (+), alejar (-) y restablecer (100%).
- **Mapa General de Arquitectura**: Vista panorámica que integra los 7 macro-procesos y actores del ecosistema.
- **Acceso Directo HD**: Enlace para abrir o descargar cada diagrama en su resolución original.

---

## 🗂️ Estructura del Repositorio

```text
CasosDeUsoJackSoft/
├── index.html                  # Visor Web Interactivo principal (GitHub Pages ready)
├── README.md                   # Documentación general y catálogo del sistema
├── .gitignore                  # Exclusiones de archivos temporales del sistema
│
├── Diagramas_PNG/              # 22 diagramas canónicos HD + 1 Mapa General del Sistema
│   ├── ACCESO.png
│   ├── ROLES.png
│   ├── USUARIOS.png
│   ├── CLIENTES.png
│   ├── EMPLEADOS.png
│   ├── MAPA_GENERAL_CASOS_DE_USO.png
│   └── ... (23 archivos PNG)
│
├── Diagramas_SVG/              # Diagramas vectoriales escalables independientes
│   └── ... (22 archivos SVG)
│
├── Diagramas_PUML/             # Código fuente PlantUML con jerarquías y notas normativas
│   └── ... (22 archivos PUML)
│
├── Diagramas_DrawIO/           # Diagrama general editable en Draw.io
│   └── Casos_de_usos.drawio
│
├── Arquitectura_C4/            # Modelado de Arquitectura C4 del Sistema JackSoft
│   ├── Arquitectura_C4_JackSoft.md
│   ├── C4_Nivel1_Contexto.[png,puml,svg]
│   ├── C4_Nivel2_Contenedores.[png,puml,svg]
│   ├── C4_Nivel3_Componentes.[png,puml,svg]
│   └── C4_Nivel4_Codigo_Clases.[png,puml,svg]
│
├── casos_de_uso_v3/            # Especificaciones funcionales canónicas v3 en Markdown
│   ├── 01_configuracion_y_seguridad.md
│   ├── 02_compras_e_inventario.md
│   ├── 03_produccion_y_recetas.md
│   ├── 04_servicios_y_operacion.md
│   ├── 05_clientes_y_ventas.md
│   ├── 06_logistica_y_domicilios.md
│   ├── 07_analitica_y_metricas.md
│   ├── casos_de_uso_v3.md
│   └── README.md
│
├── Especificaciones/           # Documentación técnica formal y documentos Word (.docx)
│   ├── 00_MOC_Casos_de_Uso.md
│   ├── CU_01_Configuracion_y_Seguridad.md a CU_07_Analitica_y_Metricas.md
│   ├── Documentacion_Casos_de_Uso_JackSoft.docx
│   └── Documentacion_Casos_de_Uso_JackSoft_31ago.docx
│
├── Visor_Interactivo/          # Espejo y recursos estáticos del visor interactivo
│   ├── index.html
│   ├── mapa_interactivo.html
│   └── mapa_interactivo.svg
│
└── scripts/                    # Scripts Python de automatización y generación
    ├── generar_mapa_interactivo.py
    ├── actualizar_casos_uso_canonicos.py
    ├── actualizar_documentacion_casos_uso.py
    └── generar_svg_casos_uso.py
```

---

## 📊 Matriz Canónica de Macro-Procesos y Subprocesos

| Macro-Proceso | Subproceso Canónico | CUs / Acciones | Actor Principal | Diagrama HD |
| :--- | :--- | :---: | :--- | :---: |
| **1. Configuración y Seguridad** | `ROLES` | 7 | Administrador | [Ver PNG](./Diagramas_PNG/ROLES.png) |
| | `USUARIOS` | 7 | Administrador | [Ver PNG](./Diagramas_PNG/USUARIOS.png) |
| | `ACCESO` | 5 | Todos los Roles | [Ver PNG](./Diagramas_PNG/ACCESO.png) |
| **2. Compras e Inventario** | `CATEGORIA DE INSUMOS` | 6 | Administrador | [Ver PNG](./Diagramas_PNG/CATEGORIA_DE_INSUMOS.png) |
| | `INSUMOS` | 7 | Administrador | [Ver PNG](./Diagramas_PNG/INSUMOS.png) |
| | `PROVEEDORES` | 6 | Administrador | [Ver PNG](./Diagramas_PNG/PROVEEDORES.png) |
| | `COMPRAS` | 7 | Administrador | [Ver PNG](./Diagramas_PNG/COMPRAS.png) |
| **3. Producción y Recetas** | `EMPLEADOS` | 7 | Administrador | [Ver PNG](./Diagramas_PNG/EMPLEADOS.png) |
| | `CATEGORIA PRODUCTOS` | 7 | Administrador | [Ver PNG](./Diagramas_PNG/CATEGORIA_PRODUCTOS.png) |
| | `PRODUCTOS` | 6 | Administrador | [Ver PNG](./Diagramas_PNG/PRODUCTOS.png) |
| | `FICHA TECNICA "PRODUCTO"` | 7 | Administrador / Cocinero | [Ver PNG](./Diagramas_PNG/FICHA_TECNICA__PRODUCTO_.png) |
| | `PRODUCTO TERMINADO` | 6 | Cocinero | [Ver PNG](./Diagramas_PNG/PRODUCTO_TERMINADO.png) |
| | `PRODUCCION` | 7 | Administrador / Cocinero | [Ver PNG](./Diagramas_PNG/PRODUCCION.png) |
| **4. Servicios y Operación** | `CATEGORIA DE SERVICIOS` | 6 | Administrador | [Ver PNG](./Diagramas_PNG/CATEGORIA_DE_SERVICIOS.png) |
| | `SERVICIO` | 6 | Administrador | [Ver PNG](./Diagramas_PNG/SERVICIO.png) |
| | `CALENDARIO` | 5 | Administrador | [Ver PNG](./Diagramas_PNG/CALENDARIO.png) |
| **5. Clientes y Ventas** | `CLIENTES` | 7 | Administrador | [Ver PNG](./Diagramas_PNG/CLIENTES.png) |
| | `SUSCRIPCIONES` | 9 | Administrador / Cliente | [Ver PNG](./Diagramas_PNG/SUSCRIPCIONES.png) |
| **6. Logística y Domicilios** | `RUTA Y DOMICILIARIOS` | 6 | Domiciliario | [Ver PNG](./Diagramas_PNG/RUTA_Y_DOMICILIARIOS.png) |
| | `MONITOREO DE ENTREGA "TIEMPO REAL"` | 7 | Administrador / Cliente | [Ver PNG](./Diagramas_PNG/MONITOREO_DE_ENTREGA__TIEMPO_REAL_.png) |
| | `INCIDENCIAS` | 6 | Domiciliario / Administrador | [Ver PNG](./Diagramas_PNG/INCIDENCIAS.png) |
| **7. Analítica y Métricas** | `DASHBOARD` | 5 | Administrador | [Ver PNG](./Diagramas_PNG/DASHBOARD.png) |
| **Ecosistema Completo** | `MAPA_GENERAL` | Global | Todos los Actores | [Ver PNG](./Diagramas_PNG/MAPA_GENERAL_CASOS_DE_USO.png) |

---

## 🚀 Despliegue en GitHub Pages

Para publicar el visor web interactivo en GitHub Pages:

1. Ve a los **Settings** del repositorio en GitHub (`https://github.com/alejandrogomezmesa1/CasosDeUsoJackSoft/settings/pages`).
2. En la sección **Build and deployment**:
   - **Source**: `Deploy from a branch`
   - **Branch**: `main`
   - **Folder**: `/ (root)`
3. Guarda los cambios. En 1-2 minutos el sitio estará disponible públicamente en:
   **`https://alejandrogomezmesa1.github.io/CasosDeUsoJackSoft/`**

---

## 💻 Ejecución Local

Si deseas correr el visor localmente en tu equipo:

```bash
# Navegar a la carpeta del proyecto
cd 05_Casos_de_Uso

# Iniciar servidor web ligero
python3 -m http.server 8080

# Abrir en el navegador:
# http://localhost:8080/index.html
```

---

## 🛠️ Tecnologías y Estándares
- **UML 2.5 / PlantUML**: Estandarización de actores, casos de uso, paquetes y relaciones (`<<include>>`, `<<extend>>`).
- **Arquitectura C4**: Modelos en 4 niveles (Contexto, Contenedores, Componentes y Clases).
- **HTML5 / CSS3 Moderno / Vanilla JS**: Interfaz responsiva sin dependencias externas pesadas.
- **Identidad Corporativa**: Paleta basada en café espresso (`#2A170F`), crema cálida (`#FAF6F0`), terracota (`#C05621`) y acentos de diseño editorial.

---

Desarrollado para el sistema **JackSoft** — *La Coca de Jacks*.

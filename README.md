# Análisis Portal de Ortodoncia — Clustering de clientes

Repositorio de trabajo para segmentar pacientes (activos primero) usando Python.
Incluye notebooks paso a paso y estructura lista para portafolio (GitHub + Notion).

## Estructura
```
analisis-portal-ortodoncia/
├─ data/
│  ├─ raw/            # CSV originales (no subir a Git)
│  ├─ interim/        # datos parcialmente procesados
│  └─ external/       # otras fuentes
├─ notebooks/
│  ├─ 01_exploracion_tab_clientes.ipynb
│  ├─ 02_preparacion_features_activos.ipynb
│  ├─ 03_modelado_clustering_activos.ipynb
│  └─ 04_perfilado_clusters_y_insights.ipynb
├─ src/
│  └─ utils.py
├─ reports/
│  └─ figures/
├─ requirements.txt
└─ README.md
```

## Datos
- Coloca `Tab_Clientes(2).csv` en `data/raw/`.
- **No subas datos sensibles** al repo público. Sube solo notebooks, código y gráficos.

## Reproducibilidad
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Licencia
Uso interno para portafolio educativo.
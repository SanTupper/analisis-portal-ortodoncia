# Análisis Portal Ortodoncia

Proyecto de portafolio para segmentación de pacientes de clínicas dentales usando **clustering**.  
El enfoque prioriza **reproducibilidad**, **interpretabilidad** y **privacidad** (no se suben datos reales al repositorio).

---

## 🎯 Objetivos
- Preparar y estandarizar datos (fechas, KPIs de presupuestos, ventanas de atención, geografía).  
- Entrenar y evaluar un **clustering interpretable** de pacientes **activos** (≤ 2 años sin visita).  
- Generar **insights accionables** (ej. abandono latente, alta frecuencia, pacientes fantasma).  

---

## 🗂️ Estructura del repo

```text
analisis-portal-ortodoncia/
├─ notebooks/
│  ├─ 01_exploracion_tab_clientes.ipynb
│  ├─ 02_preparacion_features_activos.ipynb
│  ├─ 03_modelado_clustering_activos.ipynb
│  ├─ 04_perfilado_clusters_y_insights.ipynb
│  ├─ 05_validacion_vs_pbi.ipynb
│  └─ 06_prestaciones_validacion.ipynb
├─ src/
│  └─ utils.py
├─ data/                # ignorado en git (.gitignore)
│  ├─ raw/              # datos crudos (no públicos)
│  ├─ interim/          # artefactos intermedios
│  ├─ processed/        # datasets listos para modelar
│  └─ external/         # fuentes externas
├─ reports/
│  └─ figures/
├─ requirements.txt
├─ .gitignore
└─ README.md

📒 Notebooks y flujo

01_exploracion_tab_clientes — Exploración inicial, fechas (histórico vs planificación), validación de DiasDesdeUltimaVisita (offset +11 días), geografía preliminar.

02_preparacion_features_activos — KPIs de presupuestos (log1p, salvaguardas), presencias 15d/1m/3m/6m, geografía (Comuna_grp/Región) y Empresa/Convenio → activos ≤ 730 días.

03_modelado_clustering_activos — Estandarización (pipeline mixto), barrido K=2..10, selección de K=3, entrenamiento final y perfiles de clusters.

04_perfilado_clusters_y_insights — Perfiles extendidos e insights de negocio (en progreso).

05_validacion_vs_pbi — Cruces/consistencia vs métricas del dashboard interno.

06_prestaciones_validacion — Validación por cohortes con Prestaciones (ppto vs pago mismo año) + QA de reglas.

🚀 Cómo ejecutar

Python 3.11 (recomendado).

Crear entorno e instalar dependencias:

python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
pip install -r requirements.txt


Datos locales (no públicos)
Colocar en data/raw/:

Tab_Clientes(2).csv

ETL_vPrestaciones (2).csv
(Opcional: usa .env con DATA_PATH para cambiar rutas).

Orden sugerido de ejecución

NB-01 → NB-02 → (opcional: NB-06, NB-05) → NB-03 → NB-04

📦 Salidas locales clave (regeneradas al correr notebooks)

NB-02:

data/processed/activos_for_model_v2.csv — matriz baseline sin Empresa.

data/processed/activos_for_model_v2_empresa.csv — matriz con Empresa/Convenio.

data/processed/activos_ids_v2_plus.csv — IDs (RutBeneficiario, RutTitular, #beneficiarios).

NB-03:

data/processed/activos_ids_v2_plus_clustered.csv — IDs + etiquetas de cluster.

data/processed/cluster_profiles_baseline.csv — perfiles de clusters (medianas, baseline).

data/processed/cluster_profiles_con_empresa.csv — perfiles (con Empresa).

data/processed/clusters_centroids_baseline.csv — centroides (baseline, técnico).

data/processed/clusters_centroids_con_empresa.csv — centroides (con Empresa, técnico).

⚠️ data/ está en .gitignore: este repositorio no incluye datos reales.

🧩 Decisiones principales (resumen)

Fechas: histórico en ISO; planificación en DD/MM/AAAA. Flags de planificación incluidos.

DiasDesdeUltimaVisita: se usa el valor del sistema (offset +11 días frente a recálculo).

Presupuestos: montos con log1p; KPIs con salvaguardas; NaN → 0 solo para el modelo.

Atención: presencias en ventanas 15d, 1m, 3m, 6m.

Geografía: Comuna_grp (Top-N + Otras/Infreq + Sin Comuna) y Region (one-hot).

Escalado: pipeline mixto (Standard para Edad, Robust para montos/conteos, passthrough para %Cumplimiento).

Clustering: K=3 elegido por equilibrio entre codo (SSE) y silhouette.

Comparativa A/B: incluir Empresa/Convenio no cambió resultados → baseline suficiente.

Insights clave:

Cluster 0: abandono latente.

Cluster 1: jóvenes activos, alta conversión.

Cluster 2: inactivos/fantasma.


📚 Documentación
Overview y bitácora (Notion):
https://www.notion.so/An-lisis-Portal-Ortodoncia-Portafolio-2431f20d0fc080eaa4e6ff90e3126a8a?source=copy_link
(el detalle de cada notebook se documenta en su página hija con callout de estado).

📄 Licencia
Este proyecto usa la licencia MIT. Revisa el archivo LICENSE en la raíz.
© Autor: SanTupper (commits atribuidos mediante users.noreply.github.com).
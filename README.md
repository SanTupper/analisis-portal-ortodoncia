# Análisis Portal Ortodoncia

Proyecto de portafolio para segmentación de pacientes de clínicas dentales usando **clustering**.  
El enfoque prioriza **reproducibilidad**, **interpretabilidad** y **privacidad** (no se suben datos reales al repositorio).

---

## 🎯 Objetivos
- Preparar y estandarizar datos (fechas, KPIs de presupuestos, ventanas de atención, geografía).  
- Entrenar y evaluar un **clustering interpretable** de pacientes **activos** (≤ 2 años sin visita).  
- Generar **insights accionables** (ej. abandono latente, alta frecuencia, pacientes fantasma).  

---
🗂️ Estructura del repo
```
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
```

📒 Notebooks y flujo

01_exploracion_tab_clientes — Exploración inicial, fechas (histórico vs planificación), validación de DiasDesdeUltimaVisita (offset +11 días), geografía preliminar.

02_preparacion_features_activos — KPIs de presupuestos (log1p, salvaguardas), presencias 15d/1m/3m/6m, geografía (Comuna_grp/Región) y Empresa/Convenio → activos ≤ 730 días.

03_modelado_clustering_activos — Estandarización (pipeline mixto), barrido K=2..10, selección de K=3, entrenamiento final y perfiles de clusters.

04_perfilado_clusters_y_insights — Perfiles extendidos e insights de negocio (completado). Incluye comparativa global vs PBI exportada como nb04_dashboard_vs_clustering.csv.

05_validacion_vs_pbi — Validación de consistencia vs métricas del dashboard interno (PBI). Ejecutado antes en la cronología real; la tabla comparativa se exportó en NB-04.

06_prestaciones_validacion — Validación por cohortes con Prestaciones (ppto vs pago mismo año) + QA de reglas. Ejecutado antes en la cronología real; export creado nb06_prestaciones_validacion.csv.

🚀 Cómo ejecutar

Recomendado Python 3.11.

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
Nota: NB-05 y NB-06 se ejecutaron antes en la práctica; aquí se mantiene la numeración lógica.

📦 Salidas locales clave (se regeneran al correr notebooks)

NB-02

data/processed/activos_for_model_v2.csv — matriz baseline sin Empresa.

data/processed/activos_for_model_v2_empresa.csv — matriz con Empresa/Convenio.

data/processed/activos_ids_v2_plus.csv — IDs (RutBeneficiario, RutTitular, #beneficiarios).

NB-03

data/processed/activos_ids_v2_plus_clustered.csv — IDs + etiquetas de cluster.

data/processed/cluster_profiles_baseline.csv — perfiles (medianas, baseline).

data/processed/cluster_profiles_con_empresa.csv — perfiles (con Empresa).

data/processed/clusters_centroids_baseline.csv — centroides (baseline, técnico).

data/processed/clusters_centroids_con_empresa.csv — centroides (con Empresa, técnico).

NB-04

reports/nb04_perfil_general_baseline.csv

reports/nb04_perfil_ejecutivo_baseline.csv

reports/nb04_dist_region_baseline.csv

reports/nb04_dist_comuna_baseline.csv

reports/nb04_empresa_binarios_baseline.csv

reports/nb04_top_empresas_cluster*.csv

reports/nb04_dashboard_vs_clustering.csv (comparativa global vs PBI)

reports/nb04_insights_executive.md / .html / .pdf

NB-05

(La validación se realizó en esta fase, pero la tabla comparativa se exportó en NB-04 como nb04_dashboard_vs_clustering.csv.)

NB-06

reports/nb06_prestaciones_validacion.csv — cohortes 2025 y QA de reglas (ppto/pago/ambos; tasa ~91%).

⚠️ Privacidad: data/ está en .gitignore. Este repositorio no incluye datos reales.
ℹ️ La carpeta reports/ sí se versiona (reportes ejecutivos sin PII).

🧩 Decisiones principales (resumen)

Fechas: histórico en ISO; planificación en DD/MM/AAAA. Flags de planificación incluidos.

DiasDesdeUltimaVisita: se usa el valor del sistema (offset +11 días frente a recálculo).

Presupuestos: montos con log1p; KPIs con salvaguardas; NaN → 0 solo para el modelo.

Atención: presencias en 15d, 1m, 3m, 6m.

Geografía: Comuna_grp (Top-N + Otras/Infreq + Sin Comuna) y Region (one-hot).

Escalado: pipeline mixto (Standard para Edad, Robust para montos/conteos, passthrough para %Cumplimiento, presencias y dummies).

Clustering: K=3 elegido por equilibrio entre codo (SSE) y silhouette + interpretabilidad.

Comparativa A/B: incluir Empresa/Convenio no cambió resultados → baseline suficiente.

Validación PBI (NB-05): promedios consistentes; diferencias por corte temporal.

Prestaciones (NB-06): tasa de conversión 2025 ~91%, QA de reglas (DIAGNOSTICADA/INICIADA) consistente.

Insights clave

Cluster 0: abandono latente (reactivación).

Cluster 1: jóvenes activos, alta conversión (fidelización premium).

Cluster 2: inactivos/fantasma (depuración).

📚 Documentación

Overview y bitácora (Notion):
https://www.notion.so/An-lisis-Portal-Ortodoncia-Portafolio-2431f20d0fc080eaa4e6ff90e3126a8a?source=copy_link

(el detalle de cada notebook se documenta en su página hija con callout de estado).

Nota de cronología: NB-05 y NB-06 se ejecutaron antes de NB-03/04. La numeración en el repo se mantiene por claridad del flujo.

📄 Licencia

Este proyecto usa la licencia MIT. Revisa el archivo LICENSE en la raíz.
© Autor: SanTupper (commits atribuidos mediante users.noreply.github.com).
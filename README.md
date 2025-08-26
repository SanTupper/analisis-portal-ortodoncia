# Análisis Portal Ortodoncia

Proyecto de portafolio para segmentación de pacientes de clínicas dentales usando **clustering**.  
El enfoque prioriza **reproducibilidad**, **interpretabilidad** y **privacidad** (no se suben datos reales al repositorio).

## 🎯 Objetivos
- Preparar y estandarizar datos (fechas, KPIs de presupuestos, ventanas de atención, geografía).
- Entrenar y evaluar un **clustering interpretable** de pacientes **activos** (≤ 2 años sin visita).
- Generar **insights accionables** (p. ej., inactivos de alto potencial, frecuentes con baja conversión).

## 🗂️ Estructura del repo
analisis-portal-ortodoncia/
├─ notebooks/
│ ├─ 01_exploracion_tab_clientes.ipynb
│ ├─ 02_preparacion_features_activos.ipynb
│ ├─ 03_modelado_clustering_activos.ipynb
│ ├─ 04_perfilado_clusters_y_insights.ipynb
│ ├─ 05_validacion_vs_pbi.ipynb
│ └─ 06_prestaciones_validacion.ipynb
├─ src/
│ └─ utils.py
├─ data/ # ignorado en git (.gitignore)
│ ├─ raw/ # datos crudos (no públicos)
│ ├─ interim/ # artefactos intermedios
│ ├─ processed/ # datasets listos para modelar
│ └─ external/ # fuentes externas
├─ reports/figures/ # gráficas exportadas (si aplica)
├─ requirements.txt
├─ .gitignore
└─ README.md

## 📒 Notebooks y flujo
1) **01_exploracion_tab_clientes** — Exploración inicial, fechas (histórico vs planificación), validación de `DiasDesdeUltimaVisita` (offset +11 días), geografía preliminar.  
2) **02_preparacion_features_activos** — KPIs de presupuestos (log1p, salvaguardas), presencias 15d/1m/3m/6m, geografía (Comuna\_grp/Región) y Empresa/Convenio → **activos ≤ 730 días**.  
3) **03_modelado_clustering_activos** — Baseline de clustering (estandarización, k por codo/silhouette). *(en progreso)*  
4) **04_perfilado_clusters_y_insights** — Perfiles e insights por clúster. *(pendiente)*  
5) **05_validacion_vs_pbi** — Cruces/consistencia vs métricas del dashboard interno.  
6) **06_prestaciones_validacion** — Validación por **cohortes** con Prestaciones (ppto vs pago mismo año) + QA de reglas.

## 🚀 Cómo ejecutar
1. **Python 3.11** (recomendado)  
2. Crear entorno e instalar dependencias:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   pip install -r requirements.txt
Datos locales (no públicos)
Coloca en data/raw/:

Tab_Clientes(2).csv

ETL_vPrestaciones (2).csv
(Opcional: usa .env con DATA_PATH para cambiar rutas).

Orden sugerido de ejecución

NB-01 → NB-02 → (opcional: NB-06, NB-05) → NB-03 → NB-04

Salidas locales clave (se regeneran al correr notebooks)

data/processed/activos_for_model_v2.csv — matriz X para clustering

data/processed/activos_ids_v2_plus.csv — IDs para re-enganchar labels (RutBeneficiario, RutTitular, #beneficiarios)

Privacidad: data/ está en .gitignore. Este repositorio no incluye datos reales.

🧩 Decisiones principales (resumen)
Fechas: histórico en ISO; planificación en DD/MM/AAAA. Parseo a datetime con flags de planificación.

DiasDesdeUltimaVisita: se usa el valor del sistema (offset documental +11 días frente a recálculo).

Presupuestos: montos con log1p; KPIs con salvaguardas; NaN → 0 sólo para el modelo.

Atención: uso de presencia (0/1) en ventanas 15d, 1m, 3m, 6m.

Geografía: Comuna_grp (Top-N + “Otras/Infreq” + “Sin Comuna”) y Region con one-hot.

Empresa/Convenio: flags y dummies Top-N; análisis con y sin para comparar impacto en clustering.

📚 Documentación
Overview y bitácora (Notion): enlace privado del proyecto
(el detalle de cada notebook se documenta en su página hija con callout de estado).

📄 Licencia
Este proyecto usa la licencia MIT. Revisa el archivo LICENSE en la raíz.
© Autor: SanTupper (commits atribuidos mediante users.noreply.github.com).
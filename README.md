# Análisis Portal Ortodoncia

Proyecto de portafolio para segmentación de pacientes de clínicas dentales usando **clustering**.  
El enfoque prioriza **reproducibilidad**, **interpretabilidad** y **privacidad** (no se suben datos reales al repositorio).

## 🎯 Objetivos
- Preparar y estandarizar datos (fechas, KPIs de presupuestos, ventanas de atención, geografía).
- Entrenar y evaluar un **clustering interpretable** de pacientes **activos** (≤ 2 años sin visita).
- Generar **insights accionables** (p. ej., inactivos de alto potencial, frecuentes con baja conversión).

## 🗂️ Estructura del repo
```
analisis-portal-ortodoncia/
├─ notebooks/
│ ├─ 01_exploracion_tab_clientes.ipynb
│ ├─ 02_preparacion_features_activos.ipynb
│ ├─ 03_modelado_clustering_activos.ipynb
│ └─ 04_perfilado_clusters_y_insights.ipynb
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
```

## 🚀 Cómo ejecutar
1. **Python 3.11** (recomendado).
2. Crear entorno e instalar dependencias:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   pip install -r requirements.txt
Abrir los notebooks en notebooks/ en este orden:

01_exploracion_tab_clientes.ipynb

02_preparacion_features_activos.ipynb

03_modelado_clustering_activos.ipynb

04_perfilado_clusters_y_insights.ipynb

Nota de privacidad: data/ está en .gitignore. No se incluyen datos reales en el repo.
Para reproducir, coloca tus archivos en data/raw/ y ajusta rutas si fuese necesario.

🧩 Decisiones principales (resumen)
Fechas: histórico en ISO; planificación en DD/MM/AAAA. Columnas parseadas a datetime con flags de planificación.

DiasDesdeUltimaVisita: se usa el valor del sistema (offset documental +11 días vs cálculo directo).

Presupuestos: montos con log1p; KPIs con salvaguardas; NaN→0 para el modelo.

Atención: uso de presencia (0/1) en ventanas 15d, 1m, 3m, 6m, 1a, 2a.

Geografía: Comuna_grp (Top-20 + “Otras/Infreq” + “Sin Comuna”) y Region con one-hot.

🔗 Documentación ampliada
Notion: https://www.notion.so/An-lisis-Portal-Ortodoncia-Portafolio-2431f20d0fc080eaa4e6ff90e3126a8a?source=copy_link

📄 Licencia
Sin licencia específica por ahora. Puedes usarlo como referencia educativa.
© Autor: SanTupper (commits atribuidos mediante users.noreply.github.com).
# Playbook Global · Análisis Portal Ortodoncia

**Última actualización:** 09-sep-2025  
**Autor:** Santiago Tupper  
**Objetivo del documento:** explicar, de punta a punta, el proceso de análisis y segmentación de pacientes del Portal de Ortodoncia, en un lenguaje claro para negocio y con el suficiente detalle técnico para equipos de datos.

---

## 0) Cómo leer este documento
- **Capítulos 1–3**: contexto y datos (ideal para managers y reclutadores no técnicos).
- **Capítulos 4–6**: modelado, perfilado y validación (para analistas/DS).
- **Capítulo 7**: aplicaciones de negocio (para directores comerciales/marketing).
- **Capítulo 8**: visualizaciones (roadmap).
- **Capítulos 9–10**: lecciones y siguientes pasos (para todos).

---

## 1) Introducción

### 1.1 Contexto del proyecto
Portal Ortodoncia gestiona una base amplia de pacientes con diferentes niveles de actividad y recurrencia. El **problema de negocio**: identificar **segmentos accionables** para **reactivación** (quienes no han vuelto) y **conversión** (quienes tienen potencial de compra/seguimiento), optimizando comunicación y promociones.

### 1.2 Objetivos
- **Segmentar** pacientes activos y relacionados en grupos con comportamientos distinguibles.
- **Priorizar** oportunidades de reactivación y cross-selling.
- **Entregar** una guía reproducible (este playbook) + artefactos técnicos (notebooks/código).

### 1.3 Mapa de notebooks (NB)
- **NB-01**: EDA inicial y criterios de calidad de datos.  
- **NB-02**: Preparación y limpieza; dataset modelable.  
- **NB-03**: Modelado de clustering (KMeans; K=2..10; métricas elbow/silhouette).  
- **NB-04**: Perfilado de clusters e insights.  
- **NB-05**: Validación con archivo .pbix (consistencia vs. métricas de negocio).  
- **NB-06**: Validación con Prestaciones y checks adicionales.

> Nota: La **guía de mejora `.md`** ya está en _entregables_ del repo; **Data Quality** está documentado en Notion y se subirá al repo más adelante.

---

## 2) Data Journey

### 2.1 Fuentes de datos (principales)
- `Tab_Clientes(2).csv`: atributos de pacientes (edad, actividad, convenios/empresa, etc.).
- `activos_for_model_v2.csv` + variantes (`_empresa`, `_ids`): conjunto preparado para modelado (features depuradas; flags y dummies).
- Tablas auxiliares del ecosistema (p. ej., Prestaciones, Clínicas) para validación cruzada.

### 2.2 Criterios de preparación y limpieza
- **Filtrado de activos**: pacientes con >0 en alguna métrica de **presupuesto (ppto)** y/o **presencia** en ventanas de atención (15d, 1m, 3m, 6m).  
- **Tratamiento de nulos**: imputación conservadora o exclusión según criticidad de la variable.  
- **Variables categóricas**:  
  - `TieneEmpresa`, `EsConvenio` como **flags binarios**.  
  - Dummies Top-N por **Empresa** (`Empresa_grp_*`) para contrastar **con y sin** efecto empresa.  
- **Reducción de dimensionalidad (si aplica)**: eliminación de colinealidad/redundancias según evaluación en NB-02.

### 2.3 Dataset final de modelado (vista)
- Numéricas clave (ejemplos):  
  - **Actividad**: `CantPptos`, `CantPptosAbo`, `CantPptosAvan`, `TotPptos_l1p`, `TicketPromPpto_l1p`.  
  - **Recencia/presencia**: `Atencion15d_pres`, `Atencion1m_pres`, `Atencion3m_pres`, `Atencion6m_pres`.  
  - **Desempeño**: `PctCumplimiento`.  
  - **Demografía**: `Edad`.  
- Categóricas transformadas: `TieneEmpresa`, `EsConvenio`, dummies `Empresa_grp_*`.  
- **Versión con y sin dummies de Empresa** para comparar impacto en clustering.

---

## 3) EDA (Exploratory Data Analysis)

### 3.1 Preguntas guía
- ¿Cómo se distribuye la **recencia** de atención (15d/1m/3m/6m)?
- ¿Qué tan concentrado está el **ticket promedio**?
- ¿Cuál es el peso real de **Empresa/Convenio** en el comportamiento?

### 3.2 Hallazgos iniciales (resumen)
- Distribuciones **asimétricas** en montos y tickets → sugieren **RobustScaler** como opción sólida.
- Diferencias claras entre pacientes con **Empresa/Convenio** vs. individuos: mayor frecuencia de contacto y montos en algunos subgrupos.
- Recencia (1–3 meses) correlaciona con mayor probabilidad de actividad reciente.

### 3.3 Decisiones a partir del EDA
- Preparar dos pipelines:  
  **A)** _Baseline_ sin dummies de Empresa; **B)** con dummies Top-N para medir variación en la segmentación.  
- Probar **StandardScaler vs RobustScaler** y seleccionar por estabilidad de clusters e interpretabilidad.

---

## 4) Modelado (Clustering)

### 4.1 Selección de features
- Núcleo: **Actividad + Recencia + Ticket**.  
- Variantes: **+ Empresa/Convenio** (flags/dummies) para sensibilidad.  
- Exclusión de variables que inducen **data leakage** o duplicidad.

### 4.2 Escalado
- **Comparativa**:  
  - `StandardScaler` para magnitudes “normales”.  
  - `RobustScaler` para outliers.  
- **Criterio**: retener el que dé **mejor cohesión** (baja SSE), **separación** (silhouette) y **estabilidad** (consistencia al re-fit).

### 4.3 Selección de K
- Rango evaluado: **K = 2..10**.  
- **Métodos**:  
  - **Elbow (SSE)** para saturación marginal.  
  - **Silhouette** para separación entre clusters.  
- **Regla práctica**: elegir el **K mínimo** que logre buena separación **y** que siga siendo interpretable para negocio.

### 4.4 Entrenamiento
- Algoritmo: **K-Means** (seed fija para reproducibilidad).  
- Entrenamientos por **escenario**:  
  - **Escenario A**: sin Empresa.  
  - **Escenario B**: con dummies de Empresa.  
- Guardamos: escalador, modelo, métricas, asignaciones y centroides.

---

## 5) Perfilado de Clusters

### 5.1 Metodología
- Para cada cluster:  
  - Medianas/medias por variable clave.  
  - % con atención 1m/3m/6m.  
  - Distribución de ticket.  
  - Presencia de Empresa/Convenio (si aplica).  
- **Naming**: etiquetas **cortas y memorables** (ej. “Recurrentes-Alto Ticket”, “Dormidos-Bajo Ticket”, “Nuevos-Promesa”).

### 5.2 Ejemplos de insights (genéricos; ajustar con cifras del NB-04)
- **Cluster 0 – Recurrentes-Alto Ticket**: alta presencia en 1m/3m, ticket elevado; candidatos a **programas de fidelización premium**.  
- **Cluster 1 – Dormidos-Bajo Ticket**: baja recencia, montos pequeños; foco en **reactivación con incentivos**.  
- **Cluster 2 – Ocasionales-Medio Ticket**: actividad intermitente; activar **recordatorios** y **packs**.  

### 5.3 Efecto Empresa/Convenio
- Comparar el **mix de clusters** entre escenarios 0 y 1 para cuantificar cuánto “explica” pertenecer a Empresa versus comportamiento idiosincrático del paciente.

---

## 6) Validación

### 6.1 Con archivo .pbix (NB-05)
- **Chequeos**:  
  - Totales y conteos (ej. total de pacientes ≈ 9.103 en .pbix vs. dataset de modelado).  
  - Consistencia de segmentos por clínica/periodo.  
- **Resultado esperado**: diferencias menores y explicables por filtros/fechas.

### 6.2 Con Prestaciones (NB-06)
- **Cruces** con tipos de prestaciones y frecuencia:  
  - ¿Cada cluster consume cierto **mix** de prestaciones?  
  - ¿Existen prestaciones “gatillo” de reactivación?  
- **Objetivo**: validar que los clusters reflejen **comportamientos clínicos reales** y no artefactos de modelado.

### 6.3 Limitaciones
- Posible **sesgo temporal** si los periodos comparados no alinean.  
- Calidad de registro en campos categóricos (Empresa/Convenio) heterogénea.  
- El número de clusters es una aproximación; existe **no unicidad** de soluciones.

---

## 7) Aplicaciones de Negocio

### 7.1 Reactivación
- **Dormidos-Bajo Ticket**: campañas con **descuento inicial** + **recordatorios multicanal** (WhatsApp/SMS/email) + fácil scheduling.  
- **Ocasionales**: **packs** con ahorro por frecuencia; mensajes de “continuidad de tratamiento”.

### 7.2 Fidelización / Up-sell
- **Recurrentes-Alto Ticket**: **membresías** con beneficios, recordatorios preventivos, chequeos estéticos complementarios.

### 7.3 Operación
- **Priorizar llamadas** según cluster y probabilidad de retorno.  
- Ajustar **KPIs** por segmento (tasa de reactivación 30d/60d, ticket medio por cluster, costo de contacto por retorno).

---

## 8) Visualizaciones (pendiente / en desarrollo)

### 8.1 Roadmap de dashboards
- **Power BI**: perfilado por cluster, desglose por clínica y ventana temporal; validación vs PBI oficial.  
- **Tableau Public**: storytelling para portafolio (segmentos, recencia, ticket, mapa de clínicas).  
- **GitHub Pages** (opcional): visualizaciones en HTML (Plotly/Altair) para acceso abierto.

> Cuando el primer dashboard esté listo, se añadirá aquí el **enlace público** y capturas.

---

## 9) Lecciones Aprendidas

### 9.1 Técnicas
- **RobustScaler** suele estabilizar mejor con outliers en montos/tickets.  
- Trabajar **con y sin dummies de Empresa** ayuda a separar **efecto contractual** de **comportamiento real**.  
- Mantener **seed fija** y registrar **versiones de datos** mejora reproducibilidad.

### 9.2 De proceso
- Documentar criterios de **“quién es activo”** evitó confusiones posteriores.  
- Notion para storytelling + GitHub para código es una **combinación ganadora** para audiencias mixtas.

---

## 10) Próximos Pasos

1) **Publicar** el primer dashboard (PBI o Tableau) con visualizaciones del perfilado.  
2) **Experimentos**:  
   - Modelos de **propensión a retorno** (logística, árboles).  
   - **Uplift modeling** para campañas.  
3) **Automatización**:  
   - Pipeline reproducible (ETL → features → clustering → reporte).  
   - Programar **actualizaciones mensuales**.  
4) **Data Quality**: subir al repo la sección detallada de DQ hoy en Notion.

---

### Apéndice A · Convenciones y repositorio
- **Estructura sugerida**  
```
/data
/raw
/interim
/processed
/notebooks
/src
/docs
playbook_global.md
````
- **Versionado**: ramas por NB o feature; PRs con checklist (datos, métricas, reproducibilidad).
- **Privacidad**: anonimizar IDs si el repositorio es público.

---

**Créditos & contacto**  
- Proyecto liderado por **Santiago Tupper**.  
- Feedback y colaboraciones: abrir un **Issue** en el repo o contactar por LinkedIn/Email.

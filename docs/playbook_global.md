# Playbook Global · Análisis Portal Ortodoncia

---

![Data and Cluster Analysis Tairred to mpead of wpicigglthis Presentatior Intrication for Dental Clinic.png](attachment:6bb35dab-b6e3-4a73-b6e4-79ce75b1b1db:Data_and_Cluster_Analysis_Tairred_to_mpead_of_wpicigglthis_Presentatior_Intrication_for_Dental_Clinic.png)

---

## 1) Introducción

Portal Ortodoncia reúne una amplia base de pacientes con distintos niveles de actividad. El desafío que nos planteamos fue simple pero potente: **¿cómo podemos identificar grupos de pacientes para reactivarlos y acompañarlos mejor en sus tratamientos?**

En otras palabras, queríamos pasar de mirar a los pacientes como un “todo” a entenderlos como **segmentos con comportamientos y necesidades distintas**.

👉 Este playbook es el recorrido de ese análisis: desde los datos en bruto hasta los insights de negocio.

---

## 2) El viaje de los datos

Trabajamos con varias fuentes internas, siendo la principal el **archivo de clientes**. Allí teníamos información como: edad, montos de presupuestos, recencia de visitas, convenios con empresas, etc.

Para construir un dataset sólido, aplicamos filtros básicos:

- Solo pacientes con **alguna actividad registrada** en presupuestos o atenciones recientes.
- Variables limpias, sin duplicados ni ruido excesivo.
- Transformación de categorías (por ejemplo, si un paciente pertenecía a una empresa, lo convertimos en un indicador).

El resultado fue un conjunto de datos listo para analizar, equilibrado entre lo clínico y lo comercial.

![Captura de pantalla 2025-09-12 a la(s) 15.46.18.png](attachment:aa50aae4-2a03-4090-956a-287651b44e3e:Captura_de_pantalla_2025-09-12_a_la(s)_15.46.18.png)

---

## 3) Explorando los datos (EDA)

Antes de modelar, exploramos para entender la “personalidad” de los pacientes.

Algunas observaciones clave:

- La **edad** está distribuida de manera bastante amplia, con grupos jóvenes y adultos mayores.
- El **ticket promedio** varía mucho: algunos pacientes concentran montos altos, pero la mayoría tiene valores modestos.
- La **recencia de atención** (visitas en 15 días, 1 mes, 3 meses) muestra que muchos pacientes tienen largos periodos sin regresar.

👉 Esta exploración fue la base para decidir cómo escalar los datos y qué variables usar en los grupos.

![eda_hist_edad.png](attachment:81009cb8-f8eb-4e53-a4d1-4bdd75102531:eda_hist_edad.png)

*Refleja la concentración de pacientes en rangos etarios medios, clave para segmentar la comunicación.*

![eda_box_ticket.png](attachment:bbd45645-3524-44ea-9555-241d31754848:eda_box_ticket.png)

*Muestra la dispersión del gasto por paciente, con valores extremos que elevan el promedio.*

![eda_barras_recencia.png](attachment:0f0ba9df-635b-4b48-a63e-b205523471cf:eda_barras_recencia.png)

*Evidencia cuántos pacientes llevan meses sin visitar la clínica, mostrando oportunidades de reactivación.*

---

## 4) Construyendo los grupos (Clustering)

El corazón del análisis fue aplicar un algoritmo de clustering. La idea: **dejar que los datos nos digan qué grupos existen** sin imponer categorías previas.

Para decidir cuántos grupos usar, probamos distintas opciones y analizamos cuál daba la mejor separación y coherencia. Finalmente, elegimos un número de clusters que equilibraba simplicidad con riqueza de insights.

![modelo_codo_silhouette.png](attachment:8fcad00b-ed8d-4574-a60e-018fdb76f32b:modelo_codo_silhouette.png)

*Permite determinar la cantidad óptima de clusters, combinando criterio geométrico y calidad de segmentación.*

---

## 5) Conociendo a nuestros clusters

Aquí es donde el proyecto cobra vida: traducimos números en **perfiles de pacientes**.

Ejemplos de lo que encontramos:

- **Recurrentes – Alto Ticket**: pacientes que vienen seguido y generan montos altos. Ideales para programas de fidelización premium.
- **Dormidos – Bajo Ticket**: llevan tiempo sin venir, con montos bajos. Claros candidatos a campañas de reactivación con incentivos.
- **Ocasionales – Ticket Medio**: pacientes intermitentes, que necesitan recordatorios y paquetes que fomenten continuidad.

Cada cluster tiene su propia historia y nos permite diseñar estrategias personalizadas.

![Captura de pantalla 2025-09-14 a la(s) 16.23.47.png](attachment:6ef640ba-cf82-414a-a4d7-c316c95d76e1:Captura_de_pantalla_2025-09-14_a_la(s)_16.23.47.png)

*Resume las principales variables promedio de cada cluster, funcionando como perfil ejecutivo.*

![perfilado_clusters_barras.png](attachment:ce7409c4-cc5e-432e-815f-ac02f710af1f:perfilado_clusters_barras.png)

*Destaca cómo difieren los clusters en variables clave, facilitando la interpretación práctica.*

![perfilado_clusters_radar.png](attachment:b33bee21-b1d2-4686-bcdf-d41c36e62396:perfilado_clusters_radar.png)

*Visualiza de forma comparativa las fortalezas y debilidades de cada cluster en múltiples dimensiones.*

---

## 6) Validando que los grupos tengan sentido

No queríamos que los clusters fueran solo un resultado matemático. Por eso, los validamos contra otras fuentes:

- **Power BI**: chequeamos que los totales y distribuciones coincidieran con los reportes oficiales de la clínica.
- **Prestaciones**: revisamos si ciertos clusters consumían tipos específicos de tratamientos.

El resultado fue consistente: los grupos reflejaban **patrones reales de comportamiento clínico**.

---

### 📊 Validación con Power BI

Para asegurar consistencia global:

- Total de pacientes: Dashboard (≈14.500) vs. Clustering (14.141).
- Diferencias mínimas explicadas por corte temporal (PBI incluye un mes posterior).
- % con atención en 6m, % cumplimiento y % RM ≈ idénticos en ambos.

**Evidencias visuales:**

![7d75d92c-d19f-4560-adaf-52b122b41977.JPG](attachment:e50272e6-9f76-4eb7-ae2e-4eab08950812:7d75d92c-d19f-4560-adaf-52b122b41977.jpg)

*Muestra los indicadores globales oficiales de la clínica para validar los resultados del clustering.*

![dashboard_vs_clustering.png](attachment:d001ff26-0b7b-4e03-b23b-7eb4f082564b:dashboard_vs_clustering.png)

*Confirma la consistencia entre métricas globales del clustering y el dashboard interno.*

![validacion_dashboard_vs_clustering.png](attachment:3a9380ec-a418-4edd-afbc-7e84b0986a1f:validacion_dashboard_vs_clustering.png)

*Contrasta visualmente los promedios del clustering con los del dashboard para validar diferencias menores.*

---

### 🦷 Validación con Prestaciones

Analizamos el cruce entre clusters y tipos de prestaciones:

- Cada cluster consume combinaciones distintas de tratamientos.
- Ejemplo: Cluster 1 concentra prestaciones de seguimiento, Cluster 2 explica mayor dispersión fuera de RM.
- Esto confirma que los clusters reflejan **patrones clínicos reales**, no solo artefactos del modelado.

**Evidencias visuales:**

![Captura de pantalla 2025-09-14 a la(s) 15.51.14.png](attachment:34bc34a6-a27e-4810-9396-319198e13da9:Captura_de_pantalla_2025-09-14_a_la(s)_15.51.14.png)

![nb06_cluster_conversion_abs_fixed.png](attachment:c33da84f-f5a7-4d10-92e2-561ba2622bdc:nb06_cluster_conversion_abs_fixed.png)

*Comparación de pacientes con presupuesto, pago y ambos en 2025, desglosados por cluster.*

![nb06_cluster_conversion_rate_fixed.png](attachment:bfae8499-1191-4e6a-a3e3-d5fa0742e391:nb06_cluster_conversion_rate_fixed.png)

*Tasa de conversión (pacientes con presupuesto que terminaron pagando) por cluster.*

![nb06_cluster_prestaciones_heatmap_fixed.png](attachment:804a0cd5-e81b-47b1-8538-5543e51e1677:nb06_cluster_prestaciones_heatmap_fixed.png)

*Distribución porcentual de las principales prestaciones dentro de cada cluster (heatmap).*

![nb06_cluster_prestaciones_stacked.png](attachment:6d99b891-0faa-4dd7-9364-a1d961dbca79:nb06_cluster_prestaciones_stacked.png)

*Mix de las 10 prestaciones más frecuentes, representado en porcentajes con barras apiladas por cluster.*

---

## 7) Aplicaciones prácticas para la clínica

Los insights no se quedan en teoría: abren la puerta a estrategias concretas.

- **Reactivar pacientes dormidos** con campañas simples por WhatsApp o SMS, ofreciendo descuentos de bienvenida.
- **Fidelizar a los recurrentes** con membresías o chequeos estéticos adicionales.
- **Optimizar la operación** priorizando llamadas y esfuerzos comerciales en segmentos de mayor retorno.
- **Revisar y depurar datos** para tener una base consistente.
    
    ![Segmentación de Pacientes W APLICACIONES PRÁCTICAS PARA LA CLÍNICA.png](attachment:24cb8d37-8006-4b54-a394-1e98f5d8035b:Segmentacion_de_Pacientes_W_APLICACIONES_PRACTICAS_PARA_LA_CLINICA.png)
    

---

## 8) Lecciones aprendidas

El proyecto dejó aprendizajes valiosos tanto técnicos como de gestión del proceso:

- **Metodología técnica**
    - Los outliers distorsionan resultados si no se controlan: usar **escaladores robustos** y validar siempre las transformaciones es esencial.
    - Separar escenarios **con y sin convenios empresariales** permite distinguir comportamientos y evita conclusiones sesgadas.
    - La validación cruzada con fuentes externas (como Power BI) refuerza la confianza en los resultados y muestra el valor agregado del clustering.
- **Estructura y organización**
    - Aprendí a **organizar un proyecto de análisis en carpetas estándar** (`data/raw`, `data/processed`, `notebooks`, `reports`, etc.), lo que hace más fácil mantener orden y trazabilidad.
    - Entendí la importancia de usar `.gitignore` para que los archivos sensibles o demasiado pesados no se suban al repositorio.
    - GitHub funciona como repositorio **técnico**, mientras que Notion cumple el rol narrativo y visual: juntos hacen posible comunicar tanto a reclutadores como a directivos no técnicos.
- **Proceso de trabajo**
    - No basta con obtener métricas: hay que **traducir resultados en storytelling**, con imágenes, captions y callouts que transmitan el valor a quienes no son técnicos.
    - El **worklog diario** resultó ser una herramienta muy útil para documentar avances, decisiones y pendientes de forma continua.
    - El aprendizaje no fue solo de Python o modelos, sino de cómo **documentar y versionar un proyecto de punta a punta**, con disciplina y claridad.

---

<aside>
⚙

> “No basta con analizar; hay que contar la historia de manera que otros la entiendan”.
> 
</aside>

---

### 9) Conclusiones

El proyecto no solo permitió segmentar pacientes y descubrir patrones clínicos relevantes, sino también sentar las bases de un **proceso de análisis reproducible y documentado**.

- Los clusters obtenidos mostraron perfiles diferenciados con **implicancias prácticas directas** en comunicación, fidelización y gestión comercial.
- La validación contra fuentes oficiales aseguró que los resultados fueran consistentes y confiables.
- La combinación de **herramientas técnicas (Python, GitHub)** con **herramientas narrativas (Notion, infografías, storytelling)** demostró que los análisis pueden traducirse en propuestas claras y accionables.

En síntesis: este trabajo dejó no solo un resultado analítico, sino también una metodología replicable para futuros proyectos de la clínica o de otros contextos.
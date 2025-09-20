# Postmortem — Análisis Portal Ortodoncia

## 🎯 Propósito del postmortem
Dejar registro del proceso, las decisiones, dificultades y aprendizajes que marcaron el proyecto. El objetivo no es solo evaluar resultados, sino también capturar cómo llegamos a ellos y qué nos llevamos para futuros análisis.

---

## ✅ Lo que hicimos bien
- Persistencia ante dificultades técnicas: superar semanas de intentos para abrir un archivo `.bak` en entornos distintos (Parallels, UTM, Docker, Windows App, Azure VM).
- Aprendizaje aplicado: logramos instalar y usar SQL Server en una VM para restaurar la base, extraer datos y continuar el proyecto.
- Uso de Power BI: aunque no quedó en el entregable final, sirvió para rescatar bases completas y validar métricas frente a los dashboards internos.
- Metodología clara: estructuramos el repositorio en carpetas estándar (`data/`, `notebooks/`, `reports/`, `docs/`) y aplicamos buenas prácticas (uso de `.gitignore`, commits descriptivos, releases).
- Documentación dual: combinamos GitHub para lo técnico (código, issues, releases) y Notion para lo narrativo (storytelling, imágenes, subpáginas).
- Evolución en el uso de herramientas: aprendimos a trabajar con terminal, a usar IA como asesor permanente, y a mantener un **human in the loop** para no automatizar sin criterio.
- Presentación al cliente: desarrollamos un **playbook global** en `.md` y su versión visual en Notion/PDF, con imágenes y narrativa ejecutiva.
- Entrega estructurada: consolidamos outputs en `/reports/entregables/` para cliente, y documentación en `/docs/` para portafolio.

---

## ⚠️ Lo que se podría mejorar
- Planeación inicial: faltó definir desde el principio qué entregables serían para cliente y cuáles solo para portafolio (evitar duplicaciones como “playbook vs portafolio” o “guía de mejora vs data quality”).
- Gestión del tiempo: las trabas técnicas con SQL y entornos de ejecución alargaron mucho el inicio; se podría acotar con un checklist de entornos antes de arrancar.
- Curva de aprendizaje dispersa: aprender clustering, SQL, Power BI y GitHub al mismo tiempo generó cierta sobrecarga; para futuros proyectos, escalonar aprendizajes.
- Automatización limitada: el pipeline no quedó 100% automatizado (ejecución mensual simulada); se podría haber invertido en scripts reproducibles desde el inicio.
- Visualizaciones: aunque logramos visuales claras en matplotlib y Canva, se dejó de lado la capa de BI (Power BI/Tableau), lo que resta interactividad al entregable.
- Uso de tags en Git: se aplicó un release tag tardíamente; habría sido más útil usar tags parciales a lo largo del proyecto para marcar hitos intermedios.

---

## 📚 Aprendizajes clave

### Técnicos
- Manejar distintos entornos de SQL y VM es en sí un aprendizaje valioso para cualquier rol de analista.
- El clustering no es solo aplicar K-Means: requiere limpieza, escalado adecuado y validación contra fuentes externas.
- Aprendimos a generar entregables en distintos formatos: `.csv`, `.md`, `.pdf`, `.png`.
- La importancia de capturar *sanity checks* y *mini-tests* para no perder trazabilidad en cada notebook.

### De proceso
- Documentar en paralelo (Notion + GitHub) asegura trazabilidad y facilita mostrar resultados a públicos diferentes.
- El **worklog diario** fue una herramienta clave para ordenar el avance y las decisiones.
- Crear un **release tag** ayudó a marcar un hito de cierre parcial (v1.0-entregables), incluso sin ser definitivo.
- La narrativa (captions, callouts, infografías) es tan importante como el código: convierte resultados técnicos en propuestas accionables.

### Personales / estratégicos
- Aprender a usar IA como mentor técnico y acompañante de proceso, siempre con validación manual.
- Reafirmar la importancia del **human in the loop**: la IA acelera, pero la interpretación y decisión es humana.
- Descubrimos cómo presentar resultados a clientes de forma clara y ejecutiva, diferenciando lo técnico de lo narrativo.
- La perseverancia y capacidad de resolución de problemas técnicos se convierten en un activo narrativo (LinkedIn, entrevistas, portafolio).

---

## 🚀 Próximos pasos (para futuros proyectos)
- Definir desde el inicio **entregables concretos** (cliente vs portafolio).
- Implementar un **pipeline reproducible** con scripts de ejecución secuencial.
- Incluir un **CHANGELOG** para registrar cambios de cada etapa.
- Preparar entregables de BI interactivos (Tableau/Power BI) si el cliente lo requiere.
- Seguir consolidando GitHub + Notion como estándar de documentación y storytelling.

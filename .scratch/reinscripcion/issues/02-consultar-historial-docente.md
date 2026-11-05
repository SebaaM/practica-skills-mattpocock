# 02: Consultar el historial de una inscripción como docente

**What to build:** El docente puede consultar la secuencia de cancelaciones y reinscripciones de una inscripción desde la vista de la actividad, incluso cuando está vigente.

**Blocked by:** 01 (reinscribirse desde el detalle de la actividad)

**Spec:** ../spec.md

**Status:** done

- [x] La vista del docente muestra las cancelaciones y reinscripciones en orden cronológico con sus fechas.
- [x] El historial incluye una cancelación anterior al cambio y todos los cambios de un segundo ciclo.
- [x] La vista mantiene el estado actual y la ocupación correcta de la actividad.
- [x] Las pruebas HTTP verifican la consulta como docente y el control de acceso.

## Comments

Implementado en 1156c67 y ajustado en edbd41a. Suite integrada: 70 pruebas OK y esquema sin cambios pendientes.

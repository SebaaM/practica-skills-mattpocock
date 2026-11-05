# Reinscripción a una actividad

**Status:** ready-for-agent

## Problem Statement

Si un alumno cancela su inscripción y luego quiere asistir a la misma actividad, el sistema le impide volver a inscribirse incluso cuando todavía hay cupo. El detalle de la actividad le muestra la cancelación y bloquea el formulario.

## Solution

Permitir que el alumno vuelva a inscribirse en la misma actividad después de cancelar. El recorrido propuesto comienza en el detalle de la actividad y aplica las condiciones de una primera inscripción. Si el alumno recupera un cupo, su inscripción vuelve a estar vigente y el docente puede seguir consultando el historial.

## User Stories

1. Como alumno, quiero ver la acción de reinscripción en el detalle de una actividad elegible que cancelé, para saber que puedo volver a participar.
2. Como alumno, quiero reinscribirme con mi propia cuenta, para recuperar un cupo cuando decido asistir.
3. Como alumno, quiero ver la inscripción vigente tras reinscribirme, para saber que tengo cupo.
4. Como alumno, quiero ver el estado vigente en «Mis inscripciones», para identificar las actividades a las que voy a asistir.
5. Como alumno, quiero saber si se agotó el cupo desde que cancelé, para entender por qué mi reinscripción fue rechazada.
6. Como alumno, quiero poder volver a intentar cuando se libere un cupo, para asistir si la actividad sigue abierta.
7. Como alumno, quiero que el detalle refleje si la actividad está deshabilitada, para saber por qué no puedo reinscribirme.
8. Como alumno, quiero que el sistema me informe si la actividad ya empezó, para entender por qué no puedo reinscribirme.
9. Como alumno, quiero que un envío repetido mantenga una sola inscripción vigente, para evitar ocupar más de un cupo.
10. Como alumno, quiero que un intento rechazado conserve mi cancelación, para que el estado refleje lo que ocurrió.
11. Como alumno, quiero poder cancelar después de reinscribirme si la ventana sigue abierta, para liberar el cupo si vuelvo a cambiar de planes.
12. Como docente, quiero que una reinscripción exitosa vuelva a contar en la ocupación, para conocer los cupos disponibles.
13. Como docente, quiero poder consultar cuándo se canceló y cuándo se reactivó la inscripción, para entender los cambios de estado.
14. Como docente, quiero poder consultar el historial tras varios ciclos de cancelación y reinscripción, para conservar la secuencia completa.

## Implementation Decisions

La habilitación de la reinscripción es el objetivo del pedido. Los criterios de esta sección son los propuestos durante la conversación y quedan como supuestos de la especificación.

- El alumno autenticado solicita la reinscripción de su propia inscripción desde el detalle de la actividad. El servidor aplica las condiciones aunque el alumno envíe el formulario desde una vista desactualizada.
- La inscripción cancelada puede volver a estar vigente si la actividad está habilitada, el instante actual es anterior al inicio y queda cupo. En el instante exacto de inicio se rechaza la solicitud. Una inscripción ya vigente sigue tratándose como duplicada.
- Se conserva una sola inscripción por alumno y actividad. El historial guarda los instantes de cancelación y reinscripción, incluida la fecha de las cancelaciones que ya existen.
- Una reinscripción exitosa ocupa un cupo. El cambio de estado, la comprobación de capacidad y el registro en el historial forman una operación atómica. Si otro alumno ocupa el último cupo primero, la inscripción original sigue cancelada.
- El detalle y «Mis inscripciones» reflejan el estado actual. El docente puede consultar el historial aunque la inscripción esté vigente. El diseño de la vista de historial queda a criterio de implementación.
- La cancelación posterior se rige por la ventana existente, que incluye el instante exacto de 24 horas antes del inicio.
- Al implementar, actualizar la documentación de dominio y registrar cómo esta decisión modifica el ADR de cancelación. Sigue vigente el requisito de conservar la decisión de cancelar.

## Testing Decisions

- Usar el flujo HTTP autenticado como punto principal de prueba. Ejercitar el detalle, el envío del formulario, «Mis inscripciones» y la consulta del docente. Comprobar estados, mensajes, ocupación e historial observables. Las pruebas HTTP existentes de inscripción y cancelación sirven de referencia.
- Cubrir una cancelación previa con cupo, sin cupo, con la actividad deshabilitada y en el instante exacto de inicio. Cubrir también el envío repetido, el acceso con otra cuenta, una cancelación anterior al cambio y un segundo ciclo de cancelación y reinscripción.
- Reutilizar las pruebas de contención existentes para simular dos solicitudes por el último cupo. Comprobar que solo una lo ocupa y que el intento rechazado conserva su estado e historial.
- El punto de prueba principal y la cobertura de concurrencia quedan propuestos para revisión.

## Out of Scope

- Reinscripción gestionada por el docente en nombre del alumno.
- Lista de espera, prioridad para quienes cancelaron y reserva anticipada de cupos.
- Cambios en la ventana de cancelación o en las condiciones generales de inscripción.

## Further Notes

El caso que motivó el cambio es el de un alumno que canceló y quiere volver a la misma actividad. La conversación dejó como propuestas el autoservicio desde el detalle, la validación de las condiciones habituales y la conservación del historial con una única inscripción. La etiqueta de triage corresponde al flujo de publicación solicitado.

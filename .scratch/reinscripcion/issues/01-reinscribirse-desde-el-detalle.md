# 01: Reinscribirse desde el detalle de la actividad

**What to build:** El alumno puede recuperar un cupo desde el detalle de la actividad y ver su inscripción vigente en «Mis inscripciones». Si la actividad ya no admite inscripciones, recibe el motivo y conserva su cancelación.

**Blocked by:** None (can start immediately)

**Spec:** ../spec.md

**Status:** ready-for-agent

- [ ] El alumno autenticado puede reinscribirse en una actividad habilitada, con cupo y cuyo inicio todavía no llegó.
- [ ] La misma inscripción vuelve a estar vigente y ocupa un cupo. El detalle y «Mis inscripciones» muestran ese estado.
- [ ] La habilitación, el inicio y el cupo se vuelven a comprobar al enviar el formulario. Cada rechazo explica el motivo y conserva el estado y el historial.
- [ ] Se conservan las fechas de las cancelaciones existentes y se registran los cambios de estado. Una reinscripción posterior se puede cancelar dentro de la ventana vigente.
- [ ] Los envíos repetidos y concurrentes respetan la unicidad y la capacidad. El cambio de estado y el historial se registran juntos.
- [ ] La documentación de dominio refleja la reinscripción y su relación con el ADR de cancelación.
- [ ] Las pruebas HTTP y de contención cubren el recorrido y sus límites.

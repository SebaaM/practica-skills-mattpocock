# Inscripciones UNTDF

Dominio de la demo docente: alumnos que reservan cupos en actividades y docentes que las habilitan.

## Language

**Actividad**:
Un encuentro ofrecido a la comunidad universitaria, con fecha de inicio, capacidad y estado de habilitación.
_Avoid_: Evento, curso, clase

**Inscripción**:
Vínculo entre un alumno y una actividad que reserva un cupo hasta el inicio de la actividad. Cada alumno tiene como máximo una inscripción por actividad, esté vigente o cancelada.
_Avoid_: Registro, reserva, alta

**Cancelación**:
Decisión del alumno de renunciar a su inscripción dentro de la ventana de cancelación. La inscripción deja de ocupar cupo, pero se conserva junto con el instante en que se decidió.
_Avoid_: Baja, anulación, borrado, desinscripción

**Reinscripción**:
Decisión del alumno de volver a participar en una actividad cuya inscripción canceló. La misma inscripción vuelve a estar vigente y ocupa un cupo si la actividad está habilitada, aún no empezó y tiene cupo disponible.
_Avoid_: Nueva inscripción, alta

**Historial de inscripción**:
Secuencia de cancelaciones y reinscripciones, con la fecha y hora de cada cambio.

**Ventana de cancelación**:
Período en el que el alumno puede cancelar: desde que se inscribe hasta 24 horas antes del inicio de la actividad.
_Avoid_: Plazo de baja, fecha límite

**Cupo disponible**:
Cantidad de lugares que una actividad todavía puede ofrecer: su capacidad menos las inscripciones vigentes.
_Avoid_: Vacante, lugar, disponibilidad (como sinónimo de cantidad)

**Alumno**:
Persona autenticada que se inscribe en actividades y puede cancelar o reactivar sus propias inscripciones.
_Avoid_: Estudiante, usuario

**Docente**:
Persona con acceso a la administración; habilita actividades y consulta inscripciones, pero no inscribe ni cancela por otros.
_Avoid_: Profesor, administrador

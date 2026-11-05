# Reinscripción con historial

El alumno puede volver a inscribirse después de cancelar. La reinscripción recupera un cupo con las mismas condiciones que una primera inscripción. Se mantiene una fila por alumno y actividad, como establece el [ADR 0001](0001-inscripciones-canceladas-se-conservan.md). `cancelled_at` indica el estado actual y vuelve a quedar vacío al reinscribirse. Un historial por inscripción registra cada cancelación y reinscripción con su instante. La migración incorpora al historial las fechas de las cancelaciones existentes.

## Alternativas consideradas

- **Guardar la última cancelación y la última reinscripción.** Agregar dos fechas a la inscripción simplificaría la consulta, pero perdería los cambios de ciclos anteriores.
- **Derivar el estado del último cambio.** Usar únicamente el historial evitaría almacenar el estado por separado, a costa de consultar el último cambio de cada inscripción al calcular la ocupación y mostrar el estado.

## Consecuencias

- La cancelación y la reinscripción guardan el estado actual y el historial en la misma transacción de escritura. La reinscripción comprueba la habilitación, el inicio y el cupo después de adquirir la reserva de escritura de SQLite.
- Una solicitud rechazada conserva el estado y el historial. La ventana de cancelación mantiene su límite inclusivo de 24 horas antes del inicio.

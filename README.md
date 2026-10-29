# TRAZA · Red ferroviaria española en tiempo real

Panel no oficial de la red ferroviaria: mapa con todos los trenes, cortes de vía, avisos, sucesos históricos, teléfonos y flota.

## Publicar en GitHub Pages
1. Sube el contenido de esta carpeta a un repositorio nuevo (por ejemplo `TRAZA`).
2. Settings → Pages → Deploy from a branch → `main` / raíz.
3. Settings → Actions → General → Workflow permissions → **Read and write**.
4. Pestaña Actions → «Copia de datos en vivo (Renfe)» → Run workflow (la primera vez a mano).

## De dónde salen los datos
- **Trenes en vivo**: la página intenta leer los datos abiertos de Renfe directamente cada 30 s. Si el navegador lo bloquea, usa las copias de `vivo/*.json` que actualiza la tarea programada cada 10 minutos. Si no hay ninguna, muestra una simulación sobre horarios tipo (avisado en pantalla).
- **Cortes, avisos, sucesos, teléfonos, flota**: en el bloque de datos de `index.html` (constantes `CORTES`, `OBRAS`, `SUCESOS`, `TELEFONOS`, `FLOTA`). Verificados el 29/10/2026; actualízalos a mano o con un robot como el de PRESOE.
- Iryo, Ouigo y los operadores autonómicos no publican posiciones abiertas: se muestran simulados.
- La ocupación de los trenes no es pública: se muestra una estimación y la capacidad de la serie.

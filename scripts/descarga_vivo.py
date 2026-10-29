"""Descarga los datos abiertos de Renfe en tiempo real y los guarda en vivo/.

Fuentes:
  flotaLD            posición y retraso de trenes de AV, Larga y Media Distancia
  vehicle_positions  posición de trenes de Cercanías (GTFS-RT en JSON)
  trip_updates       retrasos de Cercanías
  alerts             avisos de Cercanías
Si una fuente falla, se conserva la copia anterior.
"""
import json, pathlib, urllib.request

FUENTES = {
    "flotaLD": "https://tiempo-real.largorecorrido.renfe.com/renfe-visor/flotaLD.json",
    "vehicle_positions": "https://gtfsrt.renfe.com/vehicle_positions.json",
    "trip_updates": "https://gtfsrt.renfe.com/trip_updates.json",
    "alerts": "https://gtfsrt.renfe.com/alerts.json",
}
destino = pathlib.Path(__file__).resolve().parent.parent / "vivo"
destino.mkdir(exist_ok=True)

for nombre, url in FUENTES.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "traza-bot/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            datos = json.loads(r.read().decode("utf-8"))
        (destino / f"{nombre}.json").write_text(json.dumps(datos, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"ok   {nombre}")
    except Exception as e:  # una fuente caída no detiene las demás
        print(f"fallo {nombre}: {e}")

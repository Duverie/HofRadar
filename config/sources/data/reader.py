import json
import os


def lade_hoefe():
    datei = "data/properties.json"

    if not os.path.exists(datei):
        return []

    with open(datei, "r", encoding="utf-8") as f:
        return json.load(f)


def zeige_hoefe():
    hoefe = lade_hoefe()

    print("🏡 Gefundene Höfe:")
    print("------------------")

    for hof in hoefe:
        print(f"Name: {hof['name']}")
        print(f"Region: {hof['region']}")
        print(f"Preis: CHF {hof['preis']}")
        print(f"Grundstück: {hof['grundstueck_m2']} m²")
        print(f"Bewertung: {hof['bewertung']}/100")
        print("------------------")


if __name__ == "__main__":
    zeige_hoefe()

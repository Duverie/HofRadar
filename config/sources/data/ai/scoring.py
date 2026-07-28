from config.settings import MAX_PREIS, MIN_GRUNDSTUECK


def bewerte_hof(hof):
    punkte = 0

    # Preis
    if hof["preis"] <= MAX_PREIS:
        punkte += 25

    # Grundstück
    if hof["grundstueck_m2"] >= MIN_GRUNDSTUECK:
        punkte += 30

    # Pferdehaltung
    if hof.get("pferdehaltung"):
        punkte += 20

    # Einliegerwohnung
    if hof.get("einliegerwohnung"):
        punkte += 15

    # Bonus
    if hof["region"] in ["Elsass", "Schweiz", "Südbaden"]:
        punkte += 10

    return punkte


def bewertung_text(punkte):
    if punkte >= 90:
        return "⭐⭐⭐⭐⭐ Traumhof"
    elif punkte >= 70:
        return "⭐⭐⭐⭐ Sehr interessant"
    elif punkte >= 50:
        return "⭐⭐⭐ Prüfen"
    else:
        return "⭐ Eher ungeeignet"

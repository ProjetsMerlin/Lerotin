import datetime

def calculPhaseLunaire_m1(date=None):
    if date is None:
        date = datetime.datetime.now()

    # Nouvelle Lune de référence très précise : 2000-01-06 18:14 UTC | source : NASA / Espenak
    nouvelle_lune_ref = datetime.datetime(2000, 1, 6, 18, 14)

    cycle = 29.530588853

    jours_ecoules = (date - nouvelle_lune_ref).total_seconds() / 86400.0

    phase = (jours_ecoules % cycle) / cycle

    current_lunar = {}

    if phase < 0.03 or phase > 0.97:
        libelle = "Nouvelle Lune"
        icon = "🌑"
    elif 0.03 <= phase < 0.22:
        libelle = "Premier Croissant"
        icon = "🌒"
    elif 0.22 <= phase < 0.28:
        libelle = "Premier Quartier"
        icon = "🌓"
    elif 0.28 <= phase < 0.47:
        libelle = "Gibbeuse croissante"
        icon = "🌔"
    elif 0.47 <= phase < 0.53:
        libelle = "Pleine Lune"
        icon = "🌕"
    elif 0.53 <= phase < 0.72:
        libelle = "Gibbeuse décroissante"
        icon = "🌖"
    elif 0.72 <= phase < 0.78:
        libelle = "Dernier Quartier"
        icon = "🌗"
    else:
        libelle = "Dernier Croissant"
        icon = "🌘"

    current_lunar["phase"] = libelle
    current_lunar["icon"] = icon
    current_lunar["value"] = phase

    return current_lunar

def displayResult():
    date = datetime.datetime.now()
    aujourdhui = date.strftime("%Y/%m/%d")
    res = calculPhaseLunaire_m1(date)
    # return f"Phase lunaire du {aujourdhui} : {res['phase']} (valeur={res['value']:.3f})"
    return res
import datetime
import ephem

def calculPhaseLunaire_m2(date=None):
    if date is None:
        date = datetime.datetime.now()

    local = date.astimezone()
    date_utc = local.astimezone(datetime.timezone.utc)

    observer = ephem.Observer()
    observer.lon = '4.35'  
    observer.lat = '50.85'  
    observer.date = date_utc

    moon = ephem.Moon(observer)
    phase = moon.moon_phase  
    phase_norm = phase
    
    if phase_norm < 0.03 or phase_norm > 0.97:
        libelle = "Nouvelle Lune 🌑"
    elif phase_norm < 0.22:
        libelle = "Premier Croissant 🌒"
    elif phase_norm < 0.28:
        libelle = "Premier Quartier 🌓"
    elif phase_norm < 0.47:
        libelle = "Gibbeuse croissante 🌔"
    elif phase_norm < 0.53:
        libelle = "Pleine Lune 🌕"
    elif phase_norm < 0.72:
        libelle = "Gibbeuse décroissante 🌖"
    elif phase_norm < 0.78:
        libelle = "Dernier Quartier 🌗"
    else:
        libelle = "Dernier Croissant 🌘"

    return {
        "phase": libelle,
        "phase_value": phase_norm,
        "date_used": date_utc.strftime("%Y/%m/%d")
    }

def displayResult():
    res = calculPhaseLunaire_m2()
    date = datetime.datetime.now()
    aujourdhui = date.strftime("%Y/%m/%d")
    return f"Phase lunaire du {aujourdhui} : {res['phase']} (valeur={res['phase_value']:.3f})"

print(displayResult())

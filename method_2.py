import datetime
import ephem

def method_2(date=None):
    if date is None:
        date = datetime.datetime.now(datetime.timezone.utc)

    date_ephem = ephem.Date(date)
    prev_new_moon = ephem.previous_new_moon(date_ephem)
    age_days = float(date_ephem - prev_new_moon)

    if age_days < 1.84566:
        label, icon = "Nouvelle Lune", "🌑"
    elif age_days < 5.536:
        label, icon = "Premier Croissant", "🌒"
    elif age_days < 9.228:
        label, icon = "Premier Quartier", "🌓"
    elif age_days < 12.920:
        label, icon = "Gibbeuse croissante", "🌔"
    elif age_days < 16.611:
        label, icon = "Pleine Lune", "🌕"
    elif age_days < 20.302:
        label, icon = "Gibbeuse décroissante", "🌖"
    elif age_days < 23.993:
        label, icon = "Dernier Quartier", "🌗"
    elif age_days < 27.684:
        label, icon = "Dernier Croissant", "🌘"
    else:
        label, icon = "Nouvelle Lune", "🌑"

    return {
        "label": label,
        "icon": icon,
        "day": date.strftime("%d/%m/%Y"),
    }

print(method_2())
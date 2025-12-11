import datetime

def method_1(date=None):
    if date is None:
        date = datetime.datetime.utcnow()

    epoch = datetime.datetime(2000, 1, 6, 18, 14, 0)
    synodic_month = 29.530588853
    delta = date - epoch
    days = delta.total_seconds() / 86400.0
    age = days % synodic_month

    if age < 1.84566:
        label, icon = "Nouvelle Lune", "🌑"
    elif age < 5.536:
        label, icon = "Premier Croissant", "🌒"
    elif age < 9.228:
        label, icon = "Premier Quartier", "🌓"
    elif age < 12.920:
        label, icon = "Gibbeuse croissante", "🌔"
    elif age < 16.611:
        label, icon = "Pleine Lune", "🌕"
    elif age < 20.302:
        label, icon = "Gibbeuse décroissante", "🌖"
    elif age < 23.993:
        label, icon = "Dernier Quartier", "🌗"
    elif age < 27.684:
        label, icon = "Dernier Croissant", "🌘"
    else:
        label, icon = "Nouvelle Lune", "🌑"

    return {
        "label": label,
        "icon": icon,
        "day": date.strftime("%d/%m/%Y"),
    }

# print(method_1())
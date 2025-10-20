def formatDate(format, locale, datetime) :
    # Définir la locale pour obtenir les noms des jours et des mois en français
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    # Obtenir la date courante
    date_courante = datetime.now()
    # Formater la date selon le format souhaité
    date_formatee = date_courante.strftime(format)

    return date_formatee

def req (url, requests) :
    response = requests.request("GET", url)
    content = response.text
    return content
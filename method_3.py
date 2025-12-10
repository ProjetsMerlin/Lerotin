import requests
from bs4 import BeautifulSoup
from datetime import datetime
import locale

def date_format_lunopia(date):
    # locale FR
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

    weekday = date.strftime("%A").capitalize()
    day = date.strftime("%d")
    month = date.strftime("%B").lower()
    year = date.strftime("%Y")

    return f"{weekday} {day} {month} {year} :"


def get_current_lunar_data():
    from packages.functions import req

    current_lunar = {}

    now = datetime.now()
    current_date = date_format_lunopia(now).lower()

    content = req("https://www.lunopia.com/calendrier-lunaire", requests)
    soup = BeautifulSoup(content, "html.parser")

    rows = soup.find_all("tr")

    for row in rows:
        day_cell = row.find("td", class_="table_cal_jour")
        if not day_cell:
            continue

        span = day_cell.find("span", class_="date_long")
        if not span or not span.string:
            continue

        date_ligne = span.string.lower().strip()

        if date_ligne == current_date:

            phase_cell = row.find("td", class_="table_cal_phase")
            icon_cell = row.find("td", class_="table_cal_lune")

            current_lunar["day"] = span.string.strip()
            current_lunar["phase"] = phase_cell.string.strip() if phase_cell else ""
            current_lunar["icon"] = icon_cell.string.strip() if icon_cell else ""

    return current_lunar

def displayResult():
    date = datetime.datetime.now()
    res = get_current_lunar_data(date)
    aujourdhui = date.strftime("%Y/%m/%d")
    return f"Phase lunaire du {aujourdhui} : {res['phase']} (valeur={res['phase_value']:.3f})"
import requests
from bs4 import BeautifulSoup
from babel.dates import format_date
from datetime import datetime

def date_format_lunopia(date):
    return format_date(date, format="EEEE d MMMM yyyy", locale="fr_FR")

def method_3():
    from packages.functions import req

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

        now = datetime.now()
        date = date_format_lunopia(now).lower()
        date_ligne = span.string.lower().strip()

        if date_ligne == date:
            icon = row.find("td", class_="table_cal_lune")
            label = row.find("td", class_="table_cal_phase")

            return {
                "label": label.string.strip(),
                "icon": icon.string.strip(),
                "day": now.strftime("%d/%m/%Y"),
            }
        
print(method_3())
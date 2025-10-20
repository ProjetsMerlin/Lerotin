import locale
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

## Lerotin
from packages.functions import formatDate, req

current_lunar = dict()
current_date = formatDate("%A %d %B %Y", locale, datetime)
content = req("https://www.lunopia.com/calendrier-lunaire", requests)

data = BeautifulSoup(content, 'html.parser')
table = data.find_all("tr")
for data in table:
    days = data.find_all('td', class_='table_cal_jour')
    icons = data.find_all('td', class_='table_cal_lune')
    phases = data.find_all('td', class_='table_cal_phase')

    for day in days :
        day = day.find('span', class_="date_long").string

        if( day.lower() == current_date) :
            current_lunar["day"] = day.capitalize()
    
    for icon in icons :
        if( day.lower() == current_date) :
            current_lunar["icon"] = icon.string

    for phase in phases :
        if( day.lower() == current_date) :
            current_lunar["phase"] = phase.string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=current_lunar)

if __name__ == '__main__':
    app.run(debug=True)
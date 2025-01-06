#!/usr/bin/python3

import calendar
import datetime


theme = "Annonce la gloire du Seigneur"

"""dtb_jours = {}

y = 1
for m in range(1, 13):
    for day in calendar.Calendar().itermonthdays(2025, m):
        if day != 0:  # Ignore les jours vides
            mydate = datetime.date(2025, m, day).strftime("%Y-%m-%d")
            dtb_jours[f"jour{y}"] = [y, mydate, theme]
            y += 1

for cle, valeur in dtb_jours.items():
    print(cle, valeur)


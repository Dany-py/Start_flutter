#!/usr/bin/python3

import calendar
import datetime
import sys
sys.path.append('/usr/local/python/3.12.1/lib/python3.12/site-packages')

#print(sys.path)
import keyboard


theme = []

for i in range(0, 3):    
    thème = input('Entrer le thème : ')
    print()
    print('\nSuccessful entry\n')

"""
if keyboard.is_pressed('enter'):
        print(f"Thème saisi : {thème}")
        if keyboard.is_pressed('backspace'):
            thème = input('Corriger le thème')
    print(theme)


theme = "Annonce la gloire du Seigneur"
dtb_jours = {}

y = 1
for m in range(1, 13):
    for day in calendar.Calendar().itermonthdays(2025, m):
        if day != 0:  # Ignore les jours vides
            mydate = datetime.date(2025, m, day).strftime("%Y-%m-%d")
            dtb_jours[f"jour{y}"] = [y, mydate, theme]
            y += 1

for cle, valeur in dtb_jours.items():
    print(cle, valeur)

"""

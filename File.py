

#!/usr/bin/python3

import calendar, datetime

mdate = []
date = calendar.Calendar()

l = []

j= 0

for m in range(1, 13):
    for day in date.itermonthdays(2025, m):
        if day != 0:
            l.append(day)
    
    while j < len(l):
        mydate = datetime.date(2025, m, l[j])
        mdate.append(mydate)
        j = j+1

"""   
for y in range(0, len(mdate)):
    print(mdate[y])
"""

theme = "Anonnce la gloire du Seigneur"

dtb_jours = {}

for y in range(0, len(mdate)):
    the_liste = []
    the_liste.append(y)
    the_liste.append(mdate[y])
    the_liste.append(theme)
    dtb_jours["jour"+str(y)] =  the_liste
    
for cle, valeur in dtb_jours.items():
    print(cle,valeur)

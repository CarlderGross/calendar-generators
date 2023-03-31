import sys

#Initial variable settings
day = 1 #Starting day
year = 1 #Starting year
month = 11 #Starting month
week = ["  "] #Holds the week; used for keeping track of what weekday it is for month-end offset
monthnames = ["Fireseek", "Stirring", "Planting", "Marching", "Stormtide", "Highsun", "Swelter", "Fading", "Harvest", "Leaffall", "Patchwall", "Sunsebb"]
weekdays = ["St", "Su", "Mo", "Tr", "He", "Se", "Hi"]
# Starday, Sunday, Moonday, Treeday, Heavenday, Seaday, Highday

#Write output to file
sys.stdout = open("calendar.txt", "w")

#Print the first month
print(monthnames[month-1])
print(weekdays)

#Print calendar for years up to 2 (arbitrary number selected because I haven't decided what year it is in this game yet)
while year < 4:
    while month < 13:
        while day < 31: #all months are 30 days
            week.append(str(day) if day > 9 else " "+str(day))
            if len(week) == 7:
                print(week)
                week.clear()
            day+=1
        if (len(week) != 0):
            print(week)
        if len(week) < 7:
            offset = len(week)
        week.clear()
        for i in range (offset):
            week.append("  ")
        month += 1
        if month < 13:
            #Between-month holidays
            if month == 4:
                print("\nEostera")
            if month == 7:
                print("\nLitha")
            if month == 10:
                print ("\nMabon")
            #New month
            print("\n"+monthnames[month-1])
            print(weekdays)
        day = 1
    year += 1
    month = 1
    if year < 4: #The beginning of the year
        print("\nYule")
        print("\n"+monthnames[month-1])
        print(weekdays)

sys.stdout.close()
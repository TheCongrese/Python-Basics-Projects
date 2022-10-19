import datetime

# birthday Function
def birthday(**person):
    global dlg, lage
    sunday = []
    d = {}
    name = list(person.keys())
    anv = list(person.values())
    anv.reverse()
    name.reverse()
    for n in name:
        for i in anv:
            d.update({n: i})
    print(f"reversing inputs:\n{d}\n")
    cpt = 0
    anv.sort()
    lst = []
    for i in anv:
        for n in name:
            if person.get(n) == i:
                lst.append(n)
    for n in name:

        cpt += 1
        lage = []
        dlg = {}

        for a in anv:

            age = abs(int(datetime.datetime.today().year) - int(a.year))
            lage.append(age)
            lage.sort()
            day = a.strftime("%A")
            if person.get(n) == a:
                print(f"{n} is {age} years  old and she/he was born on {day}")
                if day == "Sunday":
                    sunday.append(n)
    for l in lage:
        for n in person.values():
            if abs(int(datetime.datetime.today().year) - int(n.year)) == l:
                for z in name:
                    if person.get(z) == n:
                        dlg.update({z: l})
    ls = list(dlg.keys())
    print(f"\n-Total People: {cpt}")
    print(f"-The oldest one is {ls[-1]}")
    print(f"-The youngest one is {ls[0]}")
    print("-The names of people from oldest to youngest: ", lst)
    print(f"-The names of people born on Sunday: {sunday}")


dic = {"amine": datetime.date(1999, 12, 15), "yacine": datetime.date(2001, 8, 12),
       "mohamed": datetime.date(1995, 7, 24),
       "fouad": datetime.date(1936, 10, 11), "samira": datetime.date(2007, 7, 2), "rahim": datetime.date(1976, 1, 31)
       }

birthday(**dic)

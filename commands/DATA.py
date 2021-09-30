import pickle
from openeentranslate import openen as op
from openlandcode import openen as landc

taal = landc
aanhalingsteken = '"'
data = []
dataalgemaakt = (str.upper(input(op(taal, "pakketinstallsuc"), 'J/N')))
if dataalgemaakt == 'N':
    data = []
    data.append(input(op(taal, "voornaam")))
    data.append(input(op(taal, "achternaam")))
    data.append(input(op(taal, "leeftijd")))
    data.append(input(op(taal, "woonplaats")))
    data.append(input(op(taal, "eten")))
    data.append(input(op(taal, "ietsanders")))
    print(op(taal, "voornaamis") ,data[0] ,'.')
    print(op(taal, "achternaamis") ,data[1] , '.')
    print(op(taal, "leeftijdis") ,data[2] , ".")
    print(op(taal, "datanogeenkeer"))
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)
else:
    with open('data.pkl', 'rb') as file:
        data = pickle.load(file)
    print(op(taal, "voornaamis") ,data[0] ,'.')
    print(op(taal, "achternaamis") ,data[1] , '.')
    print(op(taal, "leeftijdis") ,data[2] , ".")
    print(op(taal, "woonplaatsis"), data[3])
    print(op(taal, "etenis"), data[4])
    print(op(taal, "iestandersis"), data[5])
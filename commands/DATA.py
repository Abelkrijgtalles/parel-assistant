def main():
    import pickle
    from openeentranslate import openen as op
    from openlandcode import openen as landc

    taal = landc()
    aanhalingsteken = '"'
    data = []
    print(op(taal, "dataalgemaakt") + " " + 'J/N')
    dataalgemaakt = (str.upper(input()))
    if dataalgemaakt == 'N':
        data = []
        print(op(taal, "voornaam"))
        data.append(input())
        print(op(taal, "achternaam"))
        data.append(input())
        print(op(taal, "leeftijd"))
        data.append(input())
        print(op(taal, "woonplaats"))
        data.append(input())
        print(op(taal, "eten"))
        data.append(input())
        print(op(taal, "ietsanders"))
        data.append(input())
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
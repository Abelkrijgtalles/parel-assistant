def main():
    import pickle
    import openeentranslate
    import openlandcode

    taal = openlandcode.openen()
    aanhalingsteken = '"'
    data = []
    print(openeentranslate.openen(taal, "dataalgemaakt") + " " + 'J/N')
    dataalgemaakt = (str.upper(input()))
    if dataalgemaakt == 'N':
        data = []
        print(openeentranslate.openen(taal, "voornaam"))
        data.append(input())
        print(openeentranslate.openen(taal, "achternaam"))
        data.append(input())
        print(openeentranslate.openen(taal, "leeftijd"))
        data.append(input())
        print(openeentranslate.openen(taal, "woonplaats"))
        data.append(input())
        print(openeentranslate.openen(taal, "eten"))
        data.append(input())
        print(openeentranslate.openen(taal, "ietsanders"))
        data.append(input())
        print(openeentranslate.openen(taal, "voornaamis") ,data[0] ,'.')
        print(openeentranslate.openen(taal, "achternaamis") ,data[1] , '.')
        print(openeentranslate.openen(taal, "leeftijdis") ,data[2] , ".")
        print(openeentranslate.openen(taal, "datanogeenkeer"))
        with open('data.pkl', 'wb') as file:
            pickle.dump(data, file)
    else:
        with open('data.pkl', 'rb') as file:
            data = pickle.load(file)
        print(openeentranslate.openen(taal, "voornaamis") ,data[0] ,'.')
        print(openeentranslate.openen(taal, "achternaamis") ,data[1] , '.')
        print(openeentranslate.openen(taal, "leeftijdis") ,data[2] , ".")
        print(openeentranslate.openen(taal, "woonplaatsis"), data[3])
        print(openeentranslate.openen(taal, "etenis"), data[4])
        print(openeentranslate.openen(taal, "iestandersis"), data[5])
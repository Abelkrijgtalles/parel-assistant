import pickle
from openeentranslate import openen as op
from openlandcode import openen as landc

taal = landc
aanhalingsteken = '"'
data = []
dataalgemaakt = (str.upper(input(op(taal, "pakketinstallsuc"), 'J/N')))
if dataalgemaakt == 'N':
    data = []
    data.append(input('Wat is je voornaam? '))
    data.append(input('Wat is je achternaam? '))
    data.append(input('Wat is je leeftijd? '))
    data.append(input('In welke stad/dorp woon je? '))
    data.append(input('Wat is je lievelingseten? '))
    data.append(input('Is er nog wat anders wat je wil zeggen? '))
    print('Je voornaam is' ,data[0] ,'.')
    print('En je achternaam is dan' ,data[1] , '.')
    print('Dus dan ben je' ,data[2] ,' jaar.')
    print('Je kan', aanhalingsteken +'VertelData'+aanhalingsteken ,'typen als je alles wil zien.')
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)
else:
    with open('data.pkl', 'rb') as file:
        data = pickle.load(file)
    print('Je voornaam is', data[0])
    print('Je achternaam is', data[1])
    print('Je leeftijd is', data[2])
    print('Woont in', data[3])
    print('Je lievelings eten is', data[4])
    print('Dit wou je ook nog zeggen', data[5])
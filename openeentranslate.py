import json

def openen(taal, bestand):
    with open("teksten/" + taal + "/vertaling.json") as ietsofzo:
        ietsofzo = str(ietsofzo.read())


    iets = json.loads(ietsofzo)

    return iets[bestand]
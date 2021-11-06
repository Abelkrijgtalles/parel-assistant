import json
def openen(taal, bestand):
    with open("teksten/" + taal + "/vertaling.json") as ietsofzo:
        ietsofzo = str(ietsofzo.read())


# parse x:
    iets = json.loads(ietsofzo)

# the result is a Python dictionary:
    return iets[bestand]
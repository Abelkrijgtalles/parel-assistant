def openen(taal, bestand):
    import json
    openhet = str("teksten/" + taal + "/vertaling.json")
    with open(openhet) as ietsofzo:
        ietsofzo = str(ietsofzo.read())


    iets = json.loads(ietsofzo)

    return iets[bestand]
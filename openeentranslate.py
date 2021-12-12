def openen(taal, bestand):
    import json
    import os
    openhet = str(os.path.join("teksten", taal, "vertaling.json"))
    with open(openhet) as ietsofzo:
        ietsofzo = str(ietsofzo.read())


    iets = json.loads(ietsofzo)

    return iets[bestand]
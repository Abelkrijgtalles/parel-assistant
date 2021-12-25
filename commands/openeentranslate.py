def openen(taal, bestand):
    import json
    import os
    with open(os.path.join("teksten", taal , "vertaling.json")) as ietsofzo:
        ietsofzo = str(ietsofzo.read())


# parse x:
    iets = json.loads(ietsofzo)

# the result is a Python dictionary:
    return iets[bestand]
import os
from os.path import isfile, join
bestanden = []
pat = "./commands"
bestanden = [f for f in os.listdir(pat) if isfile(join(pat, f))]
gek = []

for bestand in bestanden:
    bestandennogiets = []
    bestandennogiets = bestand.split(".")
    try:
        achterdepunt = bestandennogiets[1]
    except os.error:
        print("geen bestand")
    if achterdepunt == "py":
        gek.append(bestand)

for bestand in gek:
    os.system("python commands/" + bestand)
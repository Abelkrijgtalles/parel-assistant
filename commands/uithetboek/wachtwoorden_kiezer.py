import random
import string

adjectieven = ["slaperige", "langzame", "stikende",
                "natte", "vette", "rode",
                "oranje", "gele", "groene",
                "blauwe", "paarse", "donzige",
                "witte", "trotse", "dappere"]

subsistantieven = ["appel", "dinosaurus", "bal",
                "toaster", "geit", "draak",
                "hamer", "eend", "panda"]

print("Welkom bij wachtwoordkiezer!")

while True:
    adjectief = random.choice(adjectieven)
    substantief = random.choice(subsistantieven)
    aantal = random.randrange(0, 100)
    speciaal_teken = random.choice(string.punctuation)
    wachtwoord = adjectief + substantief + str(aantal) + speciaal_teken
    print("Je nieuwe wachtwoord is: %s" % wachtwoord)

    antwoord = input("Wil je een ander wachtwoord? Typ j of n: ")
    if antwoord == "n":
        break
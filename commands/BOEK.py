def main():
    import openeentranslate
    import openlandcode
    import uithetboek.geheimeberichten as geheimeberichten
    import uithetboek.robotbouwer as robotbouwer
    import uithetboek.wachtwoorden_kiezer as wachtwoorden_kiezer
    
    taal = openlandcode.openen()

    print(openeentranslate.openen(taal, "watuitboek"))
    ding = str.upper(input())
    ding = ding.replace(" ", "")
    if ding == "GEHEIMEBERICHTEN":
        geheimeberichten.main()
    elif ding == "ROBOTBOUWER":
        robotbouwer.main()
    elif ding == "WACHTWOORDENKIEZER":
        wachtwoorden_kiezer.main()
def main():
    from openeentranslate import openen as op
    from openlandcode import openen as landc
    from uithetboek.geheimeberichten import main as geheimeberichten
    from uithetboek.robotbouwer import main as robotbouwer
    from uithetboek.wachtwoorden_kiezer import main as wachtwoorden_kiezer
    
    taal = landc()

    ding = str.upper(input(op(taal, "watuitboek")))
    ding = ding.replace(" ", "")
    if ding == "GEHEIMEBERICHTEN":
        geheimeberichten()
    elif ding == "ROBOTBOUWER":
        robotbouwer()
    elif ding == "WACHTWOORDENKIEZER":
        wachtwoorden_kiezer()
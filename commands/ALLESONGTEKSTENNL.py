def main():
    import webbrowser as web
    import openeentranslate
    import openlandcode

    taal = openlandcode.openen()

    print(openeentranslate.openen(taal, "zoeken"))
    nummer = str.upper(input())
    web.open('https://genius.com/search?q='+str(nummer))
    print(openeentranslate.openen(taal, "website"), 'https://genius.com/search?q='+str(nummer), openeentranslate.openen(taal, "open"))
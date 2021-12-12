def main():
    import webbrowser as web
    from openeentranslate import openen as op
    from openlandcode import openen as landc

    taal = landc()

    nummer = str.upper(input(op(taal, "zoeken")))
    web.open('https://genius.com/search?q='+str(nummer))
    print(op(taal, "website"), 'https://genius.com/search?q='+str(nummer), op(taal, "open"))
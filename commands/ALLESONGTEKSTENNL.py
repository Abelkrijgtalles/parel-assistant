def main():
    import webbrowser as web
    from openeentranslate import openen as op
    from openlandcode import openen as landc

    taal = landc()
    
    print(op(taal, "zoeken"))
    nummer = str.upper(input())
    web.open('https://genius.com/search?q='+str(nummer))
    print(op(taal, "website"), 'https://genius.com/search?q='+str(nummer), op(taal, "open"))
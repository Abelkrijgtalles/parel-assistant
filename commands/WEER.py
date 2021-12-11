def main():
    import webbrowser as web

    weerplaats = (str.upper(input('Welke plaats van verwachting? ')))
    web.open('https://www.weerplaza.nl/lib/zoeken.asp?zoektekst='+str(weerplaats))
    print('De website is geopend.')
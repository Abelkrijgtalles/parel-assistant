import webbrowser as web

nummer = input('Welk nummer wil je? ')
web.open('https://genius.com/search?q='+str(nummer))
print('De website is geopend.')
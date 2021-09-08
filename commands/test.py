from translate import Translator
import webbrowser as web

if web.open("google.com") == True:
    print("i guess")

translator= Translator(to_lang="nl")
translation = translator.translate("I play football or is it soccer?")
print(translation)

gek = 5

if gek == 5:
    print("Gekke gek")
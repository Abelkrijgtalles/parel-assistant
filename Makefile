push:
	git add .
	git commit -m ´Geen bericht opgegeven. Gewoon automatisch gedaan´
	git push -u origin master

terminal:
	python3 alleenvoorgithubtesten/testterminal.py > test.py
	python3 test.py

pushnm:
	git push -u origin master
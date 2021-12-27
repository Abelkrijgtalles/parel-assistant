push:
	make compile
	git add .
	git commit -m ´Geen bericht opgegeven. Gewoon automatisch gedaan´
	git push -u origin master

terminal:
	python3 alleenvoorgithubtesten/testterminal.py > test.py
	python3 test.py

pushnm:
	git push -u origin master

terminalsafe:
	python3 alleenvoorgithubtesten/testterminal.py > test.py

rmnl:
	rm -f -r teksten
	mkdir teksten
	cd teksten
	mkdir nl
	cd nl
	wget https://raw.githubusercontent.com/Abelkrijgtalles/parel-assistant/master/teksten/nl/vertaling.json

run:
	python3 main.py
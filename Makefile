testweb:
	pserve --reload development.ini

testcgi:
	#/usr/lib/python2.7/dist-packages/paste/deploy/__init__.py
	python htdocs/index.py

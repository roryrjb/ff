install: lint
	python setup.py install --user

lint:
	ruff check ff/

format:
	black ff/
	
exe:
	python setup.py build_exe
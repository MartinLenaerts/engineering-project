translate: # translate all diagrams
	python3 main.py

test: # launch tests
	rm -rf tests/__pycache__
	coverage  run -m pytest tests -v

test-coverage: # launch tests with coverage
	make test
	coverage html

analysis: # launch mypy analysis
	mypy **/*.py
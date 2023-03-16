translate: # translate all diagrams
	python3 main.py

test: # launch tests
	rm -rf tests/__pycache__
	coverage  run --data-file=cache/coverage/data -m pytest tests -v -o cache_dir=cache/pytest

test-coverage: # launch tests with coverage
	make test
	coverage html --directory=cache/coverage/report --data-file=cache/coverage/data
	# Report : file://$(shell pwd)/cache/coverage/report/index.html

analysis: # launch mypy analysis
	mypy **/*.py --cache-dir=cache/mypy
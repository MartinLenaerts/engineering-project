rm -rf tests/__pycache__
coverage run -m unittest discover -v
coverage report -m
rm -rf tests/__pycache__
coverage run -m unittest tests/*
coverage report -m
rm -rf tests/__pycache__
coverage  run -m pytest tests -v
coverage html
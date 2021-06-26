clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e ."[dev]" --upgrade --no-cache

install:
	# CFLAGS is used to install multi-rake without errors
	CFLAGS="-Wno-narrowing"
	# double-quotes is used because "[", "]" and "!" are special characters in some shells like zsh.
	pip install -e ."[dev]" --upgrade --no-cache

format:
	isort .
	black -l 79 --experimental-string-processing .

pep8:
	#  Flake8 ignores/changes
	#   F401 (imported but unused 'from foo import bar' often used in __init__ files)
	#	E501 (line too long (> 79 characters), I prefer 120 line leght)
	flake8 pyvideomaker --per-file-ignores="__init__.py:F401"

stats:
	pygount --format=summary .
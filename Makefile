.PHONY: default test build

default: build


.venv/.sentinel: requirements.txt dev-requirements.txt .venv
	. ./scripts/activate-venv.sh &&\
		python -m pip install -U pip &&\
		python -m pip install -r dev-requirements.txt
	touch $@

.venv:
	virtualenv --python 3.8 .venv

test: .venv/.sentinel
	. ./scripts/activate-venv.sh &&\
		coverage erase &&\
		tox

build: .venv/.sentinel
	rm -rf build
	# only wheel, because sdist leak local path 
	# https://github.com/pypa/setuptools/issues/1185
	. ./scripts/activate-venv.sh &&\
		python -m build -w

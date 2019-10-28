.PHONY: init build docs test clean

default: build
	./bin/run

init:
	pip install -r requirements.txt
	python setup.py develop

build:
	python setup.py build_ext --inplace

docs:
	sphinx-apidoc -o docs src/
	sphinx-build -M html docs docs

test:
	py.test tests

clean:
	rm -fR build/

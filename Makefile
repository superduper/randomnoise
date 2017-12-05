deps:
	pipenv install
run:
	pipenv run python3 wavez.py

.PHONY : all
.DEFAULT_GOAL := all

all: deps run

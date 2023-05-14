default: SteamworksPy.so format lint

SteamworksPy.so:
	g++ -std=c++23 -o SteamworksPy.so -shared -fPIC SteamworksPy.cpp -l steam_api -L.

lint: black isort pylint flake8

format:
	black .
	isort .

black:
	black --check .

isort:
	isort --check .

flake8:
	flake8 .

pylint:
	pylint deckfm

.PHONY: black isort flake8 pylint lint format dist

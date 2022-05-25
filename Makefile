
.empty:

build:
	python3 -m build

check:
	twine check dist/*

upload:
	twine upload dist/*

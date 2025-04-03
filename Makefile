
check:
	python -m twine check dist/*

upload:
	rm -rf build
	rm -rf dist
	python -m build
	python -m twine upload -r pypi dist/*

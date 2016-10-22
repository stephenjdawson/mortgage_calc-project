init:
	pip install -r requirements.txt

test:
	python -m pytest -vv test*

.PHONY: init test

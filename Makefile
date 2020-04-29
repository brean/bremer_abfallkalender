install:
	pipenv install -d

install-pip:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test-python:
	python3 -m pytest \
	  --doctest-modules \
	  --cov=bremer_abfallkalender/ \
	  --cov-report=html \
	  --cov-report=term \
	  ./bremer_abfallkalender \
	  ./test \
	  -vvv
	python3 -m flake8 \
		bremer_abfallkalender test
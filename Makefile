.PHONY: run

run:
	@export PYTHONPATH=${PYTHONPATH}:${PWD}; pipenv run python3 __WorkDir/${TARGET}
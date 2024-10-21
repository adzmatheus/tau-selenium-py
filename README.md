# UI Basic software test

- Clone the repo
- run: pipenv install
- run: pipenv run python -m pytest -n <'threads'>
- run: pipenv run python -m pytest tests/step_defs<'specific test'>

If using Windows: Install WSL

- Install docker
- pull selenium hub image
- pull selenium node <'browser'> image

Start WSL
Open docker desktop

- run: docker-compose up -d
- run: docker ps -a

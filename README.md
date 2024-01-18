# Poke Battle
A simple pokemon battle simulation using the nice pokeapi.co REST APIs data.

This simple CLI program will ask the user to select 2 pokemon to battle, it can show basic pokemon info fetched from pokeapi and simulate a battle between them. 
It will store cached result from the api calls in a redis for 1h max, and save in a sqlite the previous battle history informations.

Written in py3 using poetry for package management, pytest for tests and docker and docker-compose to spin up the program and dependencies easy.

## TODO
- add a new battle strategy to use moves and power level to calculate hp loss / stats decrease / increase based on the type of move
- calculate hp loss using a simplified function like: ( (2 * poke level / 5) * power * Attack [poke1] / Defense [poke2] )  / 50 + 2 * modifier [type / special attack]
- the correct battle function should also use % probability of the move!
- add more unit tests for the single components
- use a TUI like Textual lib to better handle the CLI ui! 
- show the pokemon image in battle and in ID card info.

## Development

requirements:
- py 3+
- poetry

## install project dependencies
```bash
poetry install
```

## build
```bash
poetry build
```

## run main program
```bash
poetry run main
```

## run tests
```bash
poetry run pytest
```


# Running the project using docker

## start all services
```bash
docker-compose up
```

## tear down
```bash
docker-compose down
```


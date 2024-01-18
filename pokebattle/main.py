import click
import random


from pokebattle.services.pokeApi import PokeApiService
from pokebattle.services.redisCache import RedisCache

from pokebattle.repositories.battle import PokemonBattleRepository
from pokebattle.models.pokemon import Pokemon

from pokebattle.strategies.randomStrategy import RandomStrategy
from pokebattle.services.battle import simulate_battle

# init redis client
redis_client = RedisCache(host='localhost', port=6379, db=0)
pokeService = PokeApiService(redis_client)
repository = PokemonBattleRepository()

class PokemonBattleCLI:
    def __init__(self):
        self.pokemon1 = None
        self.pokemon2 = None
        self.battle_history = []

    def display_initial_page(self):
        click.echo(click.style("Welcome to the Pokemon Battle Simulation!", fg="green"))

    def display_pokemon_selection_page(self):
        click.echo("\n1.Select Pokemons to battle!")
        click.echo("2. View Battle History")

    def select_pokemon(self):
        click.echo("\nPlease select the Pokemons to start the battle!")

        # Select Pokemon 1
        def select_pokemon_1():
            pokemon1_name = click.prompt("Enter Pokemon 1 name (default: bulbasaur)", default="bulbasaur")
            self.pokemon1 = pokeService.fetch_poke_info(pokemon1_name)
            if self.pokemon1 == None:
                return select_pokemon_1()
        select_pokemon_1()

        # Select Pokemon 2
        def select_pokemon_2():
            pokemon2_name = click.prompt("Enter Pokemon 2 name (default: charmander)", default="charmander")
            self.pokemon2 = pokeService.fetch_poke_info(pokemon2_name)
            if self.pokemon2 == None:
                return select_pokemon_2()
        select_pokemon_2()

        # Validate Pokemon names
        while not self.validate_pokemon_names():
            click.secho("Error: Please enter valid Pokemon names.", fg="red")
            return self.select_pokemon()

    def validate_pokemon_names(self):
        return self.pokemon1.name is not None and self.pokemon2.name is not None

    def display_battle_options(self):
        click.echo("\nBattle Options:")
        click.echo("1. Choose other Pokemons for battle")
        click.echo("2. Show Pokemons IDs choosen for this battle")
        click.echo("3. Start Battle!")

    def show_info_ids(self):
        click.echo("Pokemon 1 info:")
        click.echo(self.pokemon1.info())
        click.echo("Pokemon 2 info:")
        click.echo(self.pokemon2.info())

    def start_battle(self):
        click.echo(f"\nBattle between {self.pokemon1.name} and {self.pokemon2.name}!")

        poke1, poke2, winner, moves_number = simulate_battle(self.pokemon1, self.pokemon2, strategy=RandomStrategy())
        repository.insert_battle(poke1.name, poke2.name, winner.name, moves_number)
        click.secho(f"{winner.name} wins the battle!", fg="yellow")

    def display_battle_history(self):
        click.echo("\nBattle History:")
        #click.echo( repository.list_battle_history() )

        #table_data = [("id", "date", "Pokemon 1", "Pokemon 2", "Winner", "# of moves")]
        #table_data.extend(self.battle_history)

        table_data = repository.list_battle_history()
        table_data_strs = []
        for item in table_data:
            table_data_strs.append(f"""| {item[0]} | {item[1]} | {item[2]}     | {item[3]}     | {item[4]} """
            )

        tbl_str = "\n                    ".join(table_data_strs)
        click.echo(
                f"""
                    | ID | Date               | Pokemon 1     | Pokemon 2      | Winner        
                    |--------------------------------------------------------------------------
                    {tbl_str}
                """
            )




    def run(self):
        self.display_initial_page()

        while True:
            self.display_pokemon_selection_page()
            option = click.prompt("Enter your choice (1 or 2)", type=click.Choice(["1", "2"]))

            if option == "1":
                self.select_pokemon()
                while True:
                    self.display_battle_options()
                    battle_option = click.prompt("Enter your choice (1, 2 or 3)", type=click.Choice(["1", "2", "3"]))

                    if battle_option == "1":
                        self.select_pokemon()
                    elif battle_option == "2":
                        self.show_info_ids()
                    elif battle_option == "3":
                        self.start_battle()
                        break
            elif option == "2":
                self.display_battle_history()



def main():

    cli = PokemonBattleCLI()
    cli.run()

    #pokemon1 = pokeService.fetch_poke_info('bulbasaur')
    #pokemon2 = pokeService.fetch_poke_info('charmander')

    #print('\BEST pokemon winner ', repository.get_best_pokemon_winner() )
    #print('\n# of moves for win ', repository.get_battles_ordered_by_moves() )

if __name__ == "__main__":
    main()
from pokebattle.models.pokemon import Pokemon
from pokebattle.strategies.pokemonStrategy import PokemonStrategy

def simulate_battle(pokemon1: Pokemon, pokemon2: Pokemon, strategy: PokemonStrategy):
    print(f"Battle between {pokemon1.name} and {pokemon2.name}!\n")

    p1_moves = 0
    p2_moves = 0
    while not pokemon1.is_fainted() and not pokemon2.is_fainted():
        # Pokemon 1 attacks Pokemon 2
        pokemon1.attack(pokemon2, strategy)
        print(f"{pokemon2.name}'s HP: {pokemon2.stats.hp}\n")
        p1_moves += 1

        # Check if Pokemon 2 fainted
        if pokemon2.is_fainted():
            print(f"{pokemon2.name} fainted! {pokemon1.name} wins!\n")
            return pokemon1, pokemon2, pokemon1, p1_moves

        # Pokemon 2 attacks Pokemon 1
        pokemon2.attack(pokemon1, strategy)
        print(f"{pokemon1.name}'s HP: {pokemon1.stats.hp}\n")
        p2_moves += 1

        # Check if Pokemon 1 fainted
        if pokemon1.is_fainted():
            print(f"{pokemon1.name} fainted! {pokemon2.name} wins!\n")
            return pokemon1, pokemon2, pokemon2, p2_moves

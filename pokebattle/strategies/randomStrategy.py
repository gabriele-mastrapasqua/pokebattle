from pokebattle.strategies.pokemonStrategy import PokemonStrategy
import random

class RandomStrategy(PokemonStrategy):
    def choose_move(self):
        # Simulate a random move selection
        moves = ["Attack", "Defend", "Special Move"]
        return random.choice(moves)
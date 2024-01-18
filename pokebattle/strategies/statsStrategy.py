from pokebattle.strategies.pokemonStrategy import PokemonStrategy
from pokebattle.models.stats import Stats


class StatsStrategy(PokemonStrategy):
    def __init__(self, pokemon_stats: Stats):
        self.pokemon_stats = pokemon_stats

    def choose_move(self):
        # Simulate a decision based on Pokemon stats (simplified example)
        if self.pokemon_stats.attack > self.pokemon_stats.defense:
            return "Attack"
        elif self.pokemon_stats.defense > self.pokemon_stats.attack:
            return "Defend"
        else:
            return "Special Move"
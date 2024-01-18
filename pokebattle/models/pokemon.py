from dataclasses import dataclass
from typing import List
from .move import Move
from .stats import Stats
from .trait import Trait

from pokebattle.strategies.pokemonStrategy import PokemonStrategy

@dataclass
class Pokemon:
    id: int
    name: str
    level: int  # 1
    height: int
    weight: int
    image: str # from sprites['front_default']

    moves: List[Move]
    stats: Stats
    traits: List[Trait]

    def receive_damage(self, damage: int):
        self.stats.hp -= damage
        if self.stats.hp < 0:
            self.stats.hp = 0

    def is_fainted(self):
        return self.stats.hp <= 0
    
    def attack(self, opponent, strategy: PokemonStrategy):
        move = strategy.choose_move()
        print(f"{self.name} chooses {move}!")

        # Simulate battle logic (simplified)
        if move == "Attack":
            damage = 20
        elif move == "Defend":
            damage = 5
        else:
            damage = 30

        opponent.receive_damage(damage)

    def info(self):
        print(f"""
                name: {self.name}
                level: {self.level}
                height: {self.height}
                weight: {self.weight}
                hp: {self.stats.hp}
                attack: {self.stats.attack}
                defense: {self.stats.defense}
                special_attack: {self.stats.special_attack}
                special_defense: {self.stats.special_defense}
                speed: {self.stats.speed}
                type: {", ".join([x.name for x in self.traits])}
                moves: {", ".join([x.name for x in self.moves[: 6]])}
              """)
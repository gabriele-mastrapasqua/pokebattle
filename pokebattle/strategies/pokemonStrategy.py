from abc import ABC, abstractmethod

class PokemonStrategy(ABC):
    @abstractmethod
    def choose_move(self):
        pass

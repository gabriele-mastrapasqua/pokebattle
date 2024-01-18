from pokebattle.models.pokemon import Pokemon
from pokebattle.models.move import Move

from typing import List

import requests
import redis
import json 

from pokebattle.utils.parse import parse_pokemon_info

from pokebattle.intrerfaces.cacheble import Cacheable

class PokeApiService:
    def __init__(self, cacheble: Cacheable) -> None:
        self.cacheble = cacheble
        
    def fetch_poke_info(self, pokemon_name: str) -> Pokemon | None:
        '''
            fetch pokemon info from pokeapi.co or from cache if already fetched
        '''

        # Check if the data is in the cache
        cached_data = self.cacheble.get(pokemon_name)
        if cached_data:
            print(f"Using cached data for {pokemon_name}")
            return parse_pokemon_info( json.loads( cached_data.decode('utf-8') ) )

        # If not in cache, fetch data from the PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
        response = requests.get(url)

        if response.status_code == 200:
            # TODO - fetch all moves data 0-6 max
            json_data = response.json()
            self.fetch_moves(x for x in json_data['moves'][:6])

            # Store data in the cache with a timeout of 1 hour (3600 seconds)
            self.cacheble.set(pokemon_name, response.text, 3600)
            return parse_pokemon_info( json_data )
        else:
            print(f"Error: Unable to fetch data for {pokemon_name}")
            return None
        

    def fetch_moves(self, moves: [str]) -> List[Move] | None:
        moves = []

        return moves
from pokebattle.models.pokemon import Pokemon
from pokebattle.models.move import Move
from pokebattle.models.stats import Stats
from pokebattle.models.trait import Trait

def parse_pokemon_info(json_data: object) -> Pokemon:
    moves = [Move(name=x['move']['name'], url=x['move']['url']) for x in json_data['moves'][:6]  ]
    stats = Stats(
            hp=json_data['stats'][0]['base_stat'], 
            attack=json_data['stats'][1]['base_stat'], 
            defense=json_data['stats'][2]['base_stat'], 
            special_attack=json_data['stats'][3]['base_stat'], 
            special_defense=json_data['stats'][4]['base_stat'], 
            speed=json_data['stats'][5]['base_stat'], 
    )
    traits = [Trait(name=x['type']['name']) for x in json_data['types'] ]
    return Pokemon(
        id=json_data['id'],
        name=json_data['name'],
        level = 1,
        height=json_data['height'],
        weight=json_data['weight'],
        image=json_data['sprites']['front_default'],
        moves = moves,
        stats = stats,
        traits = traits,
    )
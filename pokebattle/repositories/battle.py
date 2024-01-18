import sqlite3
from datetime import datetime

class PokemonBattleRepository:
    def __init__(self, db_path='pokemon_battles.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pokemon_battle (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                battle_date TEXT NOT NULL,
                pokemon1_name TEXT NOT NULL,
                pokemon2_name TEXT NOT NULL,
                winner_name TEXT,
                num_moves INTEGER
            )
        ''')
        self.conn.commit()

    def insert_battle(self, pokemon1_name, pokemon2_name, winner_name, num_moves):
        battle_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO pokemon_battle (battle_date, pokemon1_name, pokemon2_name, winner_name, num_moves)
            VALUES (?, ?, ?, ?, ?)
        ''', (battle_date, pokemon1_name, pokemon2_name, winner_name, num_moves))
        self.conn.commit()

    def list_battle_history(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM pokemon_battle ORDER BY battle_date DESC')
        result = cursor.fetchall()
        return result

    def get_best_pokemon_winner(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT winner_name, COUNT(winner_name) as wins
            FROM pokemon_battle
            GROUP BY winner_name
            ORDER BY wins DESC
        ''')
        result = cursor.fetchall()
        return result

    def get_battles_ordered_by_moves(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT num_moves FROM pokemon_battle ORDER BY num_moves')
        result = cursor.fetchall()
        return result
    
    def close(self):
        self.conn.close()
import json
import json
import requests
import redis

class DeckOfCardsAPI:
    API_BASE_URL = "https://deckofcardsapi.com/api/deck"

    def _init_(self, deck_count=1):
        self.deck_count = deck_count
        self.deck_id = None

    def shuffle_deck(self):
        url = f"{self.API_BASE_URL}/new/shuffle/"
        params = {"deck_count": self.deck_count}
        response = requests.get(url, params=params)
        data = response.json()
        self.deck_id = data.get("deck_id")
        return self.deck_id

    def get_deck_id(self):
        return self.deck_id

class RedisDeckStorage:
    def _init_(self, redis_host="localhost", redis_port=6379, redis_db=0):
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

    def insert_deck_id(self, key, deck_id):
        self.redis_client.set(key, deck_id)

    def get_deck_id(self, key):
        return self.redis_client.get(key)

# Example usage:
if _name_ == "_main_":
    # Instantiate DeckOfCardsAPI
    deck_api = DeckOfCardsAPI()

    # Shuffle the deck and get the deck_id
    deck_id = deck_api.shuffle_deck()
    print(f"Deck ID: {deck_id}")

    # Instantiate RedisDeckStorage
    redis_storage = RedisDeckStorage()

    # Insert deck_id into Redis
    redis_key = "deck_id_01"
    redis_storage.insert_deck_id(redis_key, deck_id)
    print(f"Deck ID inserted into Redis with key '{redis_key}'")

    # Retrieve deck_id from Redis
    retrieved_deck_id = redis_storage.get_deck_id(redis_key)
    print(f"Retrieved Deck ID from Redis: {retrieved_deck_id}")

import redis

class DeckOfCardsAPI:
    API_BASE_URL = "https://deckofcardsapi.com/api/deck"

    def _init_(self, deck_count=1):
        self.deck_count = deck_count
        self.deck_id = None

    def shuffle_deck(self):
        url = f"{self.API_BASE_URL}/new/shuffle/"
        params = {"deck_count": self.deck_count}
        response = requests.get(url, params=params)
        data = response.json()
        self.deck_id = data.get("deck_id")
        return self.deck_id

    def get_deck_id(self):
        return self.deck_id

class RedisDeckStorage:
    def _init_(self, redis_host="localhost", redis_port=6379, redis_db=0):
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

    def insert_deck_id(self, key, deck_id):
        self.redis_client.set(key, deck_id)

    def get_deck_id(self, key):
        return self.redis_client.get(key)

# Example usage:
if _name_ == "_main_":
    # Instantiate DeckOfCardsAPI
    deck_api = DeckOfCardsAPI()

    # Shuffle the deck and get the deck_id
    deck_id = deck_api.shuffle_deck()
    print(f"Deck ID: {deck_id}")

    # Instantiate RedisDeckStorage
    redis_storage = RedisDeckStorage()

    # Insert deck_id into Redis
    redis_key = "deck_id_key"
    redis_storage.insert_deck_id(redis_key, deck_id)
    print(f"Deck ID inserted into Redis with key '{redis_key}'")

    # Retrieve deck_id from Redis
    retrieved_deck_id = redis_storage.get_deck_id(redis_key)
    print(f"Retrieved Deck ID from Redis: {retrieved_deck_id}")
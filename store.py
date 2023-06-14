import firebase_admin
from firebase_admin import credentials, firestore

from cachetools import cached, TTLCache

class ApiKeyStore:
    def __init__(self):
        self.cred = credentials.Certificate("/path/to/file")

        try:
            self.app = firebase_admin.get_app()
        except ValueError as e:
            firebase_admin.initialize_app(self.cred)

        self.firestore_client = firestore.client()

    def create_api_key(self, api_key: str):
        self.firestore_client.collection('keys').document(api_key).set({})

    @cached(cache=TTLCache(maxsize=1024, ttl=60)) # NEW
    def does_api_key_exist(self, api_key: str) -> bool:
        doc = self.firestore_client.collection('keys').document(api_key).get()
        print("Fetched API Key {} from database".format(api_key))
        return doc.exists

api_key_store = ApiKeyStore()


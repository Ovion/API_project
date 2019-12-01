from pymongo import MongoClient
from requirements.constants import MONGO, USER, KEY


class ConectColl:
    def __init__(self):
        self.client = MongoClient(MONGO.format(USER, KEY))
        self.db = self.client['Slack']
        self.coll = self.db['Chats']

    def add_doc(self, docu):
        aux = self.coll.insert_one(docu)
        print("Inserted: ", aux.inserted_id)
        return aux.inserted_id

    def add_chat(self, user, channel, text):
        document = {
            'user': user,
            'channel': channel,
            'text': text
        }
        return self.add_doc(document)

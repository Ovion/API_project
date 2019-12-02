from pymongo import MongoClient
from requirements.constants import MONGO, USER, KEY
from bson.json_util import loads, dumps


class ConectColl:
    def __init__(self):
        self.client = MongoClient(MONGO.format(USER, KEY))
        self.db = self.client['Slack']
        self.chats = self.db['Chats']
        self.users = self.db['Users']

    def add_doc_chats(self, docu):
        aux = self.chats.insert_one(docu)
        print("Inserted: ", aux.inserted_id)
        return aux.inserted_id

    def add_doc_users(self, docu):
        aux = self.users.insert_one(docu)
        print("Inserted: ", aux.inserted_id)
        return aux.inserted_id

    def last_id_user(self):
        return list(self.users.find({}, {"id_user": 1, "_id": 0}).sort([('id_user', -1)]).limit(1))[0]['id_user']

    def last_id_chat(self):
        return list(self.chats.find({}, {"id_chat": 1, "_id": 0}).sort([('id_chat', -1)]).limit(1))[0]['id_chat']

    def add_chat(self, id_user, channel, text):
        user = list(self.users.find({"id_user": int(id_user)}))[0]["user"]
        id_chat = self.last_id_chat()+1
        # id_chat = 1
        document = {
            'user': user,
            'id_user': id_user,
            'channel': channel,
            'text': text,
            'id_chat': id_chat
        }
        return self.add_doc_chats(document), id_chat

    def add_user(self, user):
        id_user = self.last_id_user()+1
        # id_user = 1
        document = {
            "id_user": id_user,
            "user": user
        }
        return self.add_doc_users(document), id_user

    def get_chats(self):
        return dumps(self.chats.find({}, {'_id': 0, 'id_user': 0, 'id_chat': 0}))

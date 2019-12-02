from bottle import route, run, get, post, request
from Mongo import ConectColl


@post('/user/new')
def add_user():
    user = request.forms.get('user')
    _id, id_user = coll.add_user(user)
    return {
        "inserted_doc": str(_id),
        "user_id": id_user
    }


@post('/conversation/new')
def add_conver():
    id_user = int(request.forms.get('id_user'))
    channel = request.forms.get('channel')
    text = request.forms.get('text')
    _id, id_chat = coll.add_chat(id_user, channel, text)
    return{
        'inserted_doc': str(_id),
        'chat_id': id_chat
    }


coll = ConectColl()
run(host='0.0.0.0', port=8080)

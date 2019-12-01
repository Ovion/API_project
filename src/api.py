from bottle import route, run, get, post, request
from Mongo import ConectColl


@post('/conversation/new')
def add_conver():
    user = request.forms.get('user')
    channel = request.forms.get('channel')
    text = request.forms.get('text')
    return{
        'inserted_doc': str(coll.add_chat(user, channel, text))
    }


coll = ConectColl()
run(host='0.0.0.0', port=8080)

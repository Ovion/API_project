from bottle import route, run, get, post, request
from Mongo import ConectColl
import sentiments as st


@get('/conversations')
def get_convers():
    '''
    This get function return all the conversations
    '''
    return coll.get_chats()


@get('/conversations/sentimental')
def get_conv_sent():
    '''
    This get returns a sentimental analysis of the users in the chat.
    First sugguest your bestfriend, and then the side of the light, i.e.
    Dark Side if the user embrace the path of the angry, hate, fear.
    Light Side if the user embrace the path of equilibrium.
    '''
    all_data = coll.get_chats_lst()
    print('Friend recommendation: ')
    friend = st.friend_recomm(all_data)
    print('Side recommendation: ')
    side = st.side_recomm(all_data)
    return friend, side


@get('/users')
def get_lst_users():
    '''
    This get function return a dictionary with users name as key, and 
    user_id as values
    '''
    return coll.dict_user()


@post('/user/new')
def add_user():
    '''
    Here you can create a new user, the system will validate that the user, does not exist yet
    '''
    user = request.forms.get('user')
    _id, id_user = coll.add_user(user)
    return {
        "inserted_doc": str(_id),
        "user_id": id_user
    }


@post('/conversation/new')
def add_conver():
    '''
    Here you can add new conversations, read the readme for an example
    '''
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

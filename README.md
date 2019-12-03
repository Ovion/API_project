# API_project
In this project I create an API, in which you can post messages from an user in a chat. You can also get the information back, and if you want, a sentimental analysis of the chat.

I worked with bottle to create the API and MongoDB Atlas as DB

## How it works
---------------

First of all you must keep runing the api.py file in the terminal.

### @post

- /user/new \
With this command you can create a new user, if the user already exits it would raise an error. Below you have an example of creating a new character:
    ```
    url = 'http://localhost:8080/user/new'
    params = {
        'user': 'Luke Skywalker'
    }
    requests.post(url, data=params).text
    ```

- /conversation/new \
With this command you can create a new conversation. You must give an id_user, a channel and the text that the user wrote. Here you have an example:

    ```
    url = 'http://localhost:8080/conversation/new'
    params = {
        'id_user': 7,
        'channel': 'Sith',
        'text': "You will burn these ideas away"
    }
    requests.post(url, data = params).text
    ```

### @get

- /conversations \
This will return all the conversations saved in MongoDB Atlas

    ```
    url = 'http://localhost:8080/conversations'
    all_data = requests.get(url)
    ```

- /sentimental/friend \
With this get you recive a dictionary with the friends recommendation for each user:

    ```
    url = 'http://localhost:8080/sentimental/friend'
    requests.get(url).text
    ```

- /sentimental/side \
Finally with this get you will recive a dictionary with the recommendation of each preference of the users to join determinate side of the light

    ```
    url = 'http://localhost:8080/sentimental/side'
    requests.get(url).text
    ```
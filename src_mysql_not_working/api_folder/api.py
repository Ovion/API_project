
from bottle import route, run, get, post, request
import psycopg2
import getpass
import mysql as sql


password = getpass.getpass("Insert your mysql root password: ")
conn = psycopg2.connect(
    host="localhost", database="api_project", user="root", password=f"{password}")


@post('/new_user')
def create_user():
    name = str(request.forms.get("name"))
    sql.insert_user(name)


run(host='localhost', port=8080)

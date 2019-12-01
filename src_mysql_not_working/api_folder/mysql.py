
import psycopg2
import getpass
# from config_mysql import config


password = getpass.getpass("Insert your mysql root password: ")
conn = psycopg2.connect(
    host="localhost", database="api_project", user="root", password=f"{password}")


def create_tables(conn=conn):
    commands = (
        """
        CREATE TABLE IF NOT EXISTS api_project.channels (
            id_channels INT NOT NULL,
            PRIMARY KEY (id_channels))
        """,
        """
        CREATE TABLE IF NOT EXISTS api_project.users (
            id_users INT NOT NULL,
            user_name VARCHAR(45) NULL,
            PRIMARY KEY (id_users))
        """,
        """
        CREATE TABLE IF NOT EXISTS api_project.messages (
            id_messages INT NOT NULL,
            users_id_users INT NOT NULL,
            channels_id_channels INT NOT NULL,
            text VARCHAR(255) NULL,
            PRIMARY KEY (id_messages),
            INDEX fk_messages_users_idx (users_id_users ASC) VISIBLE,
            INDEX fk_messages_channels1_idx (channels_id_channels ASC) VISIBLE,
        CONSTRAINT fk_messages_users
            FOREIGN KEY (users_id_users)
                REFERENCES api_project.users (id_users)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
        CONSTRAINT fk_messages_channels1
            FOREIGN KEY (channels_id_channels)
                REFERENCES api_project.channels (id_channels)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)
        """,
    )

    try:
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()


def insert_user(user_name, conn=conn):
    sql = """INSERT INTO api_project.users(user_name)
            VALUES(%s) RETURNING id_users;"""
    # conn = None
    id_users = None
    try:
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (user_name,))
        # get the generated id back
        id_users = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()

    return id_users

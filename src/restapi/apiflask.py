"""
Call http://localhost:5000
Local py-service: get, add, edit, search GET methods
"""

from flask import Flask
import json
from flask import request
import psycopg2.extras
import psycopg2
from flask import jsonify
from dataclasses import dataclass
from psycopg2.extras import RealDictCursor

api = Flask(__name__)

conn = psycopg2.connect(database="habrdb",
                        host="localhost",
                        user="habrpguser",
                        password="pgpwd4habr",
                        port="5432")
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


# curl "http://localhost:5000/get?id=1"
@api.route('/get', methods=['GET'])
def get_get():
    get_id = request.args.get("id")
    if get_id is None or not get_id.isnumeric():
        raise Exception('id', 'id must be numeric')

    cursor.execute("SELECT * FROM document_template WHERE id = %s", get_id)
    fetch = cursor.fetchall()
    close()
    data = [dict(row) for row in fetch]
    return jsonify(data)


# curl "http://localhost:5000/edit?id=1&name=Kirill&description=Simplepope5"
@api.route('/edit', methods=['GET'])
def get_edit():
    args = request.args
    return_message = {}
    if len(args) != 3 or args['id'] == "":
        return_message["result"] = "false"
        return_message["error"] = "There is not correct count of parameters"
        return json.dumps(return_message)

    try:
        cursor.execute("UPDATE document_template SET "
                       "NAME = %s, "
                       "DESCRIPTION = %s "
                       "WHERE id = %s", (args['name'], args['description'], args['id']))
        conn.commit()
        close()
        return_message["result"] = "success"
        return_message["id"] = args['id']
    except Exception as err:
        return_message["result"] = "false"
        return_message["error"] = "Cant update data"

    return json.dumps(return_message)


# curl "http://localhost:5000/add?name=Peter&description=Gandalf"
@api.route('/add', methods=['GET'])
def get_add():
    args = request.args
    return_message = {}
    if len(args) != 2:
        return_message["result"] = "false"
        return_message["error"] = "There is not correct count of parameters"
        return json.dumps(return_message)
    try:
        cursor.execute("SELECT COUNT(*) FROM document_template")
        count = cursor.fetchone()
        id = count['count'] + 1
        cursor.execute(
            "INSERT INTO document_template (ID, NAME, DESCRIPTION) "
            "VALUES(%s, %s, %s)",
            (id, args['name'], args['description']))
        conn.commit()
        close()
        return_message["result"] = "success"
        return_message["id"] = id
    except Exception as err:
        return_message["result"] = "false"
        return_message["error"] = "Cant insert new data"
        return json.dumps(return_message)
    return json.dumps(return_message)


# curl "http://localhost:5000/search?cnt=3&order=DESC"
@api.route('/search', methods=['GET'])
def get_search():
    cnt = request.args.get("cnt")
    order = request.args.get("order")
    if cnt is None or not cnt.isnumeric():
        raise Exception('cnt', 'Parameter cnt is not correct')

    desc = "DESC"
    if order is not None and order.upper() in ("DESC", "ASC"):
        desc = order

    try:
        cursor.execute("SELECT * FROM document_template ORDER BY id " + desc + " LIMIT(" + cnt + ")")
    except Exception as err:
        raise Exception('select', err)

    fetch = cursor.fetchall()
    data = [dict(row) for row in fetch]
    close()
    return jsonify(data)


def close():
    cursor.close()
    conn.close()


if __name__ == '__main__':
    api.run()

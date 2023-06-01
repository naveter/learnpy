"""
Call http://localhost:5000
request.args: the key/value pairs in the URL query string
request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
request.files: the files in the body, which Flask keeps separate from form. HTML forms must use enctype=multipart/form-data or files will not be uploaded.
request.values: combined args and form, preferring args if keys overlap
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


@api.route('/search', methods=['GET'])
def get_search():
    get_id = request.args.get("id")
    if get_id is None or not get_id.isnumeric():
        raise Exception('id', 'id must be numeric')

    cursor.execute("SELECT * FROM document_template WHERE id = %s", get_id)
    fetch = cursor.fetchall()
    close()
    data = [dict(row) for row in fetch]

    return jsonify(data)


@api.route('/change', methods=['GET'])
def get_change():
    args = request.args
    return_message = {}
    if len(args) != 3 and len(args) != 2:
        return_message["result"] = "false"
        return_message["error"] = "There is not correct count of parameters"
        return json.dumps(return_message)

    if args['id'] != "":  # Edit
        try:
            cursor.execute("UPDATE document_template SET "
                           "NAME = %s, "
                           "DESCRIPTION = %s "
                           "WHERE id = %s", (args['name'], args['description'], args['id']))
            conn.commit()
        except Exception as err:
            return_message["result"] = "false"
            return_message["error"] = "Cant update data"
            return json.dumps(return_message)

        return_message["result"] = "success"
        return_message["id"] = args['id']
    else:  # Add
        try:
            cursor.execute("SELECT COUNT(*) FROM document_template")
            count = cursor.fetchone()

            cursor.execute(
                "INSERT INTO document_template (ID, NAME, DESCRIPTION "
                "VALUES(%s, %s, %s)",
                (count + 1, args['name'], args['description']))
            conn.commit()
        except Exception as err:
            return_message["result"] = "false"
            return_message["error"] = "Cant insert new data"
            return json.dumps(return_message)

        return_message["result"] = "Success"
        return_message["id"] = count + 1

    close()
    return_message["result"] = "success"
    return_message["id"] = args['id']
    return json.dumps(return_message)


def close():
    cursor.close()
    conn.close()


if __name__ == '__main__':
    api.run()

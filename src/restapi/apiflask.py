"""
Call http://localhost:5000/companies
request.args: the key/value pairs in the URL query string
request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
request.files: the files in the body, which Flask keeps separate from form. HTML forms must use enctype=multipart/form-data or files will not be uploaded.
request.values: combined args and form, preferring args if keys overlap
"""

from flask import Flask
import json
from flask import request

api = Flask(__name__)


@api.route('/get', methods=['GET'])
def get_get():
    get_id = request.args.get("id")
    return json.dumps(get_id)


@api.route('/add', methods=['GET'])
def get_add():
    args = request.args
    return json.dumps(args)


@api.route('/search', methods=['GET'])
def get_search():
    search = request.args
    return json.dumps(search)


if __name__ == '__main__':
    api.run()
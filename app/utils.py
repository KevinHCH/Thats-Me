import os
import hashlib
from flask import make_response
from json import dumps, loads


def json_encode(raw):
	return make_response(dumps(raw, default=str))


def json_decode(str):
	return loads(str)

def file_exists(file):
	return os.path.exists(file)

def md5(value):
	encrypted = hashlib.md5(value.encode())
	return encrypted.hexdigest()
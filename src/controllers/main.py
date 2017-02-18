from flask import *
from extensions import *

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
	# find all keys with -machine
	db = current_app.extensions['redis']['REDIS']
	possible_channels = ['asdf', 'asdf1', 'asdf2']
	db.lpush('key1', *possible_channels)
	print(db.lrange('key1',0,-1)[0])
	return jsonify(db.lrange('key1',0,-1))

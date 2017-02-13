from flask import *
from extensions import *

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
	print current_app.extensions['redis']['REDIS']
	db = current_app.extensions['redis']['REDIS']
	db.set('key', 'value')
	return jsonify(db.get('key'))

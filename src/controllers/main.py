from flask import *
from extensions import *

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
	
	return jsonify(SiteStore)

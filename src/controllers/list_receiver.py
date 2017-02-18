from flask import *
from extensions import *

list_receiver = Blueprint('list_receiver', __name__, template_folder='templates')

@list_receiver.route('/v1/listreceiver/<target>', methods=["POST", "PUT"])
def list_receiver_route(target):

	req_json = request.json()
	db = current_app.extensions['redis']['REDIS']
	
	# get existing object from redis
	# key should be clientid-machine
	# update fields from req_json in stored value
	# store back to redis
	return


from flask import *
from extensions import *

machine_receiver = Blueprint('machine_receiver', __name__, template_folder='templates')

@machine_receiver.route('/v1/machinereceiver/<target>', methods=["POST", "PUT"])
def machine_receiver_route(target):

	req_json = request.json()
	db = current_app.extensions['redis']['REDIS']
	
	# get existing object from redis
	# key should be clientid-machine
	# update fields from req_json in stored value
	# store back to redis
	return


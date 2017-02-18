from flask import *
from extensions import *

site_reporter = Blueprint('site_reporter', __name__, template_folder='templates')

@site_reporter.route('/v1/reporter/<clientId>', methods=["POST", "PUT"])
def site_reporter_route(clientId, service):
	req_json = request.json()
	# get existing object from redis
	# key should be clientid-machine
	# update fields from req_json in stored value
	# store back to redis
	if not clientId in SiteStore:
		SiteStore[clientId] = []
	SiteStore[clientId] = (service, requests.get)
	return


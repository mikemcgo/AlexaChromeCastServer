from flask import *
from extensions import *

site_reporter = Blueprint('main', __name__, template_folder='templates')

@site_reporter.route('/reporter/<clientId>/<service>')
def site_reporter_route(clientId, service):
	if not clientId in SiteStore:
		SiteStore[clientId] = []
	SiteStore[clientId] = (service, requests.get)


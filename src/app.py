from flask import Flask
from flask_redis import Redis
import controllers
import config 

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

app.config['REDIS_HOST'] = '127.0.0.1'
app.config['REDIS_PORT'] = 6379
app.config['REDIS_DB'] = 0
app.config['REDIS_PASSWORD'] = "foobared"

redis = Redis(app)

# Register the controllers
app.register_blueprint(controllers.main)
app.register_blueprint(controllers.machine_receiver)
app.register_blueprint(controllers.list_receiver)

# Listen on external IPs using the configured port
if __name__ == '__main__':
    app.run(host=config.env['host'], port=config.env['port'], debug=True)

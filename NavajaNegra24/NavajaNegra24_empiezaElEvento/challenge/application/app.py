from flask import Flask, jsonify
from application.blueprints.routes import proxy_dec, flag_dec

app = Flask(__name__)
app.config.from_object('application.config.Config')

app.register_blueprint(proxy_dec, url_prefix='/')
app.register_blueprint(flag_dec, url_prefix='/admin')

@app.errorhandler(404)
def not_found(error):
    return {'ERROR': 'Not Found'}, 404

@app.errorhandler(403)
def forbidden(error):
    return {'ERROR': 'Not Allowed! Remember which the restricted URLs are.'}, 403

@app.errorhandler(400)
def bad_request(error):
    return {'ERROR': 'Bad Request'}, 400
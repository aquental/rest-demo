#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)

users = { 'user':'pass', 'usuario':'senha', 'cliente':'s3nh@' }

@auth.get_password
def get_password(username):
    pasw=users[username]
    if len(pasw) == 0:
        return None
    return pasw

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/demo/api/v1.0/soma', methods=['POST'])
@auth.login_required
def soma():
    if request.headers['Content-Type'] == 'application/json':
        #print request.headers['Content-Type']
        #print request.json
        if not request.json or not 'a' in request.json or not 'b' in request.json:
            abort(400)
        try:
            a = int(request.json['a'])
            b = int(request.json['b'])
            c = a + b
            return jsonify({'res':c})
        except:
            abort(400)
    abort(400)

@app.route('/demo/api/v1.0/version', methods=['GET'])
def version():
    return jsonify({'version': '1.0'})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

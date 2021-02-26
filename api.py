"""API pomocí flask_restful. Nainstaluješ (pip install flask-restful). Funguje jako Falcon - pomocí class.

JSONIFY teď nepoužiješ. Převádí dict->JSON:    jsonify({key1:value1, key2:value2}). Hodí se u basic flask API. Flask_restful to dělá sám.
"""


from flask import Flask, url_for, render_template, request, jsonify
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'about':"Hello World introduction"}
    def post(self):
        some_json = request.get_json()
        return {'You send': some_json}, 201


class Multiply10(Resource):
    def get(self, num):
        return {'vysledek': num*10}

api.add_resource(HelloWorld,'/')
api.add_resource(Multiply10,'/multi/<int:num>')



# ========================== RUN ======================
if __name__ == '__main__':
    app.run(debug=True)
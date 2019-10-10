from flask import request
from flask_restful import Resource

class CategoryResource(Resource):
    def get(self):
        return {'status': 'success', 'data': 'ok'}, 200
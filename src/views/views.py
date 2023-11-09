from flask_restful import Resource
from flask import request
from datetime import datetime


class VistaPong(Resource):

    def get(self):
        # Retorna pong si el servicio se encuentra en linea: /
        return 'pong proyectos v1.0', 200

from flask_restful import Resource
from flask import request
from datetime import datetime
from src.models import db, Project, ProjectSchema

projecy_schema = ProjectSchema()


class VistaPong(Resource):

    def get(self):
        # Retorna pong si el servicio se encuentra en linea: /
        return 'pong proyectos v1.0', 200


class VistaProyectos(Resource):

    def post(self, idCompany):
        # Crea un proyecto para una empresa: project/<idCompany>

        try:
            project = request.get_json()
            project['idCompany'] = idCompany
            project['startDate'] = datetime.strptime(
                project['startDate'], '%d/%m/%Y')
            project['endDate'] = datetime.strptime(
                project['endDate'], '%d/%m/%Y')
            project = Project(**project)

            db.session.add(project)
            db.session.commit()

            return projecy_schema.dump(project), 201

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400

    def get(self, idCompany):
        # Retorna todos los proyectos de una empresa: project/<idCompany>

        try:
            projects = Project.query.filter_by(idCompany=idCompany).all()

            if projects:
                return projecy_schema.dump(projects, many=True), 200
            else:
                return {'error': 'No se encontraron proyectos'}, 404

        except Exception as e:
            return {'error': str(e)}, 400

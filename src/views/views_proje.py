from flask_restful import Resource
from flask import request
from datetime import datetime
from src.models import db, Project, ProjectSchema, ProjectDetailShema, ProjectAspirant, ProjectAspirantSchema

project_schema = ProjectSchema()
project_detail_schema = ProjectDetailShema()
project_aspirant_schema = ProjectAspirantSchema()


class VistaPong(Resource):

    def get(self):
        # Retorna pong si el servicio se encuentra en linea: /
        return 'pong proyectos v2.0', 200


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

            return project_schema.dump(project), 201

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400

    def get(self, idCompany):
        # Retorna todos los proyectos de una empresa: project/<idCompany>

        try:
            projects = Project.query.filter_by(idCompany=idCompany).all()

            if projects:
                return project_detail_schema.dump(projects, many=True), 200
            else:
                return {'error': 'No se encontraron proyectos'}, 404

        except Exception as e:
            return {'error': str(e)}, 400


class VistaAspiranteProyecto(Resource):

    def post(self, idProject):
        # Crea un aspirante para un proyecto: aspirant/<idProject>

        try:
            aspirant = request.get_json()
            aspirant['idProject'] = idProject

            project = Project.query.filter_by(id=idProject).first()
            aspirants = ProjectAspirant.query.filter_by(
                idProject=idProject).all()

            if not project:
                return {'error': 'El proyecto no existe'}, 404

            if len(aspirants) >= project.aspirants:
                return {'error': 'El proyecto ya tiene el numero maximo de aspirantes'}, 400

            aspirant = ProjectAspirant(**aspirant)

            db.session.add(aspirant)
            db.session.commit()

            return {'mensaje': 'Aspirante asociado exitosamente'}, 201

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400

    def get(self, idProject):
        # Retorna todos los aspirantes de un proyecto y la información del proyecto: aspirant/<idProject>

        try:
            project = Project.query.filter_by(id=idProject).first()

            aspirants = ProjectAspirant.query.filter_by(
                idProject=idProject).all()

            if not project:
                return {'error': 'El proyecto no existe'}, 404

            aspirants_detail = project_aspirant_schema.dump(
                aspirants, many=True)

            project_detail = project_detail_schema.dump(project)

            return {'project': project_detail, 'aspirants': aspirants_detail}, 200

        except Exception as e:
            return {'error': str(e)}, 400

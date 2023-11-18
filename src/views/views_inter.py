from flask_restful import Resource
from flask import request
from datetime import datetime
from src.models import db, Interview, InterviewAspirantSchema, InterviewCompanySchema

interview_aspirant_schema = InterviewAspirantSchema()
interview_company_schema = InterviewCompanySchema()


class VistaEntrevistas(Resource):

    def post(self, idCompany):
        # Crea una entrevista para una empresa: interview/<idCompany>

        try:
            interview = request.get_json()
            interview['idCompany'] = idCompany
            interview['date'] = datetime.strptime(
                interview['date'], '%d/%m/%Y %H:%M')
            interview = Interview(**interview)

            db.session.add(interview)
            db.session.commit()

            return {'mensaje': 'Entrevista creada exitosamente'}, 201

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400

    def get(self, idCompany):
        # Retorna todas las entrevistas de una empresa: interview/<idCompany>

        try:
            interviews = Interview.query.filter_by(idCompany=idCompany).all()

            if interviews:
                return interview_company_schema.dump(interviews, many=True), 200
            else:
                return {'error': 'No se encontraron entrevistas'}, 404

        except Exception as e:
            return {'error': str(e)}, 400


class VistaEntrevistasAspirante(Resource):

    def get(self, idAspirant):
        # Retorna todas las entrevistas de un aspirante: interview/aspirant/<idAspirant>

        try:
            interviews = Interview.query.filter_by(idAspirant=idAspirant).all()

            if interviews:
                return interview_aspirant_schema.dump(interviews, many=True), 200
            else:
                return {'error': 'No se encontraron entrevistas'}, 404

        except Exception as e:
            return {'error': str(e)}, 400

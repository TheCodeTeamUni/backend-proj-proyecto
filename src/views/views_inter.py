from flask_restful import Resource
from flask import request
from datetime import datetime
from src.models import db, Interview, InterviewResult, InterviewAspirantSchema, InterviewCompanySchema, InterviewResultSchema

interview_aspirant_schema = InterviewAspirantSchema()
interview_company_schema = InterviewCompanySchema()
interview_result_schema = InterviewResultSchema()


class VistaEntrevistas(Resource):

    def post(self, idCompany):
        # Crea una entrevista para una empresa: interview/company/<idCompany>

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
        # Retorna todas las entrevistas de una empresa: interview/company/<idCompany>

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


class VistaEntrevista(Resource):

    def get(self, idInterview):
        # Retorna una entrevista de una empresa y un aspirante: interview/<idInterview>

        try:
            interview = Interview.query.filter_by(id=idInterview).first()

            if interview:
                return interview_company_schema.dump(interview), 200
            else:
                return {'error': 'No se encontró la entrevista'}, 404

        except Exception as e:
            return {'error': str(e)}, 400


class VistaEntrevistaResultado(Resource):

    def post(self, idInterview):
        # Crea un resultado de entrevista para una entrevista: interview/result/<idInterview>

        try:
            result = request.get_json()
            result['idInterview'] = idInterview

            interview = Interview.query.filter_by(id=idInterview).first()

            if not interview:
                return {'error': 'No se encontró la entrevista'}, 404

            resultInterview = InterviewResult.query.filter_by(
                idInterview=idInterview).first()

            if resultInterview:
                return {'error': 'Ya existe un resultado para esta entrevista'}, 400

            result = InterviewResult(**result)

            db.session.add(result)
            db.session.commit()

            return {'mensaje': 'Resultado de entrevista creado exitosamente'}, 201

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400

    def get(self, idInterview):
        # Retorna un resultado de entrevista para una entrevista: interview/result/<idInterview>

        try:
            result = InterviewResult.query.filter_by(
                idInterview=idInterview).first()

            if result:
                return interview_result_schema.dump(result), 200
            else:
                return {'error': 'No se encontró el resultado de entrevista'}, 404

        except Exception as e:
            return {'error': str(e)}, 400

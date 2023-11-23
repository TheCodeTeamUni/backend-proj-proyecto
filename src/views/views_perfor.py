from flask_restful import Resource
from flask import request
from datetime import datetime
from src.models import db, Performance


class VistaPerformance(Resource):

    def post(self, idAspirant):
        # Crea una evaluación del desempeño a un aspirante: performance/<idAspirant>

        try:
            performance = request.get_json()
            performance['idAspirant'] = idAspirant
            performance = Performance(**performance)

            db.session.add(performance)
            db.session.commit()

            return {'mensaje': 'Evaluación creada exitosamente'}, 201

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400

    def get(self, idAspirant):
        # Retorna todas las evaluaciones de un aspirante: performance/<idAspirant>

        try:
            performances = Performance.query.filter_by(
                idAspirant=idAspirant).all()

            if performances:

                promedio = 0
                for performance in performances:
                    promedio += performance.performance

                promedio = promedio / len(performances)

                return {'Promedio desempeño aspirante': promedio}, 200

            else:
                return {'error': 'No se encontraron evaluaciones'}, 404

        except Exception as e:
            return {'error': str(e)}, 400

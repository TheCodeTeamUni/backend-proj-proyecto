from flask_restful import Resource
from flask import request
from datetime import datetime
from src.models import db, Test, TestSchema

test_schema = TestSchema()

class VistaPruebas(Resource):

    def post(self, idCompany):
        # Crea una prueba tecnica de una empresa para un aspirante: test/company/<idCompany>
        try:
            test = request.get_json()
            test['idCompany'] = idCompany
            test['date'] = datetime.strptime(
                test['date'], '%d/%m/%Y %H:%M')
            test = Test(**test)

            db.session.add(test)
            db.session.commit()

            return {'mensaje': 'Prueba creada exitosamente'}, 201

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400
        
    def get(self, idCompany):
        # Retorna todas las pruebas de una empresa: test/company/<idCompany>
        try:
            tests = Test.query.filter_by(idCompany=idCompany).all()

            if tests:
                return test_schema.dump(tests, many=True), 200
            else:
                return {'error': 'No se encontraron pruebas'}, 404

        except Exception as e:
            return {'error': str(e)}, 400
        
class VistaPruebasAspirante(Resource):

    def get(self, idAspirant):
        # Retorna todas las pruebas de un aspirante: test/aspirant/<idAspirant>
        try:
            tests = Test.query.filter_by(idAspirant=idAspirant).all()

            if tests:
                return test_schema.dump(tests, many=True), 200
            else:
                return {'error': 'No se encontraron pruebas'}, 404

        except Exception as e:
            return {'error': str(e)}, 400
import json
from unittest import TestCase
from faker import Faker
from application import application as app
from src.models import db, Performance


class TestPerformance(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    def tearDown(self):
        performances = Performance.query.all()
        for performance in performances:
            db.session.delete(performance)

        db.session.commit()

    def test_create_performance(self):

        data = {
            "performance": 5
        }

        headers = {'Content-Type': 'application/json'}

        sol_performance = self.client.post("/performance/1",
                                           data=json.dumps(data),
                                           headers=headers)

        self.assertEqual(sol_performance.status_code, 201)

    def test_get_performance(self):

        performance = Performance(performance=5, idAspirant=1)

        db.session.add(performance)
        db.session.commit()

        sol_performance = self.client.get("/performance/1")

        self.assertEqual(sol_performance.status_code, 200)
        self.assertEqual(json.loads(sol_performance.data)['Promedio desempeño aspirante'], 5)

    def test_get_performance_fail(self):

        sol_performance = self.client.get("/performance/1")

        self.assertEqual(sol_performance.status_code, 404)
        self.assertEqual(json.loads(sol_performance.data)['error'], 'No se encontraron evaluaciones')
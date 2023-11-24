import json
from unittest import TestCase
from faker import Faker
from application import application as app
from src.models import db, Test


class TestTest(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    def tearDown(self):
        tests = Test.query.all()
        for test in tests:
            db.session.delete(test)

        db.session.commit()

    def test_create_test(self):

        data = {
            "idAspirant": 1,
            "nameTest": self.data_factory.name(),
            "date": '01/01/2020 16:00',
            "result": "Excelente",
            "notes": self.data_factory.text()
        }

        headers = {'Content-Type': 'application/json'}

        sol_test = self.client.post("/test/company/1",
                                    data=json.dumps(data),
                                    headers=headers)

        self.assertEqual(sol_test.status_code, 201)

    def test_create_test_fail(self):

        data = {
            "idAspirant": 1,
            "nameTest": self.data_factory.name(),
            "date": '01-01-2020 16:00',
            "result": "Excelente",
            "notes": self.data_factory.text()
        }

        headers = {'Content-Type': 'application/json'}

        sol_test = self.client.post("/test/company/1",
                                    data=json.dumps(data),
                                    headers=headers)

        self.assertEqual(sol_test.status_code, 400)

    def test_get_test_company(self):

        data = {
            "idAspirant": 1,
            "nameTest": self.data_factory.name(),
            "date": '01/01/2020 16:00',
            "result": "Excelente",
            "notes": self.data_factory.text()
        }

        headers = {'Content-Type': 'application/json'}

        sol_test = self.client.post("/test/company/1",
                                    data=json.dumps(data),
                                    headers=headers)

        sol_test = self.client.get("/test/company/1", headers=headers)

        self.assertEqual(sol_test.status_code, 200)

    def test_get_test_company_fail(self):

        sol_test = self.client.get("/test/company/1")

        self.assertEqual(sol_test.status_code, 404)

    def test_get_test_aspirant(self):

        data = {
            "idAspirant": 1,
            "nameTest": self.data_factory.name(),
            "date": '01/01/2020 16:00',
            "result": "Excelente",
            "notes": self.data_factory.text()
        }

        headers = {'Content-Type': 'application/json'}

        sol_test = self.client.post("/test/company/1",
                                    data=json.dumps(data),
                                    headers=headers)

        sol_test = self.client.get("/test/aspirant/1")

        self.assertEqual(sol_test.status_code, 200)
        self.assertEqual(len(sol_test.json), 1)

    def test_get_test_aspirant_fail(self):

        sol_test = self.client.get("/test/aspirant/1")

        self.assertEqual(sol_test.status_code, 404)

import json
from unittest import TestCase
from faker import Faker
from application import application as app
from src.models import db, Interview


class TestInterview(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    def tearDown(self):
        interviews = Interview.query.all()
        for interview in interviews:
            db.session.delete(interview)

        db.session.commit()

    def test_create_interview(self):

        data = {
            "nameCompany": self.data_factory.name(),
            "idAspirant": 1,
            "nameAspirant": self.data_factory.name(),
            "lastNameAspirant": self.data_factory.name(),
            "role": self.data_factory.name(),
            "date": '01/01/2020 16:00',
            "notes": self.data_factory.text()
        }

        headers = {'Content-Type': 'application/json'}

        sol_interview = self.client.post("/interview/company/1",
                                         data=json.dumps(data),
                                         headers=headers)

        self.assertEqual(sol_interview.status_code, 201)

    def test_create_interview_fail(self):

        data = {
            "nameCompany": self.data_factory.name(),
            "idAspirant": 1,
            "nameAspirant": self.data_factory.name(),
            "lastNameAspirant": self.data_factory.name(),
            "role": self.data_factory.name(),
            "date": '01-01-2020 16:00',
            "notes": self.data_factory.text()
        }

        headers = {'Content-Type': 'application/json'}

        sol_interview = self.client.post("/interview/company/1",
                                         data=json.dumps(data),
                                         headers=headers)

        self.assertEqual(sol_interview.status_code, 400)

    def test_get_interview_company(self):

        data = {
            "nameCompany": self.data_factory.name(),
            "idAspirant": 1,
            "nameAspirant": self.data_factory.name(),
            "lastNameAspirant": self.data_factory.name(),
            "role": self.data_factory.name(),
            "date": '01/01/2020 16:00',
            "notes": self.data_factory.text()
        }

        headers = {'Content-Type': 'application/json'}

        sol_interview = self.client.post("/interview/company/1",
                                         data=json.dumps(data),
                                         headers=headers)

        sol_interview = self.client.get("/interview/company/1",
                                        headers=headers)

        self.assertEqual(sol_interview.status_code, 200)

    def test_get_interview_company_fail(self):

        headers = {'Content-Type': 'application/json'}

        sol_interview = self.client.get("/interview/company/1",
                                        headers=headers)

        self.assertEqual(sol_interview.status_code, 404)

    def test_get_interview_aspirant(self):

        data = {
            "nameCompany": self.data_factory.name(),
            "idAspirant": 1,
            "nameAspirant": self.data_factory.name(),
            "lastNameAspirant": self.data_factory.name(),
            "role": self.data_factory.name(),
            "date": '01/01/2020 16:00',
            "notes": self.data_factory.text()
        }

        headers = {'Content-Type': 'application/json'}

        sol_interview = self.client.post("/interview/company/1",
                                         data=json.dumps(data),
                                         headers=headers)

        sol_interview = self.client.get("/interview/aspirant/1",
                                        headers=headers)

        self.assertEqual(sol_interview.status_code, 200)

    def test_get_interview_aspirant_fail(self):

        headers = {'Content-Type': 'application/json'}

        sol_interview = self.client.get("/interview/aspirant/1",
                                        headers=headers)

        self.assertEqual(sol_interview.status_code, 404)
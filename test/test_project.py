import json
from unittest import TestCase
from faker import Faker
from application import application as app
from src.models import db, Project, ProjectAspirant


class TestProject(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    def tearDown(self):
        projects = Project.query.all()
        for project in projects:
            db.session.delete(project)

        aspirants = ProjectAspirant.query.all()
        for aspirant in aspirants:
            db.session.delete(aspirant)

        db.session.commit()

    def test_ping_project(self):

        endpoint_ping = "/"
        headers = {'Content-Type': 'application/json'}

        sol_ping = self.client.get(endpoint_ping,
                                   headers=headers)

        self.assertEqual(sol_ping.status_code, 200)

    def test_fail_page(self):

        endpoint_usuario = "/project/fail"
        headers = {'Content-Type': 'application/json'}

        sol_logUser = self.client.get(endpoint_usuario,
                                      headers=headers)

        self.assertEqual(sol_logUser.status_code, 404)

    def test_create_project(self):

        data = {
            "nameProject": self.data_factory.name(),
            "startDate": '01/01/2020',
            "endDate": '01/01/2021',
            "description": self.data_factory.text(),
            "aspirants": self.data_factory.random_int()
        }

        headers = {'Content-Type': 'application/json'}

        sol_project = self.client.post("/project/1",
                                       data=json.dumps(data),
                                       headers=headers)

        self.assertEqual(sol_project.status_code, 201)

    def test_create_project_fail(self):

        data = {
            "nameProject": self.data_factory.name(),
            "startDate": '01-01-2020',
            "endDate": '01-01-2021',
            "description": self.data_factory.text()
        }

        headers = {'Content-Type': 'application/json'}

        sol_project = self.client.post("/project/1",
                                       data=json.dumps(data),
                                       headers=headers)

        self.assertEqual(sol_project.status_code, 400)

    def test_get_project(self):

        data = {
            "nameProject": self.data_factory.name(),
            "startDate": '01/01/2020',
            "endDate": '01/01/2021',
            "description": self.data_factory.text()
        }

        headers = {'Content-Type': 'application/json'}

        sol_project = self.client.post("/project/1",
                                       data=json.dumps(data),
                                       headers=headers)

        sol_project = self.client.get("/project/1",
                                      headers=headers)

        self.assertEqual(sol_project.status_code, 200)
        self.assertEqual(len(sol_project.json), 1)

    def test_get_project_fail(self):

        headers = {'Content-Type': 'application/json'}

        sol_project = self.client.get("/project/1",
                                      headers=headers)

        self.assertEqual(sol_project.status_code, 404)

    def test_post_aspirant_project(self):

        data = {
            "nameProject": self.data_factory.name(),
            "startDate": '01/01/2020',
            "endDate": '01/01/2021',
            "description": self.data_factory.text(),
            "aspirants": 1
        }

        headers = {'Content-Type': 'application/json'}

        sol_project = self.client.post("/project/1",
                                       data=json.dumps(data),
                                       headers=headers)

        data = {
            "idUser": 1,
            "name": self.data_factory.name(),
            "lastName": self.data_factory.name(),
            "role": self.data_factory.name(),
            "notes": self.data_factory.text()
        }

        sol_aspirant = self.client.post("/aspirant/1",
                                        data=json.dumps(data),
                                        headers=headers)

        self.assertEqual(sol_aspirant.status_code, 201)

    def test_post_aspirant_project_fail(self):

        data = {
            "idUser": 1,
            "name": self.data_factory.name(),
            "lastName": self.data_factory.name(),
            "role": self.data_factory.name(),
            "notes": self.data_factory.text()
        }

        headers = {'Content-Type': 'application/json'}

        sol_aspirant = self.client.post("/aspirant/1",
                                        data=json.dumps(data),
                                        headers=headers)

        self.assertEqual(sol_aspirant.status_code, 404)

    def test_post_aspirant_project_exist(self):

        data = {
            "nameProject": self.data_factory.name(),
            "startDate": '01/01/2020',
            "endDate": '01/01/2021',
            "description": self.data_factory.text(),
            "aspirants": 1
        }

        headers = {'Content-Type': 'application/json'}

        sol_project = self.client.post("/project/1",
                                       data=json.dumps(data),
                                       headers=headers)

        data = {
            "idUser": 1,
            "name": self.data_factory.name(),
            "lastName": self.data_factory.name(),
            "role": self.data_factory.name(),
            "notes": self.data_factory.text()
        }

        sol_aspirant = self.client.post("/aspirant/1",
                                        data=json.dumps(data),
                                        headers=headers)

        sol_aspirant = self.client.post("/aspirant/1",
                                        data=json.dumps(data),
                                        headers=headers)

        self.assertEqual(sol_aspirant.status_code, 400)

    def test_post_aspirant_project_max(self):
        data = {
            "nameProject": self.data_factory.name(),
            "startDate": '01/01/2020',
            "endDate": '01/01/2021',
            "description": self.data_factory.text(),
            "aspirants": 0
        }

        headers = {'Content-Type': 'application/json'}

        sol_project = self.client.post("/project/1",
                                       data=json.dumps(data),
                                       headers=headers)

        data = {
            "idUser": 1,
            "name": self.data_factory.name(),
            "lastName": self.data_factory.name(),
            "role": self.data_factory.name(),
            "notes": self.data_factory.text()
        }

        sol_aspirant = self.client.post("/aspirant/1",
                                        data=json.dumps(data),
                                        headers=headers)

        self.assertEqual(sol_aspirant.status_code, 400)

    def test_get_aspirant_project(self):

        data = {
            "nameProject": self.data_factory.name(),
            "startDate": '01/01/2020',
            "endDate": '01/01/2021',
            "description": self.data_factory.text(),
            "aspirants": 1
        }

        headers = {'Content-Type': 'application/json'}

        sol_project = self.client.post("/project/1",
                                       data=json.dumps(data),
                                       headers=headers)

        data = {
            "idUser": 1,
            "name": self.data_factory.name(),
            "lastName": self.data_factory.name(),
            "role": self.data_factory.name(),
            "notes": self.data_factory.text()
        }

        sol_aspirant = self.client.post("/aspirant/1",
                                        data=json.dumps(data),
                                        headers=headers)

        sol_aspirant = self.client.get("/aspirant/1",
                                       headers=headers)

        self.assertEqual(sol_aspirant.status_code, 200)
        self.assertEqual(len(sol_aspirant.json), 1)

    def test_get_aspirant_project_fail(self):

        headers = {'Content-Type': 'application/json'}

        sol_aspirant = self.client.get("/aspirant/2",
                                       headers=headers)

        self.assertEqual(sol_aspirant.status_code, 404)

from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idCompany = db.Column(db.Integer, nullable=False)
    nameProject = db.Column(db.String, nullable=False)
    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    aspirants = db.Column(db.Integer, default=0)
    description = db.Column(db.String)
    createdAt = db.Column(db.DateTime, default=datetime.now)


class ProjectAspirant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProject = db.Column(db.Integer, nullable=False)
    idUser = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String)
    lastName = db.Column(db.String)
    role = db.Column(db.String)
    notes = db.Column(db.String)
    createdAt = db.Column(db.DateTime, default=datetime.now)


class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idCompany = db.Column(db.Integer, nullable=False)
    nameCompany = db.Column(db.String, nullable=False)
    idAspirant = db.Column(db.Integer, nullable=False)
    nameAspirant = db.Column(db.String, nullable=False)
    lastNameAspirant = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.String)
    createdAt = db.Column(db.DateTime, default=datetime.now)


class InterviewResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idInterview = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)
    notes = db.Column(db.String)
    createdAt = db.Column(db.DateTime, default=datetime.now)


class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idAspirant = db.Column(db.Integer, nullable=False)
    performance = db.Column(db.Float, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.now)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idAspirant = db.Column(db.Integer, nullable=False)
    idCompany = db.Column(db.Integer, nullable=False)
    nameTest = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    result = db.Column(db.String, nullable=False)
    notes = db.Column(db.String)
    createdAt = db.Column(db.DateTime, default=datetime.now)


class ProjectSchema(SQLAlchemySchema):
    class Meta:
        model = Project
        load_instance = True

    id = fields.Integer()
    idUser = fields.Integer()
    createdAt = fields.DateTime()


class ProjectDetailShema(SQLAlchemySchema):
    class Meta:
        model = Project
        load_instance = True

    id = fields.Integer()
    nameProject = fields.String()
    startDate = fields.DateTime()
    endDate = fields.DateTime()
    aspirants = fields.Integer()
    description = fields.String()


class ProjectAspirantSchema(SQLAlchemySchema):

    class Meta:
        model = ProjectAspirant
        load_instance = True

    idProject = fields.Integer()
    idUser = fields.Integer()
    name = fields.String()
    lastName = fields.String()
    role = fields.String()
    notes = fields.String()


class InterviewAspirantSchema(SQLAlchemySchema):

    class Meta:
        model = Interview
        load_instance = True

    id = fields.Integer()
    idCompany = fields.Integer()
    nameCompany = fields.String()
    role = fields.String()
    date = fields.DateTime()
    notes = fields.String()


class InterviewCompanySchema(SQLAlchemySchema):

    class Meta:
        model = Interview
        load_instance = True

    id = fields.Integer()
    idAspirant = fields.Integer()
    nameAspirant = fields.String()
    lastNameAspirant = fields.String()
    role = fields.String()
    date = fields.DateTime()
    notes = fields.String()
    createdAt = fields.DateTime()


class InterviewResultSchema(SQLAlchemySchema):

    class Meta:
        model = InterviewResult
        load_instance = True

    idInterview = fields.Integer()
    result = fields.String()
    notes = fields.String()
    createdAt = fields.DateTime()


class TestSchema(SQLAlchemySchema):

    class Meta:
        model = Test
        load_instance = True

    id = fields.Integer()
    nameTest = fields.String()
    date = fields.DateTime()
    result = fields.String()
    notes = fields.String()

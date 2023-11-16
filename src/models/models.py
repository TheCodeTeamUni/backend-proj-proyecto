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

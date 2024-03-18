from init import db, ma
from marshmallow import fields

class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    contact_information = db.Column(db.String)

    appointments = db.relationship('Appointment', back_populates='patient')


class PatientSchema(ma.Schema):

    appointment = fields.List(fields.Nested('AppointmentSchema'))

    class Meta:
        fields = ('id', 'name', 'contact_information')

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)

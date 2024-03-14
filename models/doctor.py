from init import db, ma
from marshmallow import fields


class Doctor(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    contact_information = db.Column(db.String)
    specialty = db.Column(db.String)

    appointments = db.relationship('Appointment', back_populates='doctor')

    
class DoctorSchema(ma.Schema):

    appointment = fields.List(fields.Nested('AppointmentSchema'))

    class Meta:
        fields = ('id','name','contact_information','specialty')

doctor_schema = DoctorSchema()
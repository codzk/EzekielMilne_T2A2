# Import necessary modules
from init import db, ma
from marshmallow import fields

# Define Doctor model
class Doctor(db.Model):
    __tablename__ = "doctors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    contact_information = db.Column(db.String)
    specialty = db.Column(db.String(100))
    appointments = db.relationship('Appointment', back_populates='doctor')

# Define DoctorSchema for serialisation
class DoctorSchema(ma.Schema):
    appointment = fields.List(fields.Nested('AppointmentSchema'))

    class Meta:
        fields = ('id', 'name', 'contact_information', 'specialty')

# Initialize DoctorSchema instance
doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)

from init import db, ma
from marshmallow import fields
from models.user import User
from models.doctor import Doctor

class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='appointments')

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)

    doctor = db.relationship('Doctor', back_populates="appointments")




class AppointmentSchema(ma.Schema):
        
    user = fields.Nested("UserSchema", only = ['name','email'])

    doctor = fields.Nested("DoctorSchema", only = ['name','contact_information','specialty'] )

    class Meta:

        fields = ('id', 'name', 'date', 'reason', 'user', 'doctor')


appointment_schema = AppointmentSchema
appointments_schema = AppointmentSchema(many=True)


    
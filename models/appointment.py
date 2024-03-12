from sqlalchemy import DateTime
from init import db, ma
from marshmallow import fields

class Appointment(db.Model):
    __tablename__ = "appointment"

    appointmentid = db.Column(db.Integer, primary_key=True)
    appointmentname = db.Column(db.String)
    appointmentdate = db.Column(DateTime, nullable=False)
    appointmenttime = db.Column(DateTime, nullable=False)
    appointmenttype = db.Column(db.Integer, nullable=False)

    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patientid'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctorid'), nullable=False)
    user_id = db.Column(db. Integer, db.ForeignKey('user.id'),nullable=False)

    user_id = db.relationship('User', back_populates='appointment')
    patient_id = db.relationship('Patient', back_populates='appointment')
    doctor_id = db.relationship('Doctor', back_populates='appointment')
   

class AppointmentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only= ['name', 'email'])
    doctor = fields.Nested('DoctorSchema', only = ['firstname', 'lastname', 'specialty'])
    patient = fields.Nested('PatientSchema', only= ['fistname', 'lastname', 'contactinformation'])
    
    class Meta:
        fields = ('appointmentid', 'appointmentdate', 'appointmenttime', 'appointmenttype','user','doctor','patient')

appointment_schema = AppointmentSchema
appointments_schema = AppointmentSchema(many=True)    

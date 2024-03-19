# Import necessary modules
from init import db, ma
from marshmallow import fields

# Define Appointment model
class Appointment(db.Model):
    __tablename__ = "appointments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='appointments')
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    doctor = db.relationship('Doctor', back_populates="appointments")
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    patient = db.relationship('Patient', back_populates="appointments")
    billing_id = db.Column(db.Integer, db.ForeignKey('billings.id'), nullable=False)
    billing = db.relationship("Billing", back_populates="appointments")

# Define AppointmentSchema for serialisation
class AppointmentSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=['name', 'email'])
    doctor = fields.Nested("DoctorSchema", only=['name', 'contact_information', 'specialty'])
    patient = fields.Nested("PatientSchema", only=['name', 'contact_information'])
    billing = fields.Nested("BillingSchema", only=['id', 'amount_due', 'payment_status'])

    class Meta:
        fields = ('id', 'name', 'date', 'reason', 'user', 'doctor', 'patient', 'billing')

# Initialise AppointmentSchema instances
appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)

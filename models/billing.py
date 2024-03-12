from init import db, ma
from marshmallow import fields

class Billing(db.Model):
    __tablename__ = "billing"

    billingid = db.Column(db.Integer, primary_key=True)
    amountdue = db.Column(db.Integer, nullable=True)
    paymentstatus = db.Column(db.String)

    
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.appointmentid'), nullable=False)

    appointment = db.relationship('Appointment', back_populates= 'billing')


class BillingSchema(ma.Schema):
    
    appointment = fields.Nested('AppointmentSchema', only= ['amountdue','paymentstatus'] )

    class Meta: 
        fields = ('billingid', 'amountdue', 'paymentstatus', 'appointment')


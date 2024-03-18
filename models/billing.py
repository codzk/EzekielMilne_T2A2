from init import db, ma
from marshmallow import fields


class Billing(db.Model):
    __tablename__ = "billings"

    id = db.Column(db.Integer, primary_key=True)
    amount_due = db.Column(db.Integer)
    payment_status = db.Column(db.String(20), nullable=False)

    appointments = db.relationship('Appointment', back_populates='billing')


class BillingSchema(ma.Schema):
    appointment = fields.List(fields.Nested("AppointmentSchema"))

    class Meta:
        fields = ('id', 'amount_due', 'payment_status')


billing_schema = BillingSchema()

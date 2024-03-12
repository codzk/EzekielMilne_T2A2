
from init import db, ma

class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users'), nullable=False)

    user = db.relationship('User', back_populates='appointments')




    class AppointmentSchema(ma.Schema):
        
        user = fields.Nested("UserSchema", only = ['name', 'email'])

        class Meta:

            fields = ('id', 'date', 'reason', 'user')


    appointment_schema = AppointmentSchema
    appointments_schema = AppointmentSchema (many=True)


    
from init import db, ma
from marshmallow import fields

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=True)

    appointments = db.relationship('Appointment', back_populates='user')

class UserSchema(ma.Schema):

    appointment = fields.List(fields.Nested('AppointmentSchema'))
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')

    
user_schema = UserSchema(exclude=['password'])
# users_schema = UserSchema(exclude=['password'])




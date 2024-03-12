from init import db, ma

class Doctor(db.Model):
    __tablename__ = "doctor"

    doctorid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    contactinformation = db.Column(db.Integer, nullable=False)
    specialty = db.String(db.String)

    appointment = db.relationship('Appointment', back_populates='patient')

class DoctorSchema(ma.Schema):
    class Meta:
        fields = ('firstname', 'lastname', 'contactinformation', 'specialty')

    
doctor_schema = DoctorSchema()

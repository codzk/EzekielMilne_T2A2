from init import db, ma

class Patient(db.Model):
    __tablename__ = "patient"

    patientid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    secondname = db.Column(db.String)
    contactinformation = db.Column(db.Integer, nullable=False)

    appointment = db.relationship('Appointment', back_populates='patient')

   
class PatientSchema(ma.Schema):
    class Meta:
        fields = ('firstname', 'lastname', 'contactinformation')

    
patient_schema = PatientSchema()
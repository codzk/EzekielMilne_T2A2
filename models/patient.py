from init import db, ma

class Patient(db.Model):
    __tablename__ = "patient"

    patient_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    second_name = db.Column(db.String)
    contact_information = db.Column(db.Integer, nullable=False)

   


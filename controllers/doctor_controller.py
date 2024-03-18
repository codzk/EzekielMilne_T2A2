from flask import Blueprint

from init import db
from models.doctor import Doctor, doctors_schema, doctor_schema

doctors_bp = Blueprint('doctors', __name__, url_prefix='/doctors')

@doctors_bp.route('/')
def get_all_doctors():
    stmt = db.select(Doctor)
    doctors = db.session.scalars(stmt)
    return doctors_schema.dump(doctors)

@doctors_bp.route('/<int:doctor_id>')
def get_one_doctor(doctor_id):
    stmt = db.select(Doctor).filter_by(id=doctor_id)
    doctor = db.session.scalar(stmt)
    if doctor:
        return doctor_schema.dump(doctor)
    else:
        return {"error": f"doctor with id {doctor_id} not found"}, 404


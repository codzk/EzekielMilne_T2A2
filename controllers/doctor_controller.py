from flask import Blueprint

from init import db
from models.doctor import Doctor, doctor_schema

doctor_bp = Blueprint('doctors', __name__, url_prefix='/doctors')

@doctor_bp.route('/')
def get_all_doctors():
    stmt = db.select(Doctor).order_by(Doctor.date.desc())
    doctors = db.session.scalars(stmt)
    return doctor_schema.dump(doctors)
from flask import Blueprint

from init import db
from models.appointment import Appointment, appointments_schema

appointment_bp = Blueprint('appointments', __name__, url_prefix='/appointments')

@appointment_bp.route('/')
def get_all_appointments():
    stmt = db.select(Appointment).order_by(Appointment.date.desc())
    appointments = db.session.scalars(stmt)
    return appointments_schema.dump(appointments)


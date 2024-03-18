from flask import Blueprint

from init import db
from models.billing import Billing, billing_schema


billing_bp = Blueprint('billings', __name__, url_prefix='/billings')

@billing_bp.route('/')
def get_all_billings():
    stmt = db.select(Billing).order_by(Billing.date.desc())
    billings = db.session.scalars(stmt)
    return billing_schema.dump(billings)
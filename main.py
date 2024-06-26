import os


from flask import Flask
from marshmallow.exceptions import ValidationError
from init import db, ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False


    # configs
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URI")
    # integrate libraries into a Flask application.
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    # connect libraries with flask app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    @app.errorhandler(ValidationError)
    def validation_error(error):
        return {"error": error.messages}, 400

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)
    
    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.appointment_controller import appointments_bp
    app.register_blueprint(appointments_bp)

    from controllers.doctor_controller import doctors_bp
    app.register_blueprint(doctors_bp)

    from controllers.patient_controller import patients_bp
    app.register_blueprint(patients_bp)

    return app

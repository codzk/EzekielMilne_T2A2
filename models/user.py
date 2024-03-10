from init import db, ma

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'username', 'password', 'is_admin')

    
user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(exclude=['password'])




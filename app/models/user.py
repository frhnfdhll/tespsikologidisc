from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    jenis_kelamin = db.Column(db.String(50), nullable=False)
    umur = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(100), nullable=False, default="undraw_profile.svg")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    roles = db.Column(db.String(10), nullable=False, default="User")
    hasiltes = db.relationship('Hasiltes', backref='nama',lazy=True)

    def __repr__(self):
        return '{}'.format(self.id ,self.fullname, self.username, self.email, self.password, self.jenis_kelamin, self.umur, self.created_at, self.roles)

class Hasiltes(db.Model):
    id_hasil = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    most_D = db.Column(db.Integer, nullable=False)
    most_I = db.Column(db.Integer, nullable=False)
    most_S = db.Column(db.Integer, nullable=False)
    most_C = db.Column(db.Integer, nullable=False)
    least_D = db.Column(db.Integer, nullable=False)
    least_I = db.Column(db.Integer, nullable=False)
    least_S = db.Column(db.Integer, nullable=False)
    least_C = db.Column(db.Integer, nullable=False)
    change_D = db.Column(db.Integer, nullable=False)
    change_I = db.Column(db.Integer, nullable=False)
    change_S = db.Column(db.Integer, nullable=False)
    change_C = db.Column(db.Integer, nullable=False)
    hasil_tipekepribadian = db.Column(db.String(100), nullable=False)
    rekomendasi_pekerjaan = db.Column(db.Text, nullable=False)
    date_submit = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '{}'.format(self.id_hasil, self.most_D, self.most_I, self.most_S, self.most_C, self.least_D, self.least_I, self.least_S, self.least_C,self.change_D, self.change_I, self.change_S, self.change_C, self.hasil_tipekepribadian, self.hasil_tipekepribadian, self.rekomendasi_pekerjaan, self.date_submit)
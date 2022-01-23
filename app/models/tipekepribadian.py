from app import db

class graphic_Change(db.Model):
    id_soal = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    change_d = db.Column(db.Integer)
    change_i = db.Column(db.Integer)
    change_s = db.Column(db.Integer)
    change_c = db.Column(db.Integer)
    skor = db.Column(db.Float)
    bagian = db.Column(db.Integer)

    def __repr__(self):
        return '{}'.format(self.id_soal, self.skor, self.change_d, self.change_i, self.change_s, self.change_c, self.bagian)

class graphic_Most(db.Model):
    id_soal = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    most_d = db.Column(db.Integer)
    most_i = db.Column(db.Integer)
    most_s = db.Column(db.Integer)
    most_c = db.Column(db.Integer)
    skor = db.Column(db.Float)
    bagian = db.Column(db.Integer)

    def __repr__(self):
        return '{}'.format(self.id_soal, self.skor, self.most_d, self.most_i, self.most_s, self.most_c, self.bagian)

class graphic_Least(db.Model):
    id_soal = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    least_d = db.Column(db.Integer)
    least_i = db.Column(db.Integer)
    least_s = db.Column(db.Integer)
    least_c = db.Column(db.Integer)
    skor = db.Column(db.Float)
    bagian = db.Column(db.Integer)

    def __repr__(self):
        return '{}'.format(self.id_soal, self.skor, self.least_d, self.least_i, self.least_s, self.least_c, self.bagian)

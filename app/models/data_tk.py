from app import db

class data_tipekepribadian(db.Model):
    id_tipe = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    tipe_kepribadian = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.String(100000), nullable=False)
    ciri_umum = db.Column(db.String(1000), nullable=False)
    nilai_dalam_team = db.Column(db.String(1000), nullable=False)
    kemungkinan_kelemahan = db.Column(db.String(1000), nullable=False)
    ketakutan_terbesar = db.Column(db.String(1000), nullable=False)
    rekomendasi_pekerjaan = db.Column(db.String(100000), nullable=False)
    
    def __repr__(self):
        return '{}'.format(self.id_tipe, self.tipe_kepribadian, self.deskripsi)
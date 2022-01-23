from app import db

class Soal(db.Model):
    id_soal = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    pernyataan_a = db.Column(db.String(1000))
    pernyataan_b = db.Column(db.String(1000))
    pernyataan_c = db.Column(db.String(1000))
    pernyataan_d = db.Column(db.String(1000))
    m_a = db.Column(db.String(10), nullable=False)
    m_b = db.Column(db.String(10), nullable=False)
    m_c = db.Column(db.String(10), nullable=False)
    m_d = db.Column(db.String(10), nullable=False)
    l_a = db.Column(db.String(10), nullable=False)
    l_b = db.Column(db.String(10), nullable=False)
    l_c = db.Column(db.String(10), nullable=False)
    l_d = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '{}'.format(self.id_soal, self.pernyataan_a, self.pernyataan_b, self.pernyataan_c, self.pernyataan_d, self.m_a, self.m_b, self.m_c, self.m_d, self.l_a, self.l_b, self.l_c, self.l_d)


# class Hasiltes(db.Model):
#     id_hasiltes = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
#     most_d = db.Column(db.String(10), nullable=False)
#     most_i = db.Column(db.String(10), nullable=False)
#     most_s = db.Column(db.String(10), nullable=False)
#     most_c = db.Column(db.String(10), nullable=False)
#     least_d = db.Column(db.String(10), nullable=False)
#     least_i = db.Column(db.String(10), nullable=False)
#     least_s = db.Column(db.String(10), nullable=False)
#     least_c = db.Column(db.String(10), nullable=False)
#     change_d = db.Column(db.String(10), nullable=False)
#     change_i = db.Column(db.String(10), nullable=False)
#     change_s = db.Column(db.String(10), nullable=False)
#     change_c = db.Column(db.String(10), nullable=False)

#     def __repr__(self):
#         return '{}'.format(self.most_d, self.most_i, self.most_s, self.most_c, self.least_d, self.least_i, self.least_s, self.least_c, self.change_d, self.change_i, self.change_s, self.change_c)
    
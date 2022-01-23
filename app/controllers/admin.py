from app.models.user import Hasiltes, User

def hasiltes():
    hasiltes = Hasiltes.query.all()
    return hasiltes

def user():
    user = User.query.all()
    return user

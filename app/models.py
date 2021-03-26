from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(15))
    gender = db.Column(db.String(6))
    password = db.Column(db.String(200))

    def __repr__(self):
        return '<User id {}, name {}>'.format(self.id, self.name)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    price = db.Column(db.NUMERIC(10, 2))
    compare_price = db.Column(db.NUMERIC(10, 2))
    description = db.Column(db.Text)
    pictures = db.Column(db.Text)
    tags = db.Column(db.String(200))
    category = db.Column(db.String(200))
    added = db.Column(db.DateTime)

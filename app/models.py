from app import db

class Posts(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25))
    subject = db.Column(db.String(25))
    message = db.Column(db.String(100))

    def __repr__(self):
        return self.name
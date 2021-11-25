from app.routes import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return "<Task %r>" % self.name
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


DEFAULT_IMG = 'https://cdn-icons-png.flaticon.com/512/64/64431.png?w=740&t=st=1677678792~exp=1677679392~hmac=bf0a70d2000d3515bacb7cfdb4cabc475b5313a2a4ca8b40d200b49ac687de6d'


class Pet(db.Model):
    """Models pets in the system at the adoption agency"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default=DEFAULT_IMG)
    age = db.Column(db.Integer, nullable=True, default="unknown")
    notes = db.Column(db.Integer, nullable=True,
                      default="No notes for this pet.")
    available = db.Column(db.Boolean, nullable=False,
                          default="checked")

    def __repr__(self):
        p = self
        return f"<Pet {p.name} {p.species}>"

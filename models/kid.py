from db import db


class KidModel(db.Model):
    __tablename__ = "kids"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    sex = db.Column(db.String(10), unique=False, nullable=False)
    parents = db.Column(db.String(100), unique=False, nullable=False)
    birthdate = db.Column(db.Date, unique=False, nullable=False)

    #
    items = db.relationship(
        "ItemModel", back_populates="kid", lazy="dynamic", cascade="all, delete"
    )

    tags = db.relationship(
        "TagModel", back_populates="kid", lazy="dynamic", cascade="all, delete"
    )

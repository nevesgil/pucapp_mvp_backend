from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    kid_id = db.Column(
        db.Integer, db.ForeignKey("kids.id"), unique=False, nullable=False
    )
    kid = db.relationship("KidModel", back_populates="items")
    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")

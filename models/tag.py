from db import db

class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), unique=True, nullable=False)
    kid_id = db.Column(db.Integer(), db.ForeignKey("kids.id"), nullable=False)

    kid = db.relationship("KidModel", back_populates="tags")
    posts = db.relationship("PostModel", back_populates="tags", secondary="posts_tags")
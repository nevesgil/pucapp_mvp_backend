from db import db


class PostModel(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), unique=False, nullable=False)

    kid_id = db.Column(
        db.Integer, db.ForeignKey("kids.id"), unique=False, nullable=False
    )
    
    kid = db.relationship("KidModel", back_populates="posts")
    tags = db.relationship("TagModel", back_populates="posts", secondary="posts_tags")
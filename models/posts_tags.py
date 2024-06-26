from db import db


class PostsTags(db.Model):
    __tablename__ = "posts_tags"

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
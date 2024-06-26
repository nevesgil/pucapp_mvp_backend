import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import db
from models import KidModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from resources.schemas import KidSchema


blp = Blueprint("Kids", __name__, description="Operations on kids")


@blp.route("/kid/<string:kid_id>")
class Kid(MethodView):
    @blp.response(200, KidSchema)
    def get(self, kid_id):
        kid = KidModel.query.get_or_404(kid_id)
        return kid

    def delete(self, kid_id):
        kid = KidModel.query.get_or_404(kid_id)
        db.session.delete(kid)
        db.session.commit()
        return {"message": "DELETED"}


@blp.route("/kid")
class KidList(MethodView):
    @blp.response(201, KidSchema(many=True))
    def get(self):
        """
        Retrieve a List of All kids
        """
        return KidModel.query.with_entities(KidModel.id, KidModel.name).all()

    @blp.arguments(KidSchema)
    @blp.response(201, KidSchema)
    def post(self, kid_data):
        """
        Create a New kid
        """
        kid = KidModel(**kid_data)

        try:
            db.session.add(kid)
            db.session.commit()
        except IntegrityError:
            abort(400, message="There is already a kid with this name")
        except SQLAlchemyError:
            abort(500, message="Error inserting the kid")

        return kid, 201
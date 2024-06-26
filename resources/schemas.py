from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainKidSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    sex = fields.Str(required=True)
    parent = fields.Str(required=True)
    birthdate = fields.Date(required=True)


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    kid_id = fields.Int()


class ItemSchema(PlainItemSchema):
    kid_id = fields.Int(required=True, load_only=True)
    kid = fields.Nested(PlainKidSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class KidSchema(PlainKidSchema):
    items = fields.List(fields.Nested(PlainItemSchema(), dump_only=True))
    tags = fields.List(fields.Nested(PlainTagSchema(), dump_only=True))


class TagSchema(PlainTagSchema):
    kid_id = fields.Int(load_only=True)
    kid = fields.Nested(PlainKidSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)
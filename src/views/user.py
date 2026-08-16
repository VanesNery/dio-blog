
from src.app import ma
from src.views.role import RoleSchema
from marshmallow import fields

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "role")

    role = ma.Nested(RoleSchema, only=("id", "name"))


class CreateUserSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    role_id = fields.Integer(required=True, strict=True)

from src.app import ma

class RoleSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
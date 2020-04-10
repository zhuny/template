import marshmallow as ma


class BaseSchema(ma.Schema):
    class Meta:
        fields = "id", "created_at", "updated_at"


base_schema = BaseSchema()
basis_schema = BaseSchema(many=True)


from marshmallow import Schema, ValidationError, fields, validate


def validate_not_blank(value):
    if value is None or not value.strip():
        raise ValidationError('Field cannot be blank.')


class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    task_id = fields.Int(required=True)
    author = fields.Str(
        required=True,
        validate=[validate.Length(max=120), validate_not_blank],
    )
    content = fields.Str(
        required=True,
        validate=[validate.Length(max=1000), validate_not_blank],
    )
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(
        required=True,
        validate=[validate.Length(max=200), validate_not_blank],
    )
    description = fields.Str(validate=validate.Length(max=2000))
    status = fields.Str(validate=validate.OneOf(['pending', 'in-progress', 'completed']))
    priority = fields.Str(validate=validate.OneOf(['low', 'medium', 'high']))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

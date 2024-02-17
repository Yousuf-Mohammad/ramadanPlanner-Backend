from ninja import ModelSchema

from content.models import Content


class ContentOut(ModelSchema):
    class Config:
        model = Content
        model_fields = ["id", "title", "description", "type", "image"]

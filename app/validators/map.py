from pydantic import BaseModel, ValidationError, validator


class MapValidator(BaseModel):
    name: str
    latitude: float
    longitude: float
    zoom: int

    @validator('zoom')
    def zoom_level_must_be_greater_than_zero(cls, value):
        if value < 0:
            raise ValidationError('Zoom level cannot be less than zero!')
        return value

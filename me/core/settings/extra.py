from pydantic import BaseModel

class ExtraSettings(BaseModel):

    foo: str = "bar"

from pydantic import BaseModel, BaseSettings, Field, PostgresDsn, RedisDsn
from typing import List, Optional

class ExtraSettings(BaseModel):

    foo: str = "bar"

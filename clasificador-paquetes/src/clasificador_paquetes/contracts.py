
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class Entrada(BaseModel):
    #TODO
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )

    id_paquete: str = Field(min_length=1)
    peso_kg: float = Field(gt=0, le=30)
    distancia_km: float = Field(ge=0, le=200)


class Salida(BaseModel):
    #TODO
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )

    id_paquete: str = Field(min_length=1)
    categoria: Literal["normal", "urgente"]
    confianza: float = Field(ge=0, le=1)

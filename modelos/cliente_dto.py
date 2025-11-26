from pydantic import BaseModel, EmailStr, Field
class Cliente (BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre de la persona")
    apellido: str
    edad: int  
    id_Cliente: int
    direccion: str = Field(..., min_length=1, max_length=100, description="Nombre de la persona")
    
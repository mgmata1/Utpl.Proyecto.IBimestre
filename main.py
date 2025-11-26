"""
API REST básica con FastAPI
Este es un esqueleto de API para enseñar a estudiantes
"""

from fastapi import FastAPI,HTTPException
from modelos.persona_dto import Persona
from modelos.cliente_dto import Cliente

dbCliente=[]



# Crear la instancia de FastAPI
app = FastAPI(
    title="API de Ejemplo UTPL - mg@promox.ec",
    description="API REST básica para aprender FastAPI en Interoperabilidad de Sistemas",
    version="1.0.0"
)


@app.get("/")
def root():
    """
    Endpoint raíz - Hola Mundo
    """
    return {"mensaje": "¡Hola Mundo desde FastAPI!"}


@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    """
    Endpoint de ejemplo con parámetro de ruta
    """
    return {"mensaje": f"¡Hola {nombre}! Bienvenido a la API"}


@app.get("/info")
def informacion():
    """
    Endpoint de información de la API
    """
    return {
        "nombre": "API de Ejemplo UTPL",
        "version": "1.0.0",
        "descripcion": "Esta es una API básica creada con FastAPI para propósitos educativos"
    }

@app.post("/personas", response_model=Persona, tags=["Personas"])
def crear_persona(persona: Persona):
    """
    Endpoint para crear una nueva persona
    """
    return persona
    


@app.post("/clientes", response_model=Cliente, tags=["Clientes"])
def crear_clientes (cliente: Cliente):
    """
    Endpoint para crear un nuevo cliente
    """
    dbCliente.append(cliente)
    return cliente

    
@app.get("/cliente", response_model=list[Cliente], tags=["Clientes"])
def obtener_clientes():
    """
    Endpoint para crear un nuevo cliente
    """
    return dbCliente

@app.get("/cliente/{id}", response_model=Cliente, tags=["Clientes"])
def obtener_cliente_por_id (id: int):
    """Buscar un cliente por su id."""
    for cliente in dbCliente:
        if cliente.id == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrada")

@app.delete("/clientes/{id}", response_model=Cliente, tags=["Clientes"])
def eliminar_cliente(id: int):
    """Eliminar un cliente por su id.
    Retorna el cliente eliminada o 404 si no existe.
    """
    for idx, cliente in enumerate(dbCliente):
        if cliente.id == id:
            # Remover y retornar cliente eliminado
            return dbCliente.pop(idx)
    raise HTTPException(status_code=404, detail="Cliente no encontrada")
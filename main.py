import base64
from fastapi import  FastAPI
from pydantic import BaseModel

app = FastAPI()

class FileRoute(BaseModel):
    filename: str

@app.post("/")
def print_encoded(ruta: FileRoute):
    with open(ruta.filename, "rb") as file:
        content = file.read()
    content64 = base64.b64encode(content).decode("utf-8")
    return {
        "statusCode": 200,
        "message": "Successfully encoded file to base64",
        "encodedFile": content64
    }

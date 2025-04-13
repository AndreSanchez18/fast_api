from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ProductCreate(BaseModel):
    name : str
    price : int

products_db = [   #Contiene productos en formato JSON
    {"id":1,
     "name":"Arroz",
     "price":100},

    {"id":2,
     "name":"Fideo",
     "price":50},

    {"id":3,
     "name":"Monster",
     "price":200}
] 

@app.get("/products/")
def get_products():
    return products_db

@app.get("/products/{id}")
def get_product(id:int):

    product = list(filter(lambda x:x["id"] == id, products_db))

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@app.post("/products/")
def create_product(product : ProductCreate):
    new_id = max([p["id"] for p in products_db])+1
    new_product = {"id":new_id, "name":product.name, "price":product.price}
    products_db.append(new_product)
    return new_product
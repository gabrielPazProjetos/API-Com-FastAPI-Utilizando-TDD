from fastapi import APIRouter, HTTPException
from app.schemas import ProductSchema, ProductUpdateSchema
from app.database import db
from bson import ObjectId
from bson.errors import InvalidId
from datetime import datetime

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(product: ProductSchema):
    try:
        result = await db["products"].insert_one(product.dict())
        return {**product.dict(), "id": str(result.inserted_id)}
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao inserir produto")

@router.get("/products")
async def list_products():
    return await db["products"].find().to_list(100)

@router.get("/products/{id}")
async def get_product(id: str):
    try:
        product = await db["products"].find_one({"_id": ObjectId(id)})
        if not product:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        return product
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido")
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao consultar produto")

@router.put("/products/{id}")
async def update_product(id: str, update_data: ProductUpdateSchema):
    product = await db["products"].find_one({"_id": ObjectId(id)})
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    update_dict = update_data.dict(exclude_unset=True)
    update_dict["updated_at"] = update_dict.get("updated_at", datetime.utcnow())

    await db["products"].update_one({"_id": ObjectId(id)}, {"$set": update_dict})
    return {**product, **update_dict}

@router.delete("/products/{id}", status_code=204)
async def delete_product(id: str):
    product = await db["products"].find_one({"_id": ObjectId(id)})
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    await db["products"].delete_one({"_id": ObjectId(id)})

@router.get("/products/filter")
async def filter_products(min_price: float, max_price: float):
    query = {"price": {"$gt": min_price, "$lt": max_price}}
    return await db["products"].find(query).to_list(100)

from src.perfume.crud import create_perfume, get_perfume, get_page_of_perfumes, update_perfume, delete_perfume
from src.perfume.model import PerfumeInDB
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Perfume"])

@router.post("/", response_description="Add new perfume")
async def add_perfume(perfume: PerfumeInDB):
    return await create_perfume(perfume)

@router.get("/{perfume_id}", response_description="Get a perfume")
async def get_perfume_route(perfume_id: str):
    perfume = await get_perfume(perfume_id)
    if perfume:
        return perfume
    raise HTTPException(status_code=404, detail="Perfume not found")

@router.get("/", response_description="Get all perfumes")
async def get_perfumes(page: int = 0, page_size: int = 10):
    return await get_page_of_perfumes(page, page_size)

@router.put("/{perfume_id}", response_description="Update a perfume")
async def update_perfume_route(perfume_id: str, perfume: PerfumeInDB):
    return await update_perfume(perfume_id, perfume)

@router.delete("/{perfume_id}", response_description="Delete a perfume")
async def delete_perfume_route(perfume_id: str):
    return await delete_perfume(perfume_id)



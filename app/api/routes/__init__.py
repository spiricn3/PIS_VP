from fastapi import APIRouter

from api.routes.vozilo import router as vozila_router
from api.routes.vozac import router as vozaci_router
from api.routes.radni_nalog import router as radni_nalozi_router

api_router = APIRouter(prefix="/api")


api_router.include_router(vozila_router, prefix="/vozila", tags=["Vozila"])
api_router.include_router(vozaci_router, prefix="/vozaci", tags=["Vozaci"])
api_router.include_router(radni_nalozi_router, prefix="/radni-nalozi", tags=["Radni Nalozi"])
import uuid


from fastapi import APIRouter, Security, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


from backend.film.dao import FilmDAO
from backend.film.models import Film
from backend.film.schemas import FilmSchemasCreate, FilmSchemasResponse

from backend.exceptions import BadRequest, NotFound

router = APIRouter(prefix="/contractor", tags=["Контрагенты"])


@router.get("/getContractors")
async def get_contractors() -> list[FilmSchemasResponse]:
    films: list[FilmSchemasResponse] = await FilmDAO.get_items()
    return JSONResponse(content=jsonable_encoder({"films": films}), status_code=200)






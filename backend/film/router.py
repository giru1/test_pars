import uuid
from pprint import pprint

from fastapi import APIRouter, Security, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


from .dao import FilmDAO
from .models import Film
from .schemas import FilmSchemasCreate, FilmSchemasResponse
from .utils import parse_films

from exceptions import BadRequest, NotFound

router = APIRouter(prefix="/contractor", tags=["Контрагенты"])


@router.post("/load_films")
async def load_films():
    films = await parse_films()
    print(7777777777777777777)
    # pprint(films)
    # for film in films:
    #     await FilmDAO.add(film)
    return JSONResponse(content={"message": "Films loaded successfully"}, status_code=200)


@router.get("/films")
async def get_contractors() -> list[FilmSchemasResponse]:
    films: list[FilmSchemasResponse] = await FilmDAO.get_items()
    return JSONResponse(content=jsonable_encoder({"films": films}), status_code=200)






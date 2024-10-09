from typing import Optional

from backend.film.models import Film
from backend.film.schemas import FilmSchemasCreate, FilmSchemasResponse

from backend.dao.base import BaseDAO


class FilmDAO(BaseDAO):
    model = Film

    @classmethod
    async def get_items(cls, filter_by: dict = {}) -> list[FilmSchemasResponse]:
        films: list[FilmSchemasResponse] = await cls.get_all(filter_by)
        return [FilmSchemasCreate(**film.__dict__) for film in films]

    @classmethod
    async def add_item(cls, data: dict = {}) -> Optional[FilmSchemasCreate]:
        film: FilmSchemasResponse = await cls.add(data)

        return FilmSchemasResponse(**film.__dict__) if film is not None else None

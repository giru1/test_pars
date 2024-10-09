from uuid import UUID
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_serializer
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel,
        from_attributes=True,
        arbitrary_types_allowed=True
    )

    @field_serializer(
        "id", "store_id", "owner_id", "cash_shift_id", "reason_id", "workplace_id", "organization_id",
        check_fields=False
    )
    def uuid_to_str(uuid: UUID):
        return str(uuid) if uuid else None


class FilmSchemasCreate(BaseSchema):
    name: str | None = Field(default=None, title="Film Name")
    producer: str | None = Field(default=None, title="Producer film")
    year: str | None = Field(default=None, title="Year film")
    genre: str | None = Field(default=None, title="Genre film")
    rating: str | None = Field(default=None, title="Rating film")


class FilmSchemasResponse(FilmSchemasCreate):
    id: UUID

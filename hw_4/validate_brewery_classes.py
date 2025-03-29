from uuid import UUID
from typing import Literal, Optional

from pydantic import BaseModel, RootModel, HttpUrl, constr


class SingleBreweryResponse(BaseModel):
    id: UUID
    name: str
    brewery_type: Literal[
        'micro', 'nano', 'regional', 'brewpub',
        'large', 'planning', 'bar', 'contract',
        'proprietor', 'closed']
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: Optional[str]
    state_province: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    longitude: Optional[constr(pattern=r'^-?\d{1,3}\.\d*$')]
    latitude: Optional[constr(pattern=r'^-?\d{1,3}\.\d*$')]
    phone: Optional[constr(pattern=r'^\d*-?\d?*-?\d?*$')]
    website_url: Optional[HttpUrl]
    state: Optional[str]
    street: Optional[str]


class BreweriesResponse(RootModel):
    root: list[SingleBreweryResponse]

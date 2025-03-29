from pydantic import BaseModel, HttpUrl


class AllBreedsListResponse(BaseModel):
    message: dict
    status: str


class SubbreedsListResponse(BaseModel):
    message: list
    status: str


class RandomImageDogResponse(BaseModel):
    message: HttpUrl
    status: str


class ImagesListResponse(BaseModel):
    message: list[HttpUrl]
    status: str


class MultiRandomImagesAllDogsResponse(BaseModel):
    message: list[HttpUrl] | HttpUrl
    status: str


class MultiRandomImagesDogsBreedSubbreedResponse(BaseModel):
    message: list[HttpUrl] | HttpUrl
    status: str

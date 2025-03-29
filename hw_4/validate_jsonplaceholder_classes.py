from pydantic import BaseModel, RootModel


class SinglePostResponse(BaseModel):
    id: int
    title: str
    body: str
    userId: int


class AllPostsResponse(RootModel):
    root: list[SinglePostResponse]

from fastapi import FastAPI
from config import settings
from api.router import api_router


app = FastAPI(
    title=settings.title,
    version=settings.version,
    description=settings.description,
    root_path=settings.openapi_prefix,
    docs_url=settings.docs_url,
    openapi_url=settings.openapi_url,
)

app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/")
async def root():
    return {"app": "Trip Planner"}

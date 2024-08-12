import uvicorn

from collection_service import collection_app as app, collection_host, collection_port


@app.get("/")
async def root():
    return {"message": "Hello from collection service"}


def start():
    uvicorn.run(
        "collection_service.main:app",
        host=collection_host,
        port=collection_port,
        reload=True,
    )

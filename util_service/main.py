import uvicorn

from util_service import collection_util_app as app, collection_util_host, collection_util_port


@app.get("/")
async def root():
    return {"message": "Hello from util service"}


def start():
    uvicorn.run(
        "util_service.main:app",
        host=collection_util_host,
        port=collection_util_port,
        reload=True
    )

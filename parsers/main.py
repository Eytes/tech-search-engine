from fastapi import FastAPI
from parsers.mvideo import router as mvideo_router


app = FastAPI()
app.include_router(mvideo_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", port=8080, workers=4)

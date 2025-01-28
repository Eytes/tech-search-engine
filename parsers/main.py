from fastapi import FastAPI
from parsers.mvideo import router as mvideo_router


app = FastAPI()
app.include_router(mvideo_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="127.0.0.1", port=8080, reload=True)

from fastapi import FastAPI


app = FastAPI()


@app.get(path="/")
async def index():
    return {"status": True}

from fastapi import FastAPI

app = FastAPI()


# should be available at http://127.0.0.1:8000/ and http://localhost:8000/
@app.get("/")
async def root():
    return {"message": "Congrats! You did it. You reached FastAPI. Try adding /docs at the end"}
from fastapi import FastAPI

app = FastAPI(
    title="API de Filmes",
)


@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Filmes!"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "demo-back",
        "environment": "dev",
        "version": "0.1.0"
    }

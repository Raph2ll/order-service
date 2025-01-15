from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    """
    Healthy check to see if the application is working in a basic way
    """
    return {"status": "healthy"}

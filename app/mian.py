from fastapi import FastAPI

from app.api.simulation import router as simulation_router


app = FastAPI(
    title="VAYU 2.0",
    description="AI-powered aerospace simulation platform",
    version="0.1.0",
)


app.include_router(
    simulation_router,
    prefix="/api",
)


@app.get("/")
def root():
    return {
        "project": "VAYU 2.0",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

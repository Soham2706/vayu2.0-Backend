from fastapi import APIRouter

from app.simulation.manager import simulation_manager


router = APIRouter(
    prefix="/simulation",
    tags=["Simulation"],
)


@router.post("/connect")
async def connect_simulation():
    connected = await simulation_manager.connect()

    return {
        "connected": connected,
        "vehicle": "gz_x500",
    }


@router.get("/status")
async def simulation_status():
    return await simulation_manager.get_status()

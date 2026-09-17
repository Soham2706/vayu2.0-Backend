from app.simulation.mavlink import MAVLinkConnector


class SimulationManager:
    def __init__(self):
        self.mavlink = MAVLinkConnector()
        self.initialized = False

    async def connect(self) -> bool:
        connected = await self.mavlink.connect()

        if connected:
            self.initialized = True

        return connected

    async def get_status(self):
        health = await self.mavlink.get_health()

        return {
            "connected": self.mavlink.connected,
            "initialized": self.initialized,
            "vehicle": "gz_x500",
            "health": health,
        }


simulation_manager = SimulationManager()

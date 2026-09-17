import asyncio

from mavsdk import System


class MAVLinkConnector:
    def __init__(self, connection_url: str = "udp://:14540"):
        self.connection_url = connection_url
        self.drone = System()
        self.connected = False

    async def connect(self, timeout: float = 10.0) -> bool:
        await self.drone.connect(
            system_address=self.connection_url
        )

        async def wait_for_connection():
            async for state in self.drone.core.connection_state():
                if state.is_connected:
                    return True
            return False

        try:
            result = await asyncio.wait_for(
                wait_for_connection(),
                timeout=timeout,
            )

            self.connected = result
            return result

        except asyncio.TimeoutError:
            self.connected = False
            return False

    async def get_health(self):
        if not self.connected:
            return None

        async for health in self.drone.telemetry.health():
            return {
                "global_position_ok": health.is_global_position_ok,
                "home_position_ok": health.is_home_position_ok,
                "accelerometer_ok": health.is_accelerometer_calibration_ok,
                "gyrometer_ok": health.is_gyrometer_calibration_ok,
                "magnetometer_ok": health.is_magnetometer_calibration_ok,
            }

        return None

from flojoy import DataContainer, flojoy, SerialDevice
from flojoy.connection_manager import DeviceConnectionManager
from typing import Optional
from TauLidarCamera.camera import Camera
from TauLidarCommon.color import ColorMode


@flojoy(deps={"taulidarcamera": "0.0.5"})
def OPEN_TAU_LIDAR(
    device: SerialDevice,
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    camera = Camera.open()
    camera.setModulationChannel(0)
    camera.setIntegrationTime3d(0, 1000)
    camera.setMinimalAmplitude(0, 10)
    Camera.setColorMode(ColorMode.DISTANCE)  ## use distance for point color
    Camera.setRange(0, 6000)
    DeviceConnectionManager.register_connection(device, camera)

    return None

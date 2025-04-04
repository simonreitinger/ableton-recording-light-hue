import os

from dotenv import load_dotenv
from python_hue_v2 import Hue
from python_hue_v2.light import Light

load_dotenv()


def get_hue_bridge_config() -> tuple[str, str, str]:
    return (
        os.getenv("HUE_IP", ""),
        os.getenv("HUE_APP_KEY", ""),
        os.getenv("HUE_LIGHT_ID", ""),
    )

def set_recording_light(is_recording: bool) -> None:
    ip, app_key, light_id = get_hue_bridge_config()
    hue = Hue(ip, app_key)

    light = Light(hue.bridge, light_id)

    if is_recording:
        light.color_xy = {"x": 0.66, "y": 0.305}
        light.brightness = 20.0
        light.on = True
    else:
        light.color_xy = {"x": 0.31, "y": 0.33}
        light.brightness = 20.0
        light.on = True

import os
import time

from python_hue_v2 import BridgeFinder, Hue
from hue import get_hue_bridge_config
from dotenv import load_dotenv

load_dotenv()

def get_env_file():
    return ".env"

def initialize_hue_bridge_config():
    if not os.getenv("HUE_APP_KEY"):
        # config not set up yet, initialize it
        finder = BridgeFinder()
        time.sleep(2)
        hostname = finder.get_bridge_server_lists()[0]
        addresses = finder.get_bridge_addresses()
        ip = addresses[0]

        hue = Hue(hostname)
        input("Press the button on the hue bridge to proceed. Then press enter here:")
        app_key = hue.bridge.connect() # press the button on the hue bridge

        print(f"Got app key ({app_key})")

    ip, app_key, light_id = get_hue_bridge_config()
    hue = Hue(ip, app_key)

    print("The following rooms are available:")
    valid_options = {}
    for i, item in enumerate(hue.bridge.get_lights()):
        meta = item["metadata"]
        print(f"""{i}) {meta["name"]} ({meta["archetype"]})""")
        valid_options[i] = (item["id"], item["metadata"]["name"])

    selection = -1
    while selection not in valid_options.keys():
        try:
            selection = int(input("Enter a valid number to set the correct light: "))
        except ValueError:
            pass

    room_id = valid_options[selection][0]

    env_file_name = get_env_file()
    with open(env_file_name, "wb") as env_file:
        env_file.writelines([
            f"HUE_IP={ip}\n".encode(),
            f"HUE_APP_KEY={app_key}\n".encode(),
            f"HUE_LIGHT_ID={room_id}\n".encode(),
        ])

    print(f"If you want to repeat the full setup, delete the {env_file_name} file.")

if __name__ == "__main__":
    initialize_hue_bridge_config()

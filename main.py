import argparse
import time

from client import AbletonOSCClient
from hue import set_recording_light


def get_client(hostname, port):
    return AbletonOSCClient(hostname, port)


def main(args):
    client = get_client(args.hostname, args.port)
    is_recording = client.query("/live/song/get/record_mode")[0]

    print("Polling for recording events...")

    while True:
        try:
            is_recording_new = client.query("/live/song/get/record_mode")[0]

            is_recording_changed = is_recording != is_recording_new
            is_recording = is_recording_new

            if is_recording_changed:
                set_recording_light(is_recording)
                time.sleep(0.5)

        except KeyboardInterrupt:
            break
        except:
            continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Client for AbletonOSC")
    parser.add_argument("--hostname", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=str, default=11000)
    args = parser.parse_args()
    main(args)

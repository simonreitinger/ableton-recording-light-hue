# ableton-recording-light-hue

Python application to indicate recording mode with Philips Hue.

### Requirements
- uv [see here](https://docs.astral.sh/uv/)
- AbletonOSC [installation guide](https://github.com/ideoforms/AbletonOSC)

### Installation / Setup

Clone repository, then:

```shell
uv sync
```

With this setup script you have to press the button on the hue bridge and select a specific light to control later on. The script can be run again to change the light.
```shell
uv run init_hue.py
```

Then run the script to poll for OSC messages:

```shell
uv run main.py
```

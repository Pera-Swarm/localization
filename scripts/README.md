# Localization Scripts

Main OpenCV + MQTT localization pipeline and support scripts.

## Setup

Use the shared root .venv and the global requirements.txt:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r ..\requirements.txt
```

## Configuration

If you run `../run.sh`, missing configs are auto-created from samples on first run.
If you run `python script.py` directly, copy the sample configs before running:

- config-mapping_sample.yaml -> config-mapping.yaml
- config-mqtt_sample.yaml -> config-mqtt.yaml

## Run

Main localization pipeline:

```powershell
python script.py
```

Raspberry Pi camera demo (Raspberry Pi OS only):

```powershell
python pycamera.py
```

## Outputs

- No files are written by default. Results are shown in the OpenCV window and published to MQTT topics.

## OS notes

- pycamera.py requires the Raspberry Pi camera stack and the picamera package.

## Troubleshooting

- cv2.aruco missing: install opencv-contrib-python.
- Camera not opening: change camera index in script.py.
- MQTT errors: verify broker settings in config-mqtt.yaml.

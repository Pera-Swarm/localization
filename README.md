# Swarm Robotics Localization

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Python tooling for ArUco-based localization, marker generation, and camera calibration.

## Project structure

- markers/ - Generate ArUco marker PNGs and a PDF.
- scripts/ - Main localization pipeline (OpenCV + MQTT) and supporting tools.
- scripts/board/ - Camera calibration workflow.
- scripts/previousScripts/ - Legacy demos and prototypes.
- docs/ - External documentation entry point.

## Shared virtual environment

This repo uses a shared root .venv and a single global requirements.txt.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

If you run `./run.sh` (Unix-like shells), missing configs are auto-created from samples on first run.
If you run `python scripts/script.py` directly, copy the sample configs in scripts/ first:

- scripts/config-mapping_sample.yaml -> scripts/config-mapping.yaml
- scripts/config-mqtt_sample.yaml -> scripts/config-mqtt.yaml

## Entry points

Markers:

```powershell
cd markers
python marker_generator.py
```

Localization pipeline:

```powershell
cd scripts
python script.py
```

Calibration:

```powershell
cd scripts/board
python calibrate.py
```

Legacy demos:

```powershell
cd scripts/previousScripts
python script2.py
```

## Outputs

- markers/generated/ - PNG marker images
- markers/aruco_markers.pdf - Generated marker PDF
- scripts/board/calibration_data.txt - Saved calibration data

## Troubleshooting

- cv2.aruco missing: install opencv-contrib-python (not opencv-python only).
- MyPy import-untyped: reportlab has no type hints; ignore or add a stub package.
- Camera not opening: try a different camera index in scripts/script.py.
- MQTT connection errors: verify scripts/config-mqtt.yaml values and broker reachability.

## Notes

- run.sh is a convenience script for Unix-like shells. On Windows, use the commands above.
- Raspberry Pi camera script is documented in scripts/README.md.

## Read more

- [ar-markers](https://pypi.org/project/ar-markers/)
- [Augmented Reality using ArUco Markers in OpenCV](https://www.learnopencv.com/augmented-reality-using-aruco-markers-in-opencv-c-python/)
- [OpenCV ArUco detection](https://docs.opencv.org/master/d5/dae/tutorial_aruco_detection.html)
- [OpenCV ArUco board detection](https://docs.opencv.org/master/db/da9/tutorial_aruco_board_detection.html)

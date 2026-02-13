# Markers

Generate ArUco marker PNGs and a PDF sheet.

## Setup

Use the shared root .venv and the global requirements.txt:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r ..\requirements.txt
```

## Run

```powershell
python marker_generator.py
```

## Outputs

- generated/ - Marker PNG files
- aruco_markers.pdf - PDF sheet

## Troubleshooting

- cv2.aruco missing: install opencv-contrib-python.
- reportlab import warnings: ignore MyPy import-untyped warnings or add stubs.

# Camera Calibration

Calibrate the camera from chessboard images and write calibration_data.txt.

## Setup

Use the shared root .venv and the global requirements.txt:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r ..\..\requirements.txt
```

## Inputs

- sample/\*.jpg - Chessboard images (7x6 corners) for calibration.

## Run

```powershell
python calibrate.py
```

## Outputs

- calibration_data.txt - Camera matrix and distortion coefficients.

## Troubleshooting

- No corners detected: ensure the chessboard has 7x6 inner corners and good lighting.
- cv2 missing: install opencv-contrib-python.

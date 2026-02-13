# Legacy Scripts

Historical demos and prototypes. These are kept for reference but still runnable.

## Setup

Use the shared root .venv and the global requirements.txt:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r ..\..\requirements.txt
```

## Run

```powershell
python script1.py
python script2.py
python script3.py
python script4.py
```

## Notes

- script1.py uses the ar-markers package and a webcam.
- script3.py expects calibration data at ../board/calibration_data.txt.

## Troubleshooting

- cv2.aruco missing: install opencv-contrib-python.
- ar_markers import errors: install ar-markers.

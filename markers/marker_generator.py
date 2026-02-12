# This is the updated version of the aruco marker generater.
# Using this you can generate pdf at once

import cv2 as cv
import os
from reportlab.platypus import SimpleDocTemplate, Image, Table  # type: ignore
from reportlab.lib import colors  # type: ignore
from reportlab.lib.pagesizes import A4  # type: ignore
from reportlab.lib.units import mm  # type: ignore

# Output PDF file
pdf_path = "aruco_markers.pdf"

# Create temporary folder for images
temp_dir = "./generated"
os.makedirs(temp_dir, exist_ok=True)

# Load predefined dictionary
dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)

# Marker settings
markers = list(range(0, 10))
image_size = 600

# Generate marker images
image_paths = []
for marker_id in markers:
    marker_image = cv.aruco.generateImageMarker(
        dictionary,
        marker_id,
        image_size
    )

    path = os.path.join(temp_dir, f"marker{marker_id}.png")
    cv.imwrite(path, marker_image)
    image_paths.append(path)

print("Markers generated.")

# Create PDF
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
elements = []

# Prepare images in grid (2 columns)
table_data = []
row = []

for i, img_path in enumerate(image_paths):
    img = Image(img_path, width=70*mm, height=70*mm)
    row.append(img)

    if len(row) == 2:
        table_data.append(row)
        row = []

# Add remaining images if odd count
if row:
    table_data.append(row)

table = Table(table_data)
table.setStyle([
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER')
])

elements.append(table)
doc.build(elements)

print(f"PDF created successfully: {pdf_path}")

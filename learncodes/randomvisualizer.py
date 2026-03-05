import os
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

IMAGE_DIR = "train/images"
LABEL_DIR = "train/labels"

# Rastgele image seçip polygonları çiz
def inspect_image(img_path, label_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, _ = img.shape

    with open(label_path, "r") as f:
        lines = f.readlines()

    print(f"Inspecting: {os.path.basename(img_path)} - {len(lines)} polygons")

    for line in lines:
        parts = line.strip().split()
        cls = int(parts[0])
        coords = list(map(float, parts[1:]))

        polygon = []
        for i in range(0, len(coords), 2):
            x = int(coords[i] * w)
            y = int(coords[i+1] * h)
            polygon.append((x, y))
        polygon = np.array(polygon, dtype=np.int32)

        # Polygon çiz
        cv2.polylines(img, [polygon], isClosed=True, color=(255,0,0), thickness=2)
        # Class etiketi
        x, y = polygon[0][0], polygon[0][1]
        cv2.putText(img, f"class {cls}", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)

        # Polygon alanı
        area = cv2.contourArea(polygon)
        print(f"  Class {cls} polygon area: {area:.1f} px^2")

    plt.figure(figsize=(8,8))
    plt.imshow(img)
    plt.axis("off")
    plt.show()

# Dataset files
files = os.listdir(IMAGE_DIR)
files = [f for f in files if f.endswith(".jpg")]

# Rastgele 5 image inspect et
for _ in range(5):
    file = random.choice(files)
    img_path = os.path.join(IMAGE_DIR, file)
    label_path = os.path.join(LABEL_DIR, file.replace(".jpg", ".txt"))
    if os.path.exists(label_path):
        inspect_image(img_path, label_path)
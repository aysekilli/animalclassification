import os
import cv2
import matplotlib.pyplot as plt
import numpy as np


image_dir = "data/train/images"
label_dir = "data/train/labels"

def draw_polygons(image_path, label_path):

    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h, w, _ = img.shape

    with open(label_path, "r") as f:
        lines = f.readlines()

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
        
        cv2.polylines(
            img,
            [polygon],
            isClosed=True,
            color=(255,0,0),
            thickness=2
        )

        x, y = polygon[0][0], polygon[0][1]
         
        cv2.putText(
            img,
            f"class {cls}",
            (x,y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255,0,0),
            1
        )

    plt.imshow(img)
    plt.axis("off")
    plt.show()


import numpy as np

files = os.listdir(image_dir)

for file in files[:5]:

    img_path = os.path.join(image_dir, file)
    label_path = os.path.join(label_dir, file.replace(".jpg", ".txt"))

    if os.path.exists(label_path):
        draw_polygons(img_path, label_path)
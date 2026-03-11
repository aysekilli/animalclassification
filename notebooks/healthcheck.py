import os
import cv2
from collections import Counter

image_folder = "./data/train/images"
label_folder = "./data/train/labels"

total_images = 0
rgb_images = 0
grayscale_images = 0
missing_labels = 0
empty_labels = 0
broken_polygons = 0

class_counter = Counter()

for image_name in os.listdir(image_folder):

    if not image_name.endswith((".jpg",".png",".jpeg")):
        continue

    total_images += 1

    image_path = os.path.join(image_folder, image_name)
    label_path = os.path.join(label_folder, image_name.rsplit(".",1)[0] + ".txt")

    # image kontrol
    img = cv2.imread(image_path)

    if len(img.shape) == 2:
        grayscale_images += 1
    else:
        rgb_images += 1

    # label kontrol
    if not os.path.exists(label_path):
        missing_labels += 1
        continue

    with open(label_path) as f:
        lines = f.readlines()

    if len(lines) == 0:
        empty_labels += 1
        continue

    for line in lines:

        parts = line.strip().split()

        class_id = parts[0]
        coords = parts[1:]

        class_counter[class_id] += 1

        # polygon kontrol
        if len(coords) < 6:
            broken_polygons += 1

        if len(coords) % 2 != 0:
            broken_polygons += 1

print("----- DATASET REPORT -----")

print("Total images:", total_images)
print("RGB images:", rgb_images)
print("Grayscale images:", grayscale_images)

print("Missing labels:", missing_labels)
print("Empty labels:", empty_labels)

print("Broken polygons:", broken_polygons)

print("\nClass distribution:")

for k,v in class_counter.items():
    print("Class",k,":",v)
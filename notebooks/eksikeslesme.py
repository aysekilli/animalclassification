import os

img_dir = "train/images/"
lbl_dir = "train/labels/"

missing = []
for f in os.listdir(img_dir):
    if f.endswith(".jpg"):
        txt = f.replace(".jpg", ".txt")
        if not os.path.exists(os.path.join(lbl_dir, txt)):
            missing.append(f)

print(f"Eksik .txt sayısı: {len(missing)}")
for f in missing:
    print(f)
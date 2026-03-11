import os
img_dir = "train/images/"
lbl_dir = "train/labels/"

empty = []
for f in os.listdir(lbl_dir):
    if f.endswith(".txt"):
        if os.path.getsize(os.path.join(lbl_dir, f)) == 0:
            empty.append(f)

print(f"Boş .txt sayısı: {len(empty)}")
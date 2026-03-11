import os

# Normalizemi kontrol eder
#

img_dir = "/data/train/images/"
lbl_dir = "/data/train/labels/"

errors = []
for f in os.listdir(lbl_dir):
    if f.endswith(".txt"):
        with open(os.path.join(lbl_dir, f)) as file:
            for i, line in enumerate(file):
                parts = line.strip().split()
                try:
                    vals = [float(x) for x in parts[1:]]  # class'ı atla
                    if any(v < 0 or v > 1 for v in vals):
                        errors.append(f"{f} - satır {i+1}: değer 0-1 dışında")
                except:
                    errors.append(f"{f} - satır {i+1}: format hatası")

print(f"Hatalı satır sayısı: {len(errors)}")
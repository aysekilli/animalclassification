🐄 Animal Classification and Segmentation
YOLO11-based 'instance segmentation' model trained to detect and segment farm animals(cow,sheep,horse,pig) in images.

#Overview
This project uses [Ultralytics YOLO11](https://github.com/ultralytics/ultralytics) to perform instance segmentation on farm animals. 
Model can identify and draw outlines around each animal in an image.

Supported classes:
- 🐄 COW
- 🐴 Horse
- 🐷 Pig
- 🐑 Sheep
-  Undefined

# Dataset

- **Source:** [Roboflow Universe - CV Project](https://universe.roboflow.com/cvproject-d8hm5/cv-project-4-c/dataset/3)
- **License:** CC BY 4.0
- **Format:** YOLO segmentation (polygon masks)
- **Split:**
  - Train: 4,867 images
  - Validation: 1,195 images
  - Test: available

# Results
Trained for 50 epochs on an NVIDIA RTX 4070 Laptop GPU (~1 hour).
| Class | mAP50 (Box) | mAP50 (Mask) |
|-------|-------------|--------------|
| COW | 0.986 | 0.987 |
| Horse | 0.964 | 0.964 |
| Pig | 0.993 | 0.989 |
| Sheep | 0.858 | 0.850 |
| **All** | **0.761** | **0.759** |

#  Model

- **Architecture:** YOLO11n-seg
- **Parameters:** 2.8M
- **Input size:** 640x640
- **Best weights:** `runs/segment/train3/weights/best.pt`

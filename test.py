from ultralytics import YOLO

model = YOLO("runs/segment/train3/weights/best.pt")
results = model.predict(source="test/images", save=True, conf=0.5)
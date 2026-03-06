from ultralytics import YOLO

model = YOLO("yolo11n-seg.pt")

model.train(
    data="C:/Users/ashe/Desktop/firstdataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    device=0
)
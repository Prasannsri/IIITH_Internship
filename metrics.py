from ultralytics import YOLO

# Load segmentation model
model = YOLO("yolov8n-seg.pt")

# Run validation safely
metrics = model.val(
    data="coco128.yaml",   # keep this
    imgsz=320,             # smaller size (avoids crash)
    device="cpu"
)

print(metrics)
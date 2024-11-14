from ultralytics import YOLO

model = YOLO("/home/vikram/Downloads/PALLET/runs/runs/segment/train4/weights/best.pt")
model.export(format="engine", int8=True, data="/home/vikram/PALLET/pallet_data/pallet_data/data.yaml")
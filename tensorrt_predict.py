from ultralytics import YOLO

model = YOLO("/home/vikram/PALLET/models/best.engine", task="segment")
result = model.predict("/home/vikram/PALLET/pallet_data/train/images/640401-9657_jpg.rf.e4ed33e1051d62ab26ec885a2ab51a57.jpg")
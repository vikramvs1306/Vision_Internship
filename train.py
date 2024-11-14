from ultralytics import YOLO
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")


if __name__=="__main__":

    model = YOLO("/home/santosh/pallet-detection/trained_model.pt")

    model.train(data="/home/santosh/pallet-detection/pallet_data/data.yaml", 
                epochs=250, 
                imgsz=640, 
                device=[0, 1],
                batch=8,
                hsv_h=0.015,
                hsv_s = 0.7,
                hsv_v = 0.4,
                degrees = 0.2,
                translate = 0.1,
                scale = 0.0,
                shear = 0.0,
                perspective = 0.0,
                flipud = 0.5,
                fliplr = 0.5,
                mosaic = 0.3,
                mixup=0.3,
                copy_paste = 0.3,
                bgr=0.7)
    
from ultralytics import YOLO



if __name__=="__main__":
    print("here")
    

    model = YOLO("/home/vikram/Downloads/PALLET/runs/runs/segment/train4/weights/best.pt")

    metrics = model.val(data="/home/vikram/Downloads/PALLET/pallet_data/pallet_data/data.yaml",plots=True, conf=0.25, iou=0.5, device=0)  # no arguments needed, dataset and settings remembered
    print(metrics.box.map)  # map50-95(B)
    print(metrics.box.map50)  # map50(B)
    print(metrics.box.map75)  # map75(B)
    print(metrics.box.maps)  # a list contains map50-95(B) of each category
    print(metrics.seg.map)  # map50-95(M)
    print(metrics.seg.map50)  # map50(M)
    print(metrics.seg.map75)  # map75(M)
    print(metrics.seg.maps)  # a list contains map50-95(M) of each category
        
from ultralytics import YOLO



if __name__=="__main__":
    print("here")
    

    model = YOLO("/home/vikram/Downloads/PALLET/runs/runs/segment/train4/weights/best.pt")

    model.predict(source="/home/vikram/PALLET/pallet_data/pallet_data/valid/images/1579163485692-24_jpg.rf.ede4310dac1aecb5d2a6da31850ac8aa.jpg", 
              show=True, save=True, conf=0.7,line_width=2, save_crop=True, save_txt=True, show_labels=True, show_conf=True, classes=[0,1])
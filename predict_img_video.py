from ultralytics import YOLO

# Load the trained model weights
model = YOLO('/home/vikram/PALLET/runs/runs/segment/train4/weights/best.pt')

model.predict(
    source="/home/vikram/PALLET/BB_4720a110-fc58-4b5e-817c-5557f2a057fd.mp4",  # Path to your video file
    show=True,           # Display the video with predictions
    save=True,           # Save the output video
    conf=0.7,            # Confidence threshold
    line_width=2,        # Bounding box line width
    save_crop=False,     # Save cropped detections (optional)
    save_txt=False,      # Save results in a text file (optional)
    show_labels=True,    # Display labels on the video
    show_conf=True,      # Display confidence scores on the video
    classes=[0, 1]       # Specify classes to detect (optional)
)
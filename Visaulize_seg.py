import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# Set up paths to your images and annotations
image_folder = "/home/vikram/sensor_fusion/Pallets_2/test/images"
annotation_folder = "/home/vikram/sensor_fusion/Pallets_2/test/labels"

# Function to read YOLO segmentation annotations
def read_yolo_annotation(file_path):
    polygons = []
    with open(file_path, 'r') as f:
        for line in f:
            data = line.strip().split()
            class_id = int(data[0])
            points = np.array(data[1:], dtype=np.float32).reshape(-1, 2)
            polygons.append((class_id, points))
    return polygons

# Function to display image with segmented areas, color-coded by class with transparency
def show_image_with_segmentation(image_path, annotation_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Create an overlay for transparency effect
    overlay = image.copy()

    # Define colors for each class
    colors = {
        0: (255, 0, 0, 100),  # Red with alpha for transparency (class 0)
        1: (0, 0, 255, 100)   # Blue with alpha for transparency (class 1)
    }

    # Read annotation
    polygons = read_yolo_annotation(annotation_path)

    # Draw polygons
    for class_id, points in polygons:
        # Convert normalized coordinates to pixel coordinates
        points[:, 0] *= image.shape[1]
        points[:, 1] *= image.shape[0]
        points = points.astype(np.int32)

        # Set color based on class
        color = colors.get(class_id, (0, 255, 0, 100))  # Default green if class_id is unexpected

        # Draw filled polygon on overlay
        overlay = cv2.fillPoly(overlay, [points], color[:3])

        # Draw the outline for the polygon on the original image
        cv2.polylines(image, [points], isClosed=True, color=color[:3], thickness=2)

    # Blend overlay with the original image for transparency
    alpha = 0.5
    blended = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

    # Display the image with Matplotlib
    plt.imshow(blended)
    plt.axis('off')
    plt.show()

# Load and display a sample image with segmentation
sample_image_path = os.path.join(image_folder, '1210335-2054_jpg.rf.0ac27183104cbca99321add103b2d856.jpg')
sample_annotation_path = os.path.join(annotation_folder, '1210335-2054_jpg.rf.0ac27183104cbca99321add103b2d856.txt')

show_image_with_segmentation(sample_image_path, sample_annotation_path)

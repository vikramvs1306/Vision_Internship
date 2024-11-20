For folders "pallet_data","runs" and "yolo_ros" click on the below link:
https://drive.google.com/drive/folders/132RmYJ1xo8Qy5U0nE3AqljofeT7a717n?usp=sharing
Video results can be found in the Google drive file.

### Go through Required Pre-requisites in the next section!!!

Create conda environment using this command:
conda env create -f environment.yaml -n <environment_name>
conda activate <environment_name>


# Vision_Internship

1. Dataset Acquisition and Annotation

    Dataset: Using an open-source pallet dataset annotated with Roboflow's Smart Polygon feature (powered by SAM 2) enables efficient segmentation. Ensure accurate annotation, especially for distant or unclear pallets, as this influences detection reliability.
    YOLOv11 Format: Preparing data in YOLO format streamlines the training process and makes it compatible with modern detection frameworks.

2. Data Preparation and Organization

Divide your dataset into:

    Training Set: For the primary learning of the model.
    Validation Set: To fine-tune and monitor performance during training.
    Test Set: For assessing final model performance.

3. Model Training

    Configuration: Using Ultralytics YOLO with the following settings is ideal:
        Image Size: 640x640 pixels balances processing speed and detection accuracy.
        Augmentation: Extensive augmentation (HSV, flipping, mosaic, etc.) is effective in generalizing to varied warehouse environments.
        Multi-GPU Training: Distributing training over two GPUs (with batch size 8) improves efficiency.

Training Strategy:

    Stage 1: Initial training for 50 epochs without augmentation establishes a baseline.
    Stage 2: Continue with full augmentation for 100 epochs to improve model robustness in dynamic conditions.

4. Model Evaluation

    Metrics: Evaluation based on precision, recall, and mAP at different IoU thresholds provides insight into both detection and segmentation accuracy.
    Class-Specific Observations:
        The ground class performs better than pallets, possibly due to clarity and less visual complexity.
        For pallets, you noted potential improvements with more precise annotation and a broader dataset, which could boost the model's robustness in detecting pallets consistently.

5. Exporting to TensorRT

Using INT8 quantization is critical for optimizing inference performance on edge devices. Here’s the script:

from ultralytics import YOLO

model = YOLO("/content/best.pt")
model.export(format="engine", int8=True, data="/content/drive/MyDrive/Pallets 2.v1i.yolov11/data.yaml")

6. ROS2 Node Deployment

Developing a ROS2 node allows you to integrate the model for real-time detection on a robotic platform:

    Environment Setup: Create and activate the required Conda environment.
    Workspace Structure: Organize as yolobot, with subdirectories for recognition scripts and custom messages (yolov8_msgs).
    Building and Launching: Use colcon build, and if there are issues, set the Python executable path as indicated.

Inference Visualization:

    Launch the model using ros2 launch yolobot_recognition launch_yolov8.launch.py.
    Visualize the results in rviz2 under the inference_result topic.

Key Code Insights

The ROS2 node script (yolov11_ros2_pt.py) utilizes YOLO for detection and CvBridge to convert between ROS Image messages and OpenCV images. Customize paths and topics to match your camera setup and ensure seamless integration with your robot’s sensors.
Final Considerations

    Dataset Augmentation: Adding synthetic or diverse datasets might improve model accuracy, especially for pallets.
    Real-Time Adjustments: Consider further tuning TensorRT settings for latency-sensitive deployments.
    ROS2 Integration: Fine-tune ROS2 message publishing rates and topic configurations to match the real-time processing capacity of Jetson AGX Orin.



# Pre-requisites: 

1. Software Libraries/Frameworks

    Anaconda: A Python distribution for managing dependencies and environments.
    Install from Anaconda.

    PyTorch: Deep learning framework used for model training and inference.
    Install from PyTorch.

    TensorRT: NVIDIA's deep learning inference optimizer and runtime library.
    Install following the instructions on the TensorRT website.

    Ultralytics YOLO: The YOLO (You Only Look Once) object detection model implementation.
    Install via pip:

pip install ultralytics

OpenCV: A library for computer vision tasks, such as image processing.
Install using:

    pip install opencv-python

    ROS2 Foxy: A framework for building robot applications.
    Install from the official ROS2 website.

2. Dataset

    Pallets Dataset: An open-source dataset containing images of pallets in various scenarios. Dataset link (as per the original context) for download or use.

3. Development Environment

    Anaconda Environment Setup: You will need to create a specific environment for the project:
        Use the provided environment.yaml file:

    conda env create -f environment.yaml -n <environment_name>
    conda activate <environment_name>

4. ROS2 Messages

    Yolov8_msgs: Custom messages for the YOLO model inference results. This will be created as part of the ROS2 workspace. The ROS2 package should include:
        InferenceResult: To represent the inference results.
        Yolov8Inference: Message containing information about the inference output.

5. Hardware Requirements

    NVIDIA Jetson AGX Orin: The edge device for real-time inference and deployment.
    Ensure that you have the appropriate software stack (CUDA, TensorRT, etc.) installed on this device.

    Camera: A camera device (e.g., ZED2) to capture images for the detection model. ROS2 topics for image data will be used for feeding input to the model.

6. Additional Tools

    RViz2: A visualization tool for ROS2, used to visualize the detection and segmentation results in real-time. RViz2 can be launched and configured using ROS2 commands.
   This comprehensive setup should yield a reliable pallet detection system optimized for real-time, edge-device applications in dynamic industrial environments.


https://github.com/user-attachments/assets/1ed17926-7924-4197-b4a6-253fd1bd4832


https://github.com/user-attachments/assets/43964d06-7fee-4a3b-b3b6-c333aabdf6be








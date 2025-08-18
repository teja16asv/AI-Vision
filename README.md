# 🎯 Object Detection using YOLOv9 🚀

Developed a web application that performs object detection on uploaded MP4 videos using the YOLOv9 model. This project leverages PyTorch, OpenCV, and Streamlit to enable users to upload videos and view real-time detection with a summary of object counts — all within a simple browser interface.

---

## 🖥️ Features

1. ***Streamlit Web App Setup*** – Built using Streamlit for a responsive and minimal web interface.
2. ***Video Upload Interface*** – Allows users to upload `.mp4` videos directly from their browser.
3. ***YOLOv5 Model Integration*** – Uses a pretrained YOLOv5s model (via PyTorch Hub) for object detection.
4. ***Real-Time Frame Annotation*** – Each video frame is processed and displayed with bounding boxes.
5. ***Object Count Summary*** – Displays the total number of detected objects by class after processing.
6. ***No Manual Model Download*** – The model is loaded automatically using PyTorch Hub.

---

## 📸 Screenshot

![AI-Vision Screenshot](https://github.com/teja16asv/AI-Vision/blob/main/Images/Screenshot1.png)


---

## 🛠️ Steps to Run the Web App:

* Clone the Repository  
    `git clone https://github.com/your-username/object-detection.git`

* Open the folder  
    `cd object-detection`

* Install the required dependencies  
    `pip install -r requirements.txt`

* Start the Streamlit app  
    `streamlit run app.py`

* The app will start running on your local host. Go to the link below in your browser:
  
    > http://localhost:8501/

* Upload an MP4 video and watch real-time object detection with a summary of results!

---

## 📦 Dataset

The YOLOv9 model used is pretrained on the COCO dataset, which likewise contains 80 common object categories such as person, car, dog, and more.

---

💡 Feel free to contribute, raise issues, or provide suggestions! 😊  


# 🎯 AI-Vision: Video Object Detection Web App 🚀

Developed a web application that performs object detection on uploaded MP4 videos using the YOLOv5 model. This project leverages PyTorch, OpenCV, and Streamlit to enable users to upload videos and view real-time detection with a summary of object counts — all within a simple browser interface.

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

![AI-Vision Screenshot]([https://github.com/teja16asv/AI-Vision/issues/1#issue-3256909693](https://private-user-images.githubusercontent.com/145701247/469860070-8701ec81-eba0-44ac-a272-8d84c3fabfb2.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTMyODY0OTUsIm5iZiI6MTc1MzI4NjE5NSwicGF0aCI6Ii8xNDU3MDEyNDcvNDY5ODYwMDcwLTg3MDFlYzgxLWViYTAtNDRhYy1hMjcyLThkODRjM2ZhYmZiMi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzIzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcyM1QxNTU2MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iMjYwM2ExZWI5OGExNjg1YjI4NWZhMWYzNmQ4YTgzYTA5NGMwOWQ3ODc0OTNjMmQ4YjE4NjQwMDgyMzcxOWIxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.P_HRF8X1fa-TlDHyRF_DTF0V7d7kEgjP6Cb7o0fZEGQ))


---

## 🛠️ Steps to Run the Web App:

* Clone the Repository  
    `git clone https://github.com/your-username/AI-Vision.git`

* Open the folder  
    `cd AI-Vision`

* Install the required dependencies  
    `pip install -r requirements.txt`

* Start the Streamlit app  
    `streamlit run app.py`

* The app will start running on your local host. Go to the link below in your browser:
  
    > http://localhost:8501/

* Upload an MP4 video and watch real-time object detection with a summary of results!

---

## 📦 Dataset

The YOLOv5 model used is pretrained on the [COCO dataset](https://cocodataset.org/#home), which contains 80 common object categories like person, car, dog, etc.

---

💡 Feel free to contribute, raise issues, or provide suggestions! 😊  


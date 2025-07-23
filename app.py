import streamlit as st
import torch
import cv2
import tempfile
import numpy as np
from collections import Counter

@st.cache_resource
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

model = load_model()

st.title("🎯 AI-Vision Object Detection")
st.write("Upload a video and see real-time object detection using YOLOv5!")


video_file = st.file_uploader("📁 Upload an MP4 video", type=["mp4"])

if video_file is not None:
    # Save to temp file
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())

    cap = cv2.VideoCapture(tfile.name)

    stframe = st.empty()  # Placeholder for video

    class_counter = Counter()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Inference
        results = model(frame)
        annotated_frame = results.render()[0]

        # Count detections
        labels = results.names
        for pred in results.pred[0]:
            cls = int(pred[5])
            class_counter[labels[cls]] += 1

        # Resize for display
        annotated_frame = cv2.resize(annotated_frame, (720, 480))
        stframe.image(annotated_frame, channels="BGR")

    cap.release()

    # Show detection summary
    st.subheader("📊 Object Count Summary")
    for label, count in class_counter.items():
        st.write(f"- **{label}**: {count}")

    st.success("✅ Video processed successfully!")

import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
import os

# Load YOLOv9 model (you can choose yolov9c.pt or yolov9e.pt)
model = YOLO("yolov9e.pt")

st.title("YOLOv9 Video Object Detection")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save uploaded video to temp file
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_input.write(uploaded_file.read())
    temp_input.close()

    
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_output.close()

    # Process video frame by frame
    cap = cv2.VideoCapture(temp_input.name)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(temp_output.name, fourcc, int(cap.get(5)), 
                          (int(cap.get(3)), int(cap.get(4))))

    stframe = st.empty()  # placeholder for video frames

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLOv9 detection
        results = model.predict(frame, conf=0.5, verbose=False)
        annotated_frame = results[0].plot()  # draw boxes

        # Write to output file
        out.write(annotated_frame)

        # Show live preview in Streamlit
        stframe.image(annotated_frame, channels="BGR")

    cap.release()
    out.release()

    st.success("Processing complete ✅")

    # Display final processed video
    st.video(temp_output.name)

    # Cleanup on rerun
    os.remove(temp_input.name)


















# --------------------------------------------------------------------------------------------------------------------------------
# import streamlit as st
# import torch
# import cv2
# import tempfile
# import numpy as np
# from collections import Counter

# @st.cache_resource
# def load_model():
#     return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# model = load_model()

# st.title("🎯 AI-Vision Object Detection")
# st.write("Upload a video and see real-time object detection using YOLOv5!")


# video_file = st.file_uploader("📁 Upload an MP4 video", type=["mp4"])

# if video_file is not None:
#     # Save to temp file
#     tfile = tempfile.NamedTemporaryFile(delete=False)
#     tfile.write(video_file.read())

#     cap = cv2.VideoCapture(tfile.name)

#     stframe = st.empty()  # Placeholder for video

#     class_counter = Counter()

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Inference
#         results = model(frame)
#         annotated_frame = results.render()[0]

#         # Count detections
#         labels = results.names
#         for pred in results.pred[0]:
#             cls = int(pred[5])
#             class_counter[labels[cls]] += 1

#         # Resize for display
#         annotated_frame = cv2.resize(annotated_frame, (720, 480))
#         stframe.image(annotated_frame, channels="BGR")

#     cap.release()

#     # Show detection summary
#     st.subheader("📊 Object Count Summary")
#     for label, count in class_counter.items():
#         st.write(f"- **{label}**: {count}")

#     st.success("✅ Video processed successfully!")

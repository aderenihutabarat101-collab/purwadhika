import streamlit as st
from ultralytics import YOLO
from collections import Counter
from PIL import Image
import tempfile

model_name = "./yolov12n.pt"
model = YOLO(model_name)

st.title("Vehicle Detection & Counting")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg","png","jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as tmp:

        image.save(tmp.name)

        results = model(tmp.name)

    result = results[0]

    counter = Counter()

    for cls in result.boxes.cls:
        label = result.names[int(cls)]
        counter[label] += 1

    annotated = result.plot()

    st.image(
        annotated,
        caption="Detection Result"
    )

    st.subheader("Vehicle Count")

    for k,v in counter.items():
        st.write(f"{k}: {v}")
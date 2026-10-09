import pytesseract
from PIL import Image
import cv2
import numpy as np

def extract_text_from_image(uploaded_file):
    image = Image.open(uploaded_file).convert("RGB")
    image_array = np.array(image)

    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    processed_image = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    text = pytesseract.image_to_string(
        processed_image,
        config="--psm 6"
    )

    return text.strip()

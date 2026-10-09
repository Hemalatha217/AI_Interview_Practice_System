
import pytesseract
import json
import re
import shutil
from PIL import Image, ImageEnhance, ImageFilter


TESSERACT_PATH = shutil.which("tesseract")

if TESSERACT_PATH is None:
    WINDOWS_TESSERACT_PATH = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    import os

    if os.path.exists(WINDOWS_TESSERACT_PATH):
        TESSERACT_PATH = WINDOWS_TESSERACT_PATH

if TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def preprocess_image(image):
    """Improve image quality before OCR."""

    image = image.convert("L")

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)

    image = image.filter(ImageFilter.SHARPEN)

    return image


def extract_text_from_image(uploaded_file):
    """Extract text from an uploaded image using Tesseract OCR."""

    if not TESSERACT_PATH:
        raise RuntimeError(
            "Tesseract OCR is not installed. "
            "Add tesseract-ocr to packages.txt "
            "in your GitHub repository and redeploy."
        )

    image = Image.open(uploaded_file)

    processed_image = preprocess_image(image)

    text = pytesseract.image_to_string(
        processed_image,
        config="--psm 6"
    )

    return text.strip()


def clean_text(text):
    """Clean OCR text."""

    text = text.replace("\r", "\n")

    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(r"\n+", "\n", text)

    return text.strip()


def extract_question_and_answer(ocr_text):
    """Separate the question and answer from OCR text."""

    text = clean_text(ocr_text)

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    if not lines:
        return {
            "ocr_text": "",
            "detected_question": "",
            "detected_answer": ""
        }

    question = ""
    answer_lines = []
    question_index = -1

    question_patterns = [
        r"^(q\d*[\.\):\-]?)",
        r"^(question[\s\d]*[\.\):\-]?)",
        r"^(what\b)",
        r"^(why\b)",
        r"^(how\b)",
        r"^(when\b)",
        r"^(where\b)",
        r"^(who\b)",
        r"^(which\b)",
        r"^(explain\b)",
        r"^(define\b)",
        r"^(describe\b)",
        r"^(difference\b)"
    ]

    for i, line in enumerate(lines):

        lower_line = line.lower()

        if "?" in line:
            question = line
            question_index = i
            break

        for pattern in question_patterns:
            if re.search(pattern, lower_line):
                question = line
                question_index = i
                break

        if question_index != -1:
            break

    if question_index == -1:
        question = lines[0]
        question_index = 0

    for i in range(question_index + 1, len(lines)):
        answer_lines.append(lines[i])

    answer = " ".join(answer_lines)

    return {
        "ocr_text": text,
        "detected_question": question,
        "detected_answer": answer
    }


def convert_ocr_to_json(ocr_text):
    """Convert OCR output into a dictionary."""

    result = extract_question_and_answer(ocr_text)

    return result


def json_string(data):
    """Convert a dictionary into a formatted JSON string."""

    return json.dumps(
        data,
        indent=4,
        ensure_ascii=False
    )

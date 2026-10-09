# app.py

import streamlit as st
import json

from question import generate_questions
from ocr import (
    extract_text_from_image,
    convert_ocr_to_json,
    json_string
)
from answer import evaluate_answer


st.set_page_config(
    page_title="AI Interview Practice",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 Interview Practice System")

st.write(
    "Practice interview questions and upload "
    "your handwritten or printed answer."
)


roles = [
    "Software Developer",
    "Python Developer",
    "Java Developer",
    "Web Developer",
    "Data Analyst",
    "Data Scientist",
    "AI/ML Engineer",
    "Database Administrator"
]

role = st.selectbox(
    "Select Interview Role",
    roles
)

if st.button("Generate Interview Questions"):

    questions = generate_questions(
        role,
        number_of_questions=10
    )

    st.session_state.questions = questions
    st.session_state.role = role

    st.session_state.pop(
        "ocr_text",
        None
    )

    st.session_state.pop(
        "ocr_json",
        None
    )

    st.session_state.pop(
        "evaluation",
        None
    )

    st.success(
        f"Questions generated for {role}"
    )

if "questions" in st.session_state:

    st.subheader("📝 Interview Questions")

    questions = st.session_state.questions

    selected_question = st.radio(
        "Select a question to answer:",
        questions
    )

    st.session_state.selected_question = (
        selected_question
    )

    st.info(
        f"Selected Question: {selected_question}"
    )

    st.subheader("📷 Upload Your Answer")

    uploaded_file = st.file_uploader(
        "Upload an image containing your question and answer",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:

        st.image(
            uploaded_file,
            caption="Uploaded Answer",
            use_container_width=True
        )

        if st.button("Extract Text from Image"):

            with st.spinner(
                "Reading image using Tesseract..."
            ):

                ocr_text = extract_text_from_image(
                    uploaded_file
                )

                ocr_json = convert_ocr_to_json(
                    ocr_text
                )

                st.session_state.ocr_text = (
                    ocr_text
                )

                st.session_state.ocr_json = (
                    ocr_json
                )

    if "ocr_text" in st.session_state:

        st.subheader("🔍 Extracted OCR Text")

        st.text_area(
            "Text extracted from image:",
            st.session_state.ocr_text,
            height=150
        )

    if "ocr_json" in st.session_state:

        st.subheader("📄 OCR JSON")

        st.code(
            json_string(
                st.session_state.ocr_json
            ),
            language="json"
        )

        detected_question = (
            st.session_state.ocr_json
            .get("detected_question", "")
        )

        detected_answer = (
            st.session_state.ocr_json
            .get("detected_answer", "")
        )

        st.write(
            "**Detected Question:**",
            detected_question
        )

        st.write(
            "**Detected Answer:**",
            detected_answer
        )

        if st.button("Evaluate Answer"):

            generated_question = (
                st.session_state.selected_question
            )

            result = evaluate_answer(
                generated_question,
                detected_question,
                detected_answer
            )

            st.session_state.evaluation = result

    if "evaluation" in st.session_state:

        result = st.session_state.evaluation

        st.subheader("📊 Evaluation Result")

        score = result["score"]

        st.metric(
            "Score",
            f"{score}/100"
        )

        st.write(
            "**Status:**",
            result["status"]
        )

        st.write(
            "**Question Similarity:**",
            f"{result['question_similarity']}%"
        )

        st.write(
            "**Generated Question:**",
            result["generated_question"]
        )

        st.write(
            "**Detected Question:**",
            result["detected_question"]
        )

        st.write(
            "**Detected Answer:**",
            result["detected_answer"]
        )

        st.write(
            "**Feedback:**",
            result["feedback"]
        )

        if result["matched_keywords"]:

            st.write(
                "**Matched Keywords:**",
                ", ".join(
                    result["matched_keywords"]
                )
            )

        st.write(
            "**Improved Answer Suggestion:**",
            result["improved_answer"]
        )

        st.subheader("📄 Final Evaluation JSON")

        st.code(
            json.dumps(
                result,
                indent=4,
                ensure_ascii=False
            ),
            language="json"
        )
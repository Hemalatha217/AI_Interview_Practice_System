
import streamlit as st
from ocr import extract_text
from question_generator import generate_questions
from answer_evaluator import evaluate_answer

st.set_page_config(
    page_title="AI Interview Practice System",
    page_icon="🎤"
)

st.title("AI Interview Practice System")

st.write(
    "Select an interview role and practice role-specific interview questions."
)

# --------------------------------------------------
# SELECT INTERVIEW ROLE
# --------------------------------------------------

job_roles = [
    "Software Engineer",
    "Full Stack Developer",
    "Frontend Developer",
    "Backend Developer",
    "Web Developer",
    "Mobile App Developer",

    "AI Engineer",
    "Machine Learning Engineer",
    "Generative AI Engineer",
    "Prompt Engineer",

    "Data Analyst",
    "Data Scientist",
    "Data Engineer",

    "Cybersecurity Analyst",
    "Ethical Hacker",

    "Project Manager",
    "Product Manager",

    "HR Executive",
    "Recruiter",

    "Financial Analyst"
]

role = st.selectbox(
    "Select Interview Role",
    job_roles
)

# --------------------------------------------------
# GENERATE QUESTIONS
# --------------------------------------------------

if st.button("Generate Questions"):

    questions = generate_questions(role)

    if questions:
        st.session_state["questions"] = questions
        st.session_state["role"] = role
    else:
        st.error("Unable to generate questions.")


# --------------------------------------------------
# DISPLAY QUESTIONS
# --------------------------------------------------

if "questions" in st.session_state:

    st.subheader(
        f"{st.session_state['role']} Interview Questions"
    )

    for i, q in enumerate(
        st.session_state["questions"],
        start=1
    ):
        st.write(f"**Q{i}. {q}**")


# --------------------------------------------------
# UPLOAD ANSWER SHEET
# --------------------------------------------------

if "questions" in st.session_state:

    st.divider()

    st.subheader("Practice Your Answer")

    uploaded_file = st.file_uploader(
        "Upload Your Answer Sheet",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Uploaded Answer Sheet",
            width=600
        )

        # ------------------------------------------
        # OCR
        # ------------------------------------------

        extracted_text = extract_text(uploaded_file)

        st.subheader("Extracted Answer")

        st.text_area(
            "Your Answer",
            extracted_text,
            height=200
        )

        # ------------------------------------------
        # EVALUATE ANSWER
        # ------------------------------------------

        if st.button("Evaluate Answer"):

            score, feedback = evaluate_answer(
                st.session_state["questions"][0],
                extracted_text
            )

            st.success(
                f"Score: {score}/100"
            )

            st.subheader("Feedback")

            st.write(feedback)


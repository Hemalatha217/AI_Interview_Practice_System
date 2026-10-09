import re
STOP_WORDS = {
    "what",
    "is",
    "are",
    "the",
    "a",
    "an",
    "of",
    "to",
    "and",
    "in",
    "on",
    "for",
    "why",
    "how",
    "what's",
    "explain",
    "define",
    "describe",
    "difference",
    "between"
}
def normalize_text(text):
    """
    Convert text to lowercase and remove unnecessary characters.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
def get_keywords(text):
    """
    Extract useful keywords from text.
    """
    text = normalize_text(text)
    words = text.split()
    keywords = []
    for word in words:
        if word not in STOP_WORDS and len(word) > 1:
            keywords.append(word)
    return set(keywords)

def calculate_question_similarity(generated_question, detected_question):
    """
    Compare generated question and uploaded question.
    Returns a percentage between 0 and 100.
    """
    generated_keywords = get_keywords(generated_question)
    detected_keywords = get_keywords(detected_question)
    if not generated_keywords or not detected_keywords:
        return 0
    common_words = generated_keywords.intersection(
        detected_keywords
    )
    union_words = generated_keywords.union(
        detected_keywords
    )
    similarity = (
        len(common_words) / len(union_words)
    ) * 100
    return round(similarity, 2)

def questions_match(generated_question, detected_question):
    """
    Decide whether the uploaded question matches
    the generated interview question.
    """
    similarity = calculate_question_similarity(
        generated_question,
        detected_question
    )
    generated_keywords = get_keywords(generated_question)
    detected_keywords = get_keywords(detected_question)
    common_words = generated_keywords.intersection(
        detected_keywords
    )

    if normalize_text(generated_question) == normalize_text(
        detected_question
    ):
        return True, 100
    
    if len(common_words) >= 2 and similarity >= 30:
        return True, similarity

    return False, similarity

def evaluate_answer_keywords(generated_question, answer):
    """
    Evaluate answer based on how many important
    keywords from the question appear in the answer.
    """
    question_keywords = get_keywords(generated_question)
    answer_keywords = get_keywords(answer)

    if not question_keywords:
        return 0, []

    matched_keywords = (
        question_keywords.intersection(answer_keywords)
    )
    percentage = (
        len(matched_keywords) /
        len(question_keywords)
    ) * 100

    return round(percentage), list(matched_keywords)

def evaluate_answer(
    generated_question,
    detected_question,
    detected_answer
):
    """
    Main answer evaluation function.
    """
    match, similarity = questions_match(
        generated_question,
        detected_question
    )

    if not match:

        mismatch_score = min(
            20,
            max(0, int(similarity / 5))
        )

        return {
            "generated_question": generated_question,
            "detected_question": detected_question,
            "detected_answer": detected_answer,
            "status": "Question Mismatch",
            "score": mismatch_score,
            "question_similarity": similarity,
            "feedback": (
                "The uploaded question does not match "
                "the generated interview question. "
                "Therefore, the answer cannot be "
                "properly evaluated."
            ),
            "matched_keywords": [],
            "improved_answer": (
                "Please upload an answer for the "
                "generated question."
            )
        }

    if not detected_answer.strip():

        return {
            "generated_question": generated_question,
            "detected_question": detected_question,
            "detected_answer": "",
            "status": "No Answer Detected",
            "score": 0,
            "question_similarity": similarity,
            "feedback": (
                "The question matches, but no answer "
                "could be detected from the image."
            ),
            "matched_keywords": [],
            "improved_answer": (
                "Please upload an image containing "
                "your answer."
            )
        }

    keyword_score, matched_keywords = (
        evaluate_answer_keywords(
            generated_question,
            detected_answer
        )
    )

    answer_length = len(detected_answer.split())

    if answer_length >= 30:
        length_bonus = 20
    elif answer_length >= 15:
        length_bonus = 10
    else:
        length_bonus = 0

    score = keyword_score * 0.8 + length_bonus

    score = min(100, int(score))

    if score >= 80:

        status = "Good Answer"

        feedback = (
            "The uploaded question matches the "
            "generated question and the answer "
            "contains relevant keywords with "
            "reasonable explanation."
        )

    elif score >= 50:

        status = "Partially Correct"

        feedback = (
            "The question matches, but the answer "
            "needs more relevant points and "
            "explanation."
        )

    else:

        status = "Weak Answer"

        feedback = (
            "The question matches, but the answer "
            "does not contain enough relevant "
            "information."
        )

    improved_answer = (
        "Try to answer the question directly, "
        "include the important concepts related "
        "to the topic, and provide a simple example "
        "where appropriate."
    )

    return {
        "generated_question": generated_question,
        "detected_question": detected_question,
        "detected_answer": detected_answer,
        "status": status,
        "score": score,
        "question_similarity": similarity,
        "feedback": feedback,
        "matched_keywords": matched_keywords,
        "improved_answer": improved_answer
    }
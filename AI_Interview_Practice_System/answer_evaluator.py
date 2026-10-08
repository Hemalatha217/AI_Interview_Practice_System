def evaluate_answer(question, answer):

    words = len(answer.split())

    if words > 50:

        score = 90

        feedback = (
            "Good answer with sufficient explanation."
        )

    elif words > 20:

        score = 70

        feedback = (
            "Average answer. Add more details."
        )

    else:

        score = 50

        feedback = (
            "Answer is too short."
        )

    return score, feedback
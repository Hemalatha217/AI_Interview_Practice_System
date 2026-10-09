ROLE_QUESTIONS = {
    "Software Developer": [
        "What is SDLC?",
        "Explain the four main principles of Object-Oriented Programming.",
        "What is the difference between a stack and a queue?",
        "What is the difference between an array and a linked list?",
        "What is exception handling and why is it important?",
        "How do you debug a program that produces incorrect output?",
        "What is Git and why is version control important?",
        "What is the difference between a primary key and a foreign key?",
        "How would you improve the performance of a slow application?",
        "Explain a software project you have worked on."
    ],

    "Python Developer": [
        "What is Python?",
        "What are the features of Python?",
        "What is the difference between a list and a tuple?",
        "What are dictionaries in Python?",
        "What is exception handling in Python?",
        "What are Python functions?",
        "What is the difference between deep copy and shallow copy?",
        "What are modules and packages in Python?",
        "What is inheritance in Python?",
        "What are decorators in Python?"
    ],

    "Java Developer": [
        "What is Java?",
        "What are the features of Java?",
        "What is the difference between JDK, JRE and JVM?",
        "What is Object-Oriented Programming?",
        "What is inheritance in Java?",
        "What is method overloading?",
        "What is method overriding?",
        "What is exception handling in Java?",
        "What is an interface in Java?",
        "What is the difference between an array and ArrayList?"
    ],

    "Web Developer": [
        "What is HTML?",
        "What is CSS?",
        "What is JavaScript?",
        "What is the difference between HTML and CSS?",
        "What is responsive web design?",
        "What is the DOM?",
        "What is an API?",
        "What is the difference between frontend and backend?",
        "What is HTTP?",
        "What is the difference between GET and POST?"
    ],

    "Data Analyst": [
        "What is data analysis?",
        "What is the difference between structured and unstructured data?",
        "What is data cleaning?",
        "What is exploratory data analysis?",
        "What is the difference between mean, median and mode?",
        "What is data visualization?",
        "What is SQL?",
        "What is a primary key?",
        "What is a JOIN in SQL?",
        "What is the difference between WHERE and HAVING?"
    ],

    "Data Scientist": [
        "What is data science?",
        "What is machine learning?",
        "What is supervised learning?",
        "What is unsupervised learning?",
        "What is overfitting?",
        "What is underfitting?",
        "What is a training dataset?",
        "What is feature engineering?",
        "What is cross-validation?",
        "What is the difference between classification and regression?"
    ],

    "AI/ML Engineer": [
        "What is Artificial Intelligence?",
        "What is Machine Learning?",
        "What is Deep Learning?",
        "What is a neural network?",
        "What is supervised learning?",
        "What is unsupervised learning?",
        "What is reinforcement learning?",
        "What is overfitting?",
        "What is a loss function?",
        "What is model training?"
    ],

    "Database Administrator": [
        "What is a database?",
        "What is DBMS?",
        "What is a primary key?",
        "What is a foreign key?",
        "What is normalization?",
        "What is SQL?",
        "What is a database index?",
        "What is a transaction?",
        "What is the ACID property?",
        "What is a database backup?"
    ]
}


def generate_questions(role, number_of_questions=10):
    """
    Returns interview questions for the selected role.
    """

    if role not in ROLE_QUESTIONS:
        return []

    questions = ROLE_QUESTIONS[role]

    return questions[:number_of_questions]
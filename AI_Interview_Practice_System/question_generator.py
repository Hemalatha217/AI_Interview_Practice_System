
def generate_questions(role):

    role_questions = {

        "Software Engineer": [
            "What is the Software Development Life Cycle (SDLC)?",
            "Explain the four main principles of Object-Oriented Programming.",
            "What is the difference between a stack and a queue?",
            "What are the differences between an array and a linked list?",
            "What is exception handling and why is it important?",
            "How do you debug a program that produces incorrect output?",
            "What is Git and why is version control important?",
            "What is the difference between a primary key and a foreign key?",
            "How would you improve the performance of a slow application?",
            "Explain a software project you have developed."
        ],

        "Full Stack Developer": [
            "What is the difference between frontend and backend development?",
            "What is the role of HTML, CSS, and JavaScript in a web application?",
            "What is a REST API?",
            "How does a frontend communicate with a backend?",
            "How do you connect a web application to a database?",
            "What is authentication and authorization?",
            "What is the difference between SQL and NoSQL databases?",
            "How do you handle errors in a full-stack application?",
            "How would you deploy a full-stack application?",
            "Explain a full-stack project you have developed."
        ],

        "Frontend Developer": [
            "What are semantic HTML elements?",
            "Explain the CSS box model.",
            "What is responsive web design?",
            "What is the difference between Flexbox and CSS Grid?",
            "What is the DOM in JavaScript?",
            "What is event handling in JavaScript?",
            "What is the difference between let, const, and var?",
            "How do you improve the performance of a website?",
            "How do you make a website accessible?",
            "Explain a frontend project you have developed."
        ],

        "Backend Developer": [
            "What is backend development?",
            "What is a REST API?",
            "What is the difference between GET and POST requests?",
            "How does authentication work in a backend application?",
            "What is the difference between SQL and NoSQL?",
            "How do you optimize a database query?",
            "What is exception handling in backend development?",
            "What is middleware?",
            "How would you design a scalable backend system?",
            "Explain a backend project you have developed."
        ],

        "Web Developer": [
            "What is the difference between HTML, CSS, and JavaScript?",
            "What are semantic HTML elements?",
            "What is responsive web design?",
            "What is the CSS box model?",
            "What is the DOM?",
            "What is an API?",
            "What is the difference between frontend and backend?",
            "How do you debug a web application?",
            "How do you improve website performance?",
            "Explain a web development project you have developed."
        ],

        "Mobile App Developer": [
            "What is the difference between native and cross-platform mobile applications?",
            "What is the Android application lifecycle?",
            "What is an Activity in Android?",
            "How does a mobile application communicate with an API?",
            "What is mobile application state management?",
            "How do you handle errors in a mobile application?",
            "How do you improve mobile application performance?",
            "What is mobile application testing?",
            "How do you secure data in a mobile application?",
            "Explain a mobile application you have developed."
        ],

        "AI Engineer": [
            "What is Artificial Intelligence?",
            "What is the difference between Artificial Intelligence and Machine Learning?",
            "What is supervised learning?",
            "What is unsupervised learning?",
            "What is a neural network?",
            "What is model training?",
            "What is overfitting?",
            "What are evaluation metrics for AI models?",
            "How can an AI model be integrated into a software application?",
            "Explain an AI project you have developed."
        ],

        "Machine Learning Engineer": [
            "What is the difference between supervised and unsupervised learning?",
            "What is overfitting and how can you prevent it?",
            "What is underfitting?",
            "What is feature engineering?",
            "What is the difference between classification and regression?",
            "What is cross-validation?",
            "What is the purpose of a confusion matrix?",
            "How do you select a machine learning algorithm?",
            "How do you deploy a machine learning model?",
            "Explain a machine learning project you have developed."
        ],

        "Generative AI Engineer": [
            "What is Generative AI?",
            "What is a Large Language Model?",
            "What is prompt engineering?",
            "What is a token?",
            "What is an embedding?",
            "What is Retrieval-Augmented Generation?",
            "What is hallucination in Generative AI?",
            "What is fine-tuning?",
            "How can an LLM be integrated into an application?",
            "Explain a Generative AI project you have developed."
        ],

        "Prompt Engineer": [
            "What is prompt engineering?",
            "What is zero-shot prompting?",
            "What is few-shot prompting?",
            "What is prompt context?",
            "How can you improve an ineffective prompt?",
            "What is prompt evaluation?",
            "What causes hallucinations in language models?",
            "What is the difference between a system prompt and a user prompt?",
            "How would you design a prompt for a specific business task?",
            "Explain a prompt engineering project you have worked on."
        ],

        "Data Analyst": [
            "What is data cleaning?",
            "How do you handle missing values in a dataset?",
            "What is the difference between mean, median, and mode?",
            "What is exploratory data analysis?",
            "How is SQL used in data analysis?",
            "What is data visualization?",
            "What is a KPI?",
            "How do you identify trends and patterns in data?",
            "How do you validate the accuracy of your analysis?",
            "Explain a data analysis project you have worked on."
        ],

        "Data Scientist": [
            "What is the difference between Data Science and Data Analysis?",
            "What is exploratory data analysis?",
            "How do you handle missing data?",
            "What is feature engineering?",
            "What is correlation?",
            "What is regression?",
            "What is classification?",
            "What is cross-validation?",
            "How do you evaluate a machine learning model?",
            "Explain a Data Science project you have developed."
        ],

        "Data Engineer": [
            "What is Data Engineering?",
            "What is a data pipeline?",
            "What is ETL?",
            "What is the difference between ETL and ELT?",
            "What is a data warehouse?",
            "What is a data lake?",
            "How do you handle large datasets?",
            "What is data quality?",
            "How do you design a scalable data pipeline?",
            "Explain a Data Engineering project you have worked on."
        ],

        "Cybersecurity Analyst": [
            "What is the CIA triad?",
            "What is the difference between a threat, vulnerability, and risk?",
            "What is authentication?",
            "What is authorization?",
            "What is encryption?",
            "What is a firewall?",
            "What is phishing?",
            "What is malware?",
            "How would you investigate a security incident?",
            "Explain a cybersecurity project you have worked on."
        ],

        "Ethical Hacker": [
            "What is ethical hacking?",
            "What is penetration testing?",
            "What is vulnerability assessment?",
            "What is network scanning?",
            "What is SQL injection?",
            "What is cross-site scripting?",
            "What is social engineering?",
            "What is the difference between a vulnerability and an exploit?",
            "How do you document a security vulnerability?",
            "Explain an ethical hacking project you have worked on."
        ],

        "Project Manager": [
            "What are the main stages of project management?",
            "What is project scope?",
            "How do you create a project schedule?",
            "How do you identify and manage project risks?",
            "What is Agile methodology?",
            "What is Scrum?",
            "What is a sprint?",
            "How do you handle conflicts within a project team?",
            "How do you track project progress?",
            "Explain a project you have managed."
        ],

        "Product Manager": [
            "What are the main responsibilities of a Product Manager?",
            "How do you identify customer requirements?",
            "What is product-market fit?",
            "How do you prioritize product features?",
            "What is a product roadmap?",
            "How do you measure product success?",
            "What is an MVP?",
            "How do you analyze customer feedback?",
            "How do you work with developers and designers?",
            "Explain a product you would like to develop."
        ],

        "HR Executive": [
            "What is the recruitment process?",
            "What is employee onboarding?",
            "What is performance management?",
            "How do you handle employee conflicts?",
            "What is employee engagement?",
            "How do you maintain employee records?",
            "What is workforce planning?",
            "How do you handle confidential employee information?",
            "What are important HR metrics?",
            "How would you handle an employee grievance?"
        ],

        "Recruiter": [
            "What are the main stages of recruitment?",
            "How do you source candidates?",
            "How do you screen resumes?",
            "How do you evaluate candidates during an initial interview?",
            "What is an Applicant Tracking System?",
            "How do you handle multiple job openings?",
            "How do you assess whether a candidate fits a job requirement?",
            "How do you communicate with candidates?",
            "How do you handle a difficult hiring requirement?",
            "How would you improve the recruitment process?"
        ],

        "Financial Analyst": [
            "What is financial analysis?",
            "What is a balance sheet?",
            "What is an income statement?",
            "What is cash flow?",
            "What is financial forecasting?",
            "What is budgeting?",
            "What is financial modelling?",
            "What is the difference between revenue and profit?",
            "What financial ratios are commonly used for analysis?",
            "How would you analyze a company's financial performance?"
        ]
    }

    return role_questions.get(role, [])


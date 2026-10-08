# AI_Interview_Practice_System

## About the Project

AI Interview Practice System is a web-based application that helps users practice for interviews in a simple and interactive way.

The system provides an easy-to-use interface for interview preparation and allows users to work with interview-related content using OCR.

The project is developed using Python and Streamlit.

### Live Demo

https://aiinterviewpracticesystem-n6bo4qgxebdzkbn8uzbnkt.streamlit.app/

### Technologies Used

- Python
- Streamlit
- Pillow
- Pytesseract
- Tesseract OCR

### Features

- Practice interview questions
- Interactive web interface
- Upload images
- Extract text from images using OCR
- Process images using Pillow
- Display extracted text
- Simple and user-friendly interface

### How It Works

User | v Streamlit Application | v Interview Practice | v Upload Image | v Image Processing | v Tesseract OCR | v Extracted Text | v Display Result


### Main Modules

1. **Interview Practice**

Users can use the application to practice interview-related questions.

2. **Image Upload**

Users can upload an image containing text.

3. **Image Processing**

Pillow is used to read and process the uploaded image.

4. **OCR Text Extraction**

Pytesseract and Tesseract OCR are used to extract text from the image.

### Example

The user uploads an image containing:

Tell me about yourself What are your strengths? Why should we hire you?


The OCR system extracts the text and displays it in the application.

### Project Structure

AIInterviewPracticeSystem/ │ ├── AIInterviewPracticeSystem/ │ └── Project source files │ ├── README.md ├── requirements.txt ├── packages.txt │ └── .gitignore


### Installation

#### Requirements

- Python 3.x
- Git
- pip

### Clone the Repository

git clone https://github.com/Hemalatha217/AIInterviewPractice_System.git


### Open the Project Folder

cd AIInterviewPractice_System


### Install Required Packages

pip install -r requirements.txt


### Run the Application

streamlit run app.py


The application will open in your browser.

### Requirements

The main packages used in this project are:

streamlit pillow pytesseract


Tesseract OCR is required for text extraction.

### Project Purpose

The purpose of this project is to make interview preparation easier and more accessible.

The system provides a simple web-based platform where users can practice interview-related activities.

### Future Enhancements

The project can be improved by adding:

- AI-generated interview questions
- Voice-based interview practice
- Speech-to-text
- AI-based answer evaluation
- Answer scoring
- Personalized feedback
- Resume-based questions
- Interview performance reports

### Benefits

- Easy interview preparation
- Simple web interface
- Automatic text extraction
- Reduces manual text entry
- Easy to run and deploy

### Author

**Hemalatha**

### License

This project is developed for educational and demonstration purposes.

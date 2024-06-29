# Full-Stack PDF Question-Answer Application

## Overview

This is a full-stack application that allows users to upload PDF documents and ask questions regarding the content of these documents. The backend processes these documents and utilizes natural language processing to provide answers to the questions posed by the users.

## Tools and Technologies

- **Backend**: FastAPI
- **NLP Processing**: LangChain/LLamaIndex
- **Frontend**: React.js
- **Database**: SQLite or PostgreSQL
- **File Storage**: Local filesystem or cloud storage (e.g., AWS S3)

## Features

- **PDF Upload**:
  - Users can upload PDF documents to the application.
  - The application stores the PDF and extracts its text content for further processing.
  
- **Asking Questions**:
  - Users can ask questions related to the content of an uploaded PDF.
  - The system processes the question and the content of the PDF to provide an answer.

- **Displaying Answers**:
  - The application displays the answer to the user’s question.
  - Users can ask follow-up or new questions on the same document.


# Medical Document Parsing and Extracting System

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Running the API](#running-the-api)
- [Example API Request](#example-api-request)
- [Testing](#testing)
- [Project Structure](#project-structure)

## Overview
This project is designed to extract specific information from medical documents, such as prescriptions and patient details. It uses OCR to convert document images to text and then parses the text to retrieve relevant fields.

## Features
- **Document Parsing**: Extracts patient information from prescriptions and general medical records.
- **OCR Integration**: Uses `pytesseract` for OCR to convert images of documents into text.
- **PDF to Image Conversion**: Utilizes `pdf2image` to convert PDF documents into images.
- **Data Extraction**: Uses regular expressions to accurately extract fields from the text.
- **API Development**: Provides a FastAPI-based web service for document uploads and data extraction.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/medical-document-parser.git
    cd medical-document-parser
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Install Poppler for PDF conversion:
    - Download Poppler from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
    - Extract the contents and add the `bin` folder to your system PATH.

5. Install Tesseract OCR:
    - Download Tesseract from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
    - Install it and add the installation path to your system PATH.

## Usage

### Running the API
1. Start the FastAPI server:
    ```bash
    uvicorn backend.src.main:app --reload
    ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

### Example API Request
- Endpoint: `/extract_from_doc`
- Method: `POST`
- Parameters:
    - `file_format`: The format of the document (`prescription` or `patient_details`).
    - `file`: The document file to be uploaded.

## Testing
Run the tests using `pytest`:
```bash
pytest
```

## Project Structure
- `backend/src/`: Contains the main source code for the parsers and API.
- `test/`: Contains unit tests for the parsers.
- `frontend/`: Contains frontend-related files (if any).
- `notebooks/`: Contains Jupyter notebooks for experimentation and development.

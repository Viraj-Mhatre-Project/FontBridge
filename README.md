# System Architecture

AksharSetu is designed as a modular document processing system that converts
legacy Marathi fonts (such as Shivaji) into Unicode Marathi.

## Core Components

The system contains two main layers:

1. Core Processing Engine (Python)
2. User Interface Layer (Flutter)

---

## 1. Core Engine

The Python core engine is responsible for all heavy processing tasks.

Modules:

converter.py  
Handles Shivaji → Unicode conversion.

extractor.py  
Extracts text from PDF and DOCX documents.

ocr.py  
Processes scanned images using OCR.

pdf_generator.py  
Generates clean Unicode PDFs.

---

## 2. Flutter Application

The Flutter application provides the cross-platform user interface.

Platforms supported:

- Android
- Windows
- Linux
- macOS

Main UI features:

- Upload document
- Scan document
- Preview converted text
- Export clean PDF
- Share converted file

---

## 3. Processing Workflow

The full system workflow:

User Upload / Scan
        ↓
Document Input
        ↓
Text Extraction
        ↓
Font Detection
        ↓
Shivaji → Unicode Conversion
        ↓
Unicode Text
        ↓
PDF Generation
        ↓
Preview in Flutter
        ↓
Download / Share

---

## 4. Project Structure

aksharsetu/
│
├── core_engine/
│   ├── converter.py
│   ├── extractor.py
│   ├── ocr.py
│   └── pdf_generator.py
│
├── flutter_app/
│
├── assets/
│   └── fonts/
│
├── docs/
│   ├── shivaji_mapping.json
│   ├── conversion_rules.md
│   └── system_architecture.md

---

## 5. Future Enhancements

- Support for additional legacy Marathi fonts
- Batch document conversion
- Cloud processing support
- AI-based OCR correction
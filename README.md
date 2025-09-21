# resume-relevance-checker
A smart tool for placement teams to find the perfect candidates for job opportunities.
Project Overview

The Automated Resume Relevance Check System is a tool designed to help recruiters quickly and accurately assess how relevant a candidate’s resume is for a given job description (JD). This system leverages AI and Large Language Models to score resumes, identify matched and missing skills, and provide a short summary, significantly reducing manual screening time.

Features

Real-time relevance scoring (0–100%)

Highlight matched and missing skills

Support for multiple formats: PDF & DOCX

Easy-to-use web interface using Streamlit

Optionally tracks workflow using LangGraph & LangSmith

Exportable results in JSON or CSV

Tech Stack
Layer	Technology / Library
AI & LLM	OpenAI GPT-4, LangChain
Workflow	LangGraph
Tracking	LangSmith
Embeddings	Chroma / FAISS
File Handling	PyPDF2, python-docx
UI	Streamlit
Language	Python
Installation

Clone the repository:

git clone https://github.com/YourUsername/resume-relevance-checker.git
cd resume-relevance-checker


Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

Usage

Run the Streamlit app:

streamlit run app.py


Open the app in your browser.

Paste the Job Description and upload a Resume (PDF/DOCX).

Click “Check Relevance” to see:

Relevance Score

Matched Skills

Missing Skills

Summary

Project Structure
resume-relevance-checker/
│── app.py                  # Main Streamlit app
│── requirements.txt        # Dependencies
│── README.md               # Project description
│
├── config/
│   └── settings.py         # API keys & config
├── data/
│   ├── resumes/            # Sample resumes
│   └── jd/                 # Sample job descriptions
├── modules/
│   ├── extractors.py       # Resume/JD text extraction
│   ├── relevance_checker.py# LLM scoring logic
│   ├── embeddings.py       # Embeddings & vector store
│   └── utils.py            # Helper functions
├── outputs/
│   ├── results.json        # Raw results
│   └── reports/            # Exported reports
├── notebooks/
│   └── experiments.ipynb   # Testing & experiments
└── tests/                  # Unit tests

Future Enhancements

Batch processing for multiple resumes

Rank resumes automatically

Export detailed reports

Full LangGraph workflow visualization

Feedback loop for improving AI scoring accuracy

License

This project is for educational and hackathon purposes.


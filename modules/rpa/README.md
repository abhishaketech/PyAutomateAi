# PyAutomateAI
# 🤖 PyAutomate AI — RPA Control Panel

A powerful, modular automation system built using **Python**, **Streamlit**, and **AI (Gemini Pro)** to run RPA (Robotic Process Automation) tasks from a sleek web interface.

> Automate tasks like web scraping, OCR, PDF text extraction, desktop control, email notifications, and AI-powered content generation — all from your browser.

---

## 🧰 Features

- ✅ **Web Scraping** (books.toscrape.com)
- ✅ **Desktop Automation** (opens Notepad, types text)
- ✅ **OCR** (extract text from uploaded images)
- ✅ **PDF Text Extraction**
- ✅ **Send Emails via Gmail**
- ✅ **Ask Gemini AI for text responses**
- ✅ **Workflow Builder** (chain multiple tasks in sequence)
- ⚙️ Future-ready with support for:
  - Cloud deployment
  - Dashboard & reporting
  - Slack/email integration

---

## 🖼️ Live Demo

Run locally and access via `http://localhost:8501`.

---

## 📦 Tech Stack

| Layer     | Tool/Library                  |
|-----------|-------------------------------|
| UI        | [Streamlit](https://streamlit.io) |
| AI        | [Google Gemini API](https://ai.google.dev/) |
| OCR       | `pytesseract`, `Pillow`       |
| PDF       | `PyMuPDF (fitz)`              |
| Email     | `smtplib`, `email.mime`       |
| Scraping  | `requests`, `BeautifulSoup`   |
| Backend   | Python Modules (modular RPA)  |

---

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/arfaive2004/pyautomate-ai.git
cd pyautomate-ai

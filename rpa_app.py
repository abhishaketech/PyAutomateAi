import streamlit as st
from modules.rpa import file_extractor, notifier
from modules.rpa import scraper, desktop_bot, ocr_engine
from modules.rpa import gemini_engine
from modules.rpa import workflow_engine
from modules.rpa import desktop_bot

import os


# Set page configuration FIRST — must be before any other Streamlit calls
st.set_page_config(page_title="Workflow Builder", layout="centered")

# Streamlit content starts here
st.title("Workflow Builder")
st.markdown("Run automation tasks directly from this interface.")


'''Sidebar dropdown for showcasing future features:
- Lets the user explore what's coming in the roadmap
- Displays a description when a feature is selected'''

# Sidebar: Future Features
st.sidebar.title("Future Features")
future_features = st.sidebar.selectbox(
    "Explore what's coming next:",
    [
        "AI Decision Making (Gemini Integration)",
        "PDF and Excel Data Extraction",
        "Workflow Builder",
        "Cloud Deployment",
        "Dashboard and Reporting",
        "Slack/Email Notifications"
    ]
)

st.sidebar.info(f"Selected: {future_features}")

'''Main Section: Book Scraper
- Button to start web scraping from books.toscrape.com
- Saves the data to a CSV
- Shows a download button so user can get the file directly'''

# Section: Book Scraper
if st.button("Run Book Scraper"):
    data = scraper.scrape_books()
    scraper.save_to_csv(data)
    st.success(f"Scraped and saved {len(data)} books to books.csv")

    with open("books.csv", "rb") as file:
        st.download_button(
            label="Download books.csv",
            data=file,
            file_name="books.csv",
            mime="text/csv"
        )

# Section: Desktop Automation
if st.button("Run Desktop Automation"):
    desktop_bot.open_target("notepad.exe")
    desktop_bot.type_text("Automated by PyAutomate AI")
    st.success("Notepad opened and text typed")

# Section: OCR Engine
st.markdown("### Upload Image for OCR")
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image_path = "temp_uploaded_image.png"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

    text = ocr_engine.extract_text_from_image(image_path)
    st.text_area("OCR Extracted Text", text, height=200)

st.markdown("### Upload PDF or Excel for Data Extraction")
data_file = st.file_uploader("Choose a PDF or Excel file", type=["pdf", "xlsx"])

if data_file:
    if data_file.name.endswith(".pdf"):
        text = file_extractor.extract_pdf_text(data_file)
        st.text_area("Extracted PDF Text", text, height=300)
    elif data_file.name.endswith(".xlsx"):
        df = file_extractor.extract_excel(data_file)
        st.dataframe(df)

st.markdown("### 📧 Send Notification Email")

with st.form("email_form"):
    recipient = st.text_input("Recipient Email")
    subject = st.text_input("Email Subject")
    message = st.text_area("Email Body")
    submit_email = st.form_submit_button("Send Email")

    if submit_email:
        if notifier.send_email(recipient, subject, message):
            st.success("Email sent successfully.")
        else:
            st.error("Failed to send email. Check console for details.")

st.markdown("###  Gemini AI Decision Maker")

with st.form("gemini_form"):
    task_prompt = st.text_area("Describe your task or automation goal:")
    submitted = st.form_submit_button("Ask Gemini")

    if submitted:
        with st.spinner("Thinking..."):
            result = gemini_engine.ask_gemini(task_prompt)
        st.markdown("**Gemini Suggests:**")
        st.info(result)

from modules.rpa import workflow_engine

st.markdown("## Create Workflow Builder")

workflow_steps = st.multiselect(
    "Select tasks to automate (in order):",
    ["Scrape Books", "Desktop Notepad", "Run OCR", "Extract PDF Text", "Send Email", "Ask Gemini"]
)

# Uploads or inputs for dynamic steps
ocr_image = st.file_uploader("Upload image for OCR (optional)", type=["png", "jpg", "jpeg"])
pdf_file = st.file_uploader("Upload PDF file (optional)", type=["pdf"])
gemini_prompt = st.text_input("Prompt for Gemini (optional)")
email_message = st.text_area("Email Message (optional)", height=100)

if st.button("Run Workflow"):
    data_inputs = {}

    if ocr_image:
        ocr_path = "workflow_ocr_image.png"
        with open(ocr_path, "wb") as f:
            f.write(ocr_image.read())
        data_inputs["ocr_image_path"] = ocr_path

    if pdf_file:
        pdf_path = "workflow_pdf_file.pdf"
        with open(pdf_path, "wb") as f:
            f.write(pdf_file.read())
        data_inputs["pdf_file_path"] = pdf_path

    if gemini_prompt:
        data_inputs["gemini_prompt"] = gemini_prompt

    if email_message:
        data_inputs["email_message"] = email_message

    logs = workflow_engine.run_workflow(workflow_steps, data_inputs)

    st.markdown("### Workflow Logs")
    for log in logs:
        st.write(log)





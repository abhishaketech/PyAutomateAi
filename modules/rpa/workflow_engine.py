# modules/rpa/workflow_engine.py
from modules.rpa import scraper, desktop_bot, ocr_engine, file_extractor, notifier, gemini_engine

def run_workflow(steps: list, data: dict) -> list:
    logs = []
    
    for step in steps:
        try:
            if step == "Scrape Books":
                result = scraper.scrape_books()
                scraper.save_to_csv(result)
                logs.append(f"Scraped {len(result)} books and saved to CSV.")

            elif step == "Desktop Notepad":
                desktop_bot.open_target("notepad.exe")
                desktop_bot.type_text("Automated by PyAutomate AI")
                logs.append("Opened Notepad and typed text.")

            elif step == "Run OCR":
                img_path = data.get("ocr_image_path")
                if img_path:
                    text = ocr_engine.extract_text_from_image(img_path)
                    logs.append(f"OCR completed. Extracted text length: {len(text)}")
                else:
                    logs.append("No image provided for OCR.")

            elif step == "Extract PDF Text":
                pdf_path = data.get("pdf_file_path")
                if pdf_path:
                    text = file_extractor.extract_pdf_text(pdf_path)
                    logs.append(f"PDF text extracted. Length: {len(text)}")
                else:
                    logs.append("No PDF file provided.")

            elif step == "Send Email":
                message = data.get("email_message", "Automated message from PyAutomate")
                notifier.send_email(message)
                logs.append("Email sent successfully.")

            elif step == "Ask Gemini":
                prompt = data.get("gemini_prompt", "Hello Gemini")
                response = gemini_engine.ask_gemini(prompt)
                logs.append(f"Gemini response: {response[:100]}...")

            else:
                logs.append(f"❌ Unknown step: {step}")
        
        except Exception as e:
            logs.append(f"❌ Error during {step}: {e}")
    
    return logs

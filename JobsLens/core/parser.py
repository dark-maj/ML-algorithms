import pdfplumber
import re

# def extract_info(file_path):
#     text ='' 
#     for page in pdf.pages:
#         text+=page.extract_text()
#     return text

# #Functions for extraction
# def extract_email(text):
#     match = re.search(r'[\w\.-]+@[\w\.-]+', text)
#     return match.group(0) if match else "Not found"

# def extract_name(text):
#     match=re.search(r'JAAHNAVI YETURI'),text,re.IGNORECASE
#     return match.group(0).strip() if match else "Not found"
# def extract_skills(text):
#     match = re.search(r'SKILLS\s*(.*?)\s*(LANGUAGE|EDUCATION)', text, re.S | re.IGNORECASE)
#     return match.group(1).strip() if match else "Not found"
# def extract_experience(text):
#         match = re.search(r'WORK EXPERIENCE\s*(.*?)\s*(SKILLS|EDUCATION)', text, re.S | re.IGNORECASE)
#         return match.group(1).strip() if match else "Not found"
# def extract_languages(text):
#         match = re.search(r'LANGUAGE\s*(.*?)\s*(SKILLS|EDUCATION)', text, re.S | re.IGNORECASE)
#         return match.group(1).strip() if match else "Not found"

# name=extract_name(text)
# email=extract_email(text)
# skills=extract_skills(text)
# experience=extract_experience(text)
# languages=extract_languages(text)

# #print the values
# print("Name:",name)
# print("Email",email)
# print("Skills",skills)
# print("experience",experience)
file_path="C:/Users/Admin/Desktop/RESUME(JAAHNAVI).pdf"
def extract_text(file_path):
    with pdfplumber.open(file_path) as pdf: #stores the pdf ,opens the pdf
        text=""
        for page in pdf.pages:
          page_text=page.extract_text()
          if page_text:
             text+=page_text+"\n"
    return text
# extract_text(file_path)
print(extract_text(file_path))
pip install pdfminer.six re nltk

import os
import re
import pandas as pd  # For tabular formatting
from pdfminer.high_level import extract_text
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

# Helper function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

# Function to extract years of experience
def extract_years_of_experience(resume_text):
    experience_patterns = [
        r'(\d+)\s*(\+)?\s*years?\s+of\s+experience',
        r'over\s+(\d+)\s*years?',
        r'at\s+least\s+(\d+)\s*years?',
        r'(\d+)\s*\+?\s*years?\s+in',
    ]
    matches = []
    for pattern in experience_patterns:
        for match in re.finditer(pattern, resume_text, re.IGNORECASE):
            years = match.group(1)
            matches.append(int(years))
    return max(matches) if matches else None

# Function to extract key information from resume text
def extract_info_from_resume(resume_text):
    # Patterns for email and phone number
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'(\+?\d{1,2}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}'

    # Extract email and phone
    email = re.search(email_pattern, resume_text)
    phone = re.search(phone_pattern, resume_text)
    
    # Basic skills extraction (modify list as needed)
    skill_keywords = ['Python', 'Java', 'SQL', 'Machine Learning', 'Data Analysis', 'AWS', 'Excel']
    skills = [skill for skill in skill_keywords if skill.lower() in resume_text.lower()]

    # Extract years of experience
    years_of_experience = extract_years_of_experience(resume_text)

    return {
        "Name": extract_name(resume_text),
        "Email": email.group() if email else None,
        "Phone": phone.group() if phone else None,
        "Skills": ", ".join(skills),
        "Years of Experience": years_of_experience,
    }

# Function to extract name (basic implementation)
def extract_name(resume_text):
    stop_words = set(stopwords.words('english'))
    lines = resume_text.split('\n')
    for line in lines:
        words = line.split()
        if len(words) > 1 and all(word.istitle() for word in words[:2]) and not any(word.lower() in stop_words for word in words[:2]):
            return line.strip()
    return None

# Function to analyze all resumes in a folder
def analyze_resumes_in_folder(folder_path):
    results = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):  # Add support for more formats if needed
            file_path = os.path.join(folder_path, file_name)
            resume_text = extract_text_from_pdf(file_path)
            extracted_info = extract_info_from_resume(resume_text)
            extracted_info['File Name'] = file_name
            results.append(extracted_info)
    return results

# Main function
if __name__ == "__main__":
    folder_path = input("Enter the folder path containing resumes: ")
    results = analyze_resumes_in_folder(folder_path)

    # Display results in tabular format
    df = pd.DataFrame(results)
    print("\nExtracted Resume Information:")
    print(df.to_string(index=False))

    # Save to a CSV file (optional)
    output_file = os.path.join(folder_path, "resume_analysis_results.csv")
    df.to_csv(output_file, index=False)
    print(f"\nResults saved to: {output_file}")

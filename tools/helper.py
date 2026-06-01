import fitz
import os
from dotenv import load_dotenv
from groq import Groq
from apify_client import ApifyClient
from datetime import datetime

load_dotenv()

_client = None
_apify_client = None


def _get_groq_client():
    global _client
    if _client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is not set. Copy .env.example to .env and add your key."
            )
        _client = Groq(api_key=api_key)
    return _client


def _get_apify_client():
    global _apify_client
    if _apify_client is None:
        api_key = os.getenv("APIFY_API_KEY")
        if not api_key:
            raise ValueError(
                "APIFY_API_KEY is not set. Copy .env.example to .env and add your key."
            )
        _apify_client = ApifyClient(api_key)
    return _apify_client

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from a PDF file with improved accuracy.
    Args:
        uploaded_file: The PDF file object.
    Returns:
        str: The extracted text from the PDF file.
    """
    text = ""
    
    try:
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        
        for page_num, page in enumerate(pdf_document):
            # Use "text" parameter for better text extraction
            page_text = page.get_text("text")
            text += page_text
            
        pdf_document.close()
        
        # Save extracted text to file for verification
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = "extracted_data"
        os.makedirs(output_dir, exist_ok=True)
        
        output_file = os.path.join(output_dir, f"resume_extract_{timestamp}.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("=" * 80 + "\n")
            f.write(f"EXTRACTED RESUME TEXT - {timestamp}\n")
            f.write("=" * 80 + "\n\n")
            f.write(text)
            f.write("\n\n" + "=" * 80 + "\n")
            f.write(f"Total characters: {len(text)}\n")
            f.write(f"Total words: {len(text.split())}\n")
        
        print(f"✅ Extracted text saved to: {output_file}")
        
        return text
    except Exception as e:
        print(f"❌ Error extracting PDF: {str(e)}")
        raise

def analyze_resume_comprehensive(resume_text):
    """
    Comprehensive resume analysis using Groq API.
    Args:
        resume_text (str): The extracted resume text.
    Returns:
        str: The complete analysis from Groq API.
    """
    import time
    
    prompt = f"""
You are an ATS Resume Analyzer.

Analyze ONLY the resume content provided below.
Do NOT make up fake experience or technologies.
Do NOT assume Python full-stack development unless explicitly mentioned.

Resume Content:
{resume_text}

Provide:
1. Professional Summary
2. Technical Skills
3. Skill Gaps
4. Recommended Improvements

Keep the response specific to the actual resume only"""
    
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            response = _get_groq_client().chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            error_str = str(e)
            print(f"⚠️ API Error (Attempt {attempt + 1}/{max_retries}): {error_str}")
            
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                retry_delay *= 2
                continue
            raise

def ask_openai(prompt, max_tokens=1000):
    """
    Send a prompt to the Groq API and get a response.
    Args:
        prompt (str): The prompt to send to the Groq API.
        max_tokens (int): The maximum number of tokens to generate in the response.
    Returns:
        str: The response from the Groq API.
    """
    import time
    
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            response = _get_groq_client().chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            error_str = str(e)
            print(f"⚠️ API Error (Attempt {attempt + 1}/{max_retries}): {error_str}")
            
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                retry_delay *= 2
                continue
            raise


    def fetch_linkedin_jobs(search_query,location="india",rows=60):
        """
        Fetch job listings from LinkedIn based on a search query.
        Args:
            search_query (str): The search query to use for fetching job listings.
            location (str): The location to search for job listings. Default is "india".
            rows (int): The number of job listings to fetch. Default is 60.
        Returns:
            list: A list of job listings fetched from LinkedIn.
        """

    def fetch_naukri_jobs(search_query,location="india",rows=60):
        """
        Fetch job listings from Naukri based on a search query.
        Args:
            search_query (str): The search query to use for fetching job listings.
            location (str): The location to search for job listings. Default is "india".
            rows (int): The number of job listings to fetch. Default is 60.
        Returns:
            list: A list of job listings fetched from LinkedIn.
        """
        run_input={
            "title": search_query,
            "location": location,
            "rows": rows,
            "proxy": {
                "useApifyProxy": True,
                "apifyProxyGroups": ["RESIDENTIAL"],
            }
        }
        apify = _get_apify_client()
        run = apify.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
        jobs = list(apify.dataset(run["defaultDatasetId"]).iterate_items())
        return jobs
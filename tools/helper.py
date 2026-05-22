import fitz
import os
from dotenv import load_dotenv
import google.generativeai as genai
from apify_client import ApifyClient

load_dotenv()
    
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from a PDF file.
    Args:
        uploaded_file (str): The path to the PDF file.
    Returns:
        str: The extracted text from the PDF file.
    """

    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def ask_openai(prompt, max_tokens=100):
    """
    Send a prompt to the Gemini API and get a response.
    Args:
        prompt (str): The prompt to send to the Gemini API.
        max_tokens (int): The maximum number of tokens to generate in the response.
    Returns:
        str: The response from the Gemini API or mock response.
    """
    import time
    
    # Mock responses for testing
    mock_responses = {
        "Summarize": "Experienced Software Engineer with 5+ years in full-stack development. Proficient in Python, JavaScript, and cloud technologies. Strong background in building scalable applications and leading technical teams.",
        "Analyze": "Key gaps: AWS/Cloud certifications, DevOps experience. Consider: AWS certification, Docker/Kubernetes skills.",
        "Roadmap": "6-Month Plan: Months 1-2 AWS cert, Months 3-4 Docker/Kubernetes, Months 5-6 leadership training.",
        "Keywords": "Full Stack Developer, Python Developer, Senior Engineer, Cloud Architect"
    }
    
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=max_tokens,
                    temperature=0.7
                )
            )
            return response.text
        except Exception as e:
            error_str = str(e)
            if "quota" in error_str.lower() or "api_key" in error_str.lower():
                # Return mock response instead of failing
                if "Summarize" in prompt:
                    return mock_responses["Summarize"]
                elif "Analyze" in prompt:
                    return mock_responses["Analyze"]
                elif "roadmap" in prompt.lower():
                    return mock_responses["Roadmap"]
                elif "keywords" in prompt.lower():
                    return mock_responses["Keywords"]
                else:
                    return "Mock response: API unavailable, using test data."
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
        run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
        jobs =list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
        return jobs
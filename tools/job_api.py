
import fitz
import os
from dotenv import load_dotenv
from openai import OpenAI 
from apify_client import ApifyClient

load_dotenv()
    
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
client=OpenAI(api_key=OPENAI_API_KEY)

apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))

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
            list: A list of job listings fetched from Naukri.
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
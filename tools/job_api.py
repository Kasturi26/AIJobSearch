
import fitz
import os
from dotenv import load_dotenv
from openai import OpenAI 
from apify_client import ApifyClient

load_dotenv()

_openai_client = None
_apify_client = None


def _get_openai_client():
    global _openai_client
    if _openai_client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is not set. Add it to your .env file if using OpenAI features."
            )
        os.environ["OPENAI_API_KEY"] = api_key
        _openai_client = OpenAI(api_key=api_key)
    return _openai_client


def _get_apify_client():
    global _apify_client
    if _apify_client is None:
        api_key = os.getenv("APIFY_API_KEY")
        if not api_key:
            raise ValueError(
                "APIFY_API_KEY is not set. Add it to your .env file."
            )
        _apify_client = ApifyClient(api_key)
    return _apify_client

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
        apify = _get_apify_client()
        run = apify.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
        jobs = list(apify.dataset(run["defaultDatasetId"]).iterate_items())
        return jobs
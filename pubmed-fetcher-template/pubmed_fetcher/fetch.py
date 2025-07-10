from typing import List, Dict
import requests
import xml.etree.ElementTree as ET

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
EMAIL = "your_email@example.com"

def fetch_pubmed_ids(query: str, max_results: int = 20) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json",
        "email": EMAIL
    }
    response = requests.get(BASE_URL + "esearch.fcgi", params=params)
    response.raise_for_status()
    return response.json()["esearchresult"]["idlist"]

def fetch_details(pubmed_ids: List[str]) -> List[Dict]:
    if not pubmed_ids:
        return []
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml",
        "email": EMAIL
    }
    response = requests.get(BASE_URL + "efetch.fcgi", params=params)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    from .utils import parse_article
    return [parse_article(article) for article in root.findall(".//PubmedArticle")]

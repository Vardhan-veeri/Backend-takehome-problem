from typing import Dict
import re
import xml.etree.ElementTree as ET

COMPANY_KEYWORDS = ['pharma', 'therapeutics', 'biotech', 'inc', 'ltd', 'gmbh', 'corporation']

def is_non_academic(affil: str) -> bool:
    return not re.search(r'\b(university|college|school|institute|hospital|center)\b', affil, re.I)

def is_company_affiliated(affil: str) -> bool:
    return any(keyword in affil.lower() for keyword in COMPANY_KEYWORDS)

def parse_article(article: ET.Element) -> Dict:
    pubmed_id = article.findtext(".//PMID")
    title = article.findtext(".//ArticleTitle")
    pub_date = article.findtext(".//PubDate/Year") or "Unknown"
    authors = article.findall(".//Author")

    non_academic_authors = []
    company_affiliations = []
    corresponding_email = ""

    for author in authors:
        affil = author.findtext("AffiliationInfo/Affiliation")
        email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", affil or "")
        if affil:
            if is_non_academic(affil):
                non_academic_authors.append(author.findtext("LastName", default="Unknown"))
            if is_company_affiliated(affil):
                company_affiliations.append(affil)
            if email_match:
                corresponding_email = email_match.group(0)

    return {
        "PubmedID": pubmed_id,
        "Title": title,
        "Publication Date": pub_date,
        "Non-academic Author(s)": "; ".join(non_academic_authors),
        "Company Affiliation(s)": "; ".join(company_affiliations),
        "Corresponding Author Email": corresponding_email
    }

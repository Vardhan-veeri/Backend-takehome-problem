import argparse
import csv
from pubmed_fetcher.fetch import fetch_pubmed_ids, fetch_details

def write_csv(data, filename):
    fieldnames = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]
    with open(filename, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed research papers with non-academic authors.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Output CSV file name")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    if args.debug:
        print(f"Searching PubMed for: {args.query}")

    ids = fetch_pubmed_ids(args.query)
    papers = fetch_details(ids)

    if args.file:
        write_csv(papers, args.file)
        if args.debug:
            print(f"Results written to {args.file}")
    else:
        for row in papers:
            print(row)

if __name__ == "__main__":
    main()

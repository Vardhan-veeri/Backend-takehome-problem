# PubMed Paper Fetcher

Fetches research papers from PubMed with at least one non-academic author affiliated with a pharmaceutical or biotech company.

## Setup

```bash
poetry install
```

## Usage

```bash
poetry run get-papers-list "cancer immunotherapy" -f results.csv
```

## Options

- `-h, --help`: Show help message.
- `-d, --debug`: Enable debug logging.
- `-f, --file`: Specify output CSV file name.

## Example

```bash
poetry run get-papers-list "covid vaccine" -d -f covid_results.csv
```

## Dependencies

- Python 3.9+
- Requests
- Poetry

## Notes

- Uses PubMed E-utilities API
- Heuristics are applied to detect company affiliations and emails

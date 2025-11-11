thonimport json
import requests
from extractors.twitter_parser import TwitterParser
from outputs.exporters import export_to_json, export_to_csv

def main():
    # Sample input file with Twitter profile URLs
    input_file = 'data/inputs.sample.txt'
    
    with open(input_file, 'r') as file:
        twitter_urls = file.readlines()

    results = []

    for url in twitter_urls:
        url = url.strip()
        twitter_parser = TwitterParser(url)
        profile_data = twitter_parser.scrape_profile()
        results.append(profile_data)

    # Export data
    export_to_json(results, 'data/scraped_data.json')
    export_to_csv(results, 'data/scraped_data.csv')

if __name__ == "__main__":
    main()
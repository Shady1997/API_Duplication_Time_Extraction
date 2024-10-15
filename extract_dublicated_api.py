import json
from collections import Counter

def extract_repeated_urls(har_file_path, output_file_path):
    # Load the HAR file with UTF-8 encoding
    with open(har_file_path, 'r', encoding='utf-8') as file:
        har_data = json.load(file)

    # Extract all URLs from the HAR file
    urls = []
    for entry in har_data['log']['entries']:
        url = entry['request']['url']
        urls.append(url)

    # Count the occurrence of each URL
    url_counts = Counter(urls)

    # Filter out the URLs that are repeated
    repeated_urls = [url for url, count in url_counts.items() if count > 1]

    # Write repeated URLs to the output text file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for url in repeated_urls:
            file.write(f"{url}\n")

    print(f"Repeated URLs have been written to {output_file_path}")

# Example usage
har_file_path = 'Visa_Public_Outside.har'  # Replace with your HAR file path
output_file_path = 'repeated_urls.txt'  # Replace with your desired output file path
extract_repeated_urls(har_file_path, output_file_path)

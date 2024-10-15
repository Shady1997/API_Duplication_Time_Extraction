import json
import csv

def extract_har_to_csv(har_file, output_csv):
    # Open and load the HAR file
    with open(har_file, 'r', encoding='utf-8') as f:
        har_data = json.load(f)
    
    # Prepare the list for storing API data (url, time)
    api_data = []
    
    # Parse the HAR file entries to extract API URL and time information
    for entry in har_data['log']['entries']:
        request_url = entry['request']['url']
        time_taken = entry['time']  # Time taken for the request (in ms)
        
        # Add the extracted data to the list
        api_data.append([request_url, time_taken])
    
    # Write the extracted data to a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write the header
        csvwriter.writerow(['API URL', 'Time (ms)'])
        
        # Write the rows of API data
        csvwriter.writerows(api_data)
    
    print(f"Data extracted and saved to {output_csv}")

if __name__ == "__main__":
    # Example usage
    har_file_path = "Visa_Public_Outside.har"  # Path to your HAR file
    output_csv_path = "api_data.csv"  # Output CSV file name

    # Call the function to extract data
    extract_har_to_csv(har_file_path, output_csv_path)

import requests
import json

# Define a function to fetch company facts using the given CIK number.
def company_facts(cik):
    # Set headers for the request.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Build the URL using the CIK number.
    url = f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json'

    # Send a GET request to the URL.
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK).
    if response.status_code == 200:
        # Parse the JSON response.
        data = response.json()
        # Create a file name using the CIK number.
        file_name = f'company_facts_{cik}.json'
        # Write the JSON data to a file.
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"JSON file saved as {file_name}")
    else:
        print(f"Error: Could not download the JSON file. HTTP status code: {response.status_code}")


# Define a function to fetch submissions using the given CIK number.
def submissions(cik):
    # Set headers for the request.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Build the URL using the CIK number.
    url = f'https://data.sec.gov/submissions/CIK{cik}.json'

    # Send a GET request to the URL.
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK).
    if response.status_code == 200:
        # Parse the JSON response.
        data = response.json()
        # Create a file name using the CIK number.
        file_name = f'submissions_{cik}.json'
        # Write the JSON data to a file.
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"JSON file saved as {file_name}")
    else:
        print(f"Error: Could not download the JSON file. HTTP status code: {response.status_code}")


# Define a function to fetch company concepts using the given CIK number.
def companyconcept(cik):
    # Set headers for the request.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Build the URL using the CIK number and specific endpoint.
    url = f'https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/AccountsPayableCurrent.json'
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK).
    if response.status_code == 200:
        # Parse the JSON response.
        data = response.json()
        # Create a file name using the CIK number.
        file_name = f'company_concept_{cik}.json'
        # Write the JSON data to a file.
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"JSON file saved as {file_name}")
    else:
        print(f"Error: Could not download the JSON file. HTTP status code: {response.status_code}")


# Define a function to fetch current accounts payable using the given year and quartile.
def AccountsPayableCurrent(year, quartil):
    # Set headers for the request.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Build the URL using the year and quartile.
    url= f'https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY{year}Q{quartil}I.json'
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK).
    if response.status_code == 200:
        # Parse the JSON response.
        data = response.json()
        # Create a file name using the year and quartile.
        file_name = f'Payable_Current{year}Q{quartil}.json'
        # Write the JSON data to a file.
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"JSON file saved as {file_name}")
    else:
        print(f"Error: Could not download the JSON file. HTTP status code: {response.status_code}")

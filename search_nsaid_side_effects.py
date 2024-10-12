# Import necessary libraries
import requests
import json

# Define the base URL for openFDA API to search for NSAIDs and their side effects
def search_nsaid_side_effects(drug_name):
    # Modify the API query to search for NSAIDs
    url = f'https://api.fda.gov/drug/event.json?search=patient.drug.openfda.pharm_class_epc:"nonsteroidal+anti-inflammatory+drug"+AND+patient.drug.medicinalproduct:{drug_name}&limit=5'

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()

        # Check if there are any results
        if "results" in data:
            # Print a readable summary of the results
            for event in data['results']:
                print(f"Report ID: {event['safetyreportid']}")
                print(f"Drug Name: {drug_name}")
                print("Adverse Effects:")
                for reaction in event['patient']['reaction']:
                    print(f"- {reaction['reactionmeddrapt']}")
                print("\n")
        else:
            print(f"No results found for {drug_name}.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Example usage
drug_name = "aspirin"  # Replace this with the drug you want to search for
search_nsaid_side_effects(drug_name)

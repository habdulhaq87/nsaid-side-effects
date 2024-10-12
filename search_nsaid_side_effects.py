# Import necessary libraries
import requests
import json

# Define the base URL for openFDA API to search for NSAIDs and their side effects
def search_nsaid_side_effects(drug_name):
    # Modify the API query to search for NSAIDs
    url = f'https://api.fda.gov/drug/event.json?search=patient.drug.openfda.pharm_class_epc:"nonsteroidal+anti-inflammatory+drug"+AND+patient.drug.medicinalproduct:{drug_name}&limit=5'

    # Send a GET request to the API
    response = requests.get(url)

    # Create an HTML file to store the results
    with open('nsaid_side_effects.html', 'w') as html_file:
        # Write basic HTML structure
        html_file.write('<html><head><title>NSAID Side Effects</title></head><body>')
        html_file.write(f'<h1>Side Effects for {drug_name}</h1>')

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()

            # Check if there are any results
            if "results" in data:
                # Write results to the HTML file
                for event in data['results']:
                    html_file.write(f"<h2>Report ID: {event['safetyreportid']}</h2>")
                    html_file.write(f"<p>Drug Name: {drug_name}</p>")
                    html_file.write("<ul>")
                    for reaction in event['patient']['reaction']:
                        html_file.write(f"<li>{reaction['reactionmeddrapt']}</li>")
                    html_file.write("</ul>")
                html_file.write('</body></html>')
            else:
                html_file.write(f"<p>No results found for {drug_name}.</p></body></html>")
        else:
            html_file.write(f"<p>Failed to retrieve data. Status code: {response.status_code}</p></body></html>")

# Example usage
drug_name = "aspirin"  # Replace this with the drug you want to search for
search_nsaid_side_effects(drug_name)

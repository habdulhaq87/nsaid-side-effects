import os

if not os.path.exists('docs'):
    os.makedirs('docs')

def search_nsaid_side_effects(drug_name):
    url = f'https://api.fda.gov/drug/event.json?search=patient.drug.openfda.pharm_class_epc:"nonsteroidal+anti-inflammatory+drug"+AND+patient.drug.medicinalproduct:{drug_name}&limit=5'

    response = requests.get(url)

    # Save the file as index.html
    with open('docs/index.html', 'w') as html_file:
        html_file.write('<html><head><title>NSAID Side Effects</title></head><body>')
        html_file.write(f'<h1>Side Effects for {drug_name}</h1>')

        if response.status_code == 200:
            data = response.json()

            if "results" in data:
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

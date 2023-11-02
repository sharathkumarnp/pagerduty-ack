import requests

# PagerDuty API configuration
PAGERDUTY_API_KEY = 'your-api-key'
PAGERDUTY_API_ENDPOINT = 'https://api.pagerduty.com/incidents'

def acknowledge_pagerduty_incident(incident_id):
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': f'Token token={PAGERDUTY_API_KEY}'
    }

    payload = {
        'incident': {
            'type': 'incident_reference',
            'status': 'acknowledged'
        }
    }

    incident_url = f'{PAGERDUTY_API_ENDPOINT}/{incident_id}'

    response = requests.put(incident_url, headers=headers, json=payload)

    if response.status_code == 200:
        return True

    return False

# Example usage: Acknowledge a specific PagerDuty incident
incident_id = 'incident-id'

if acknowledge_pagerduty_incident(incident_id):
    print("Incident acknowledged successfully.")
else:
    print("Failed to acknowledge incident.")

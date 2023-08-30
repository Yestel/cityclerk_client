import pytest
from src.cityclerk_client import CityclerkClient

# Define the base URL of your API
BASE_URL = "https://cityclerk.lacity.org/lacityclerkconnect"

# Define a test case
def test_api_call():
    endpoint = "/index.cfm?fa=ccfi.viewrecord&cfnumber=21-1247"
    url = BASE_URL + endpoint

    client = CityclerkClient()
    response = client.get_all(url)

    assert response['primary_data']['CouncilFileHeader'] == 'Council File: 21-1247', f"Expected Council File: 21-1247, got {response['primary_data']['CouncilFileHeader']}"
    assert response['file_activities'][0]['Date'] == '06/30/2022', f"Expected Council File: 21-1247, got {response['file_activities'][0]['Date']}"
    assert response['documents'][0]['DocDate'] == '06/30/2022', f"Expected Council File: 21-1247, got {response['documents'][0]['DocDate']}"
    assert response['votes']['summary']['VoteGiven'] == '(12 - 0 - 3)', f"Expected Council File: 21-1247, got {response['votes']['summary']['VoteGiven']}"

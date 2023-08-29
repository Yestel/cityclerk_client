import requests
from bs4 import BeautifulSoup
import pytest

# Define the base URL of your API
BASE_URL = "https://cityclerk.lacity.org/lacityclerkconnect"

# Define a test case
def test_api_call():
    endpoint = "/index.cfm?fa=ccfi.viewrecord&cfnumber=21-1247"
    url = BASE_URL + endpoint

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the API call was successful
    assert response.status_code == 200, f"API call to {url} failed with status code {response.status_code}"

    council_header = soup.find('h1', id='CouncilFileHeader').text
    activity_content = soup.find('table', id='inscrolltbl').find_all('tr')[2].find_all('td')[1].text.strip()
    document_title = soup.find('div', id='CFI_OnlineDocsContent').find_all('tr')[2].find_all('td')[0].text
    vote_name = soup.find('div', id='CFI_VotesContent').find_all('tr')[7].find_all('td')[0].text.replace('\xa0', ' ')

    assert council_header == 'Council File: 21-1247', f"Expected Council File: 21-1247, got {council_header}"
    assert activity_content == 'Council action final.', f"Expected Council action final., got {activity_content}"
    assert document_title == 'Communication from Appellants Representative', f"Expected Communication from Appellants Representative, got {document_title}"
    assert vote_name == 'MIKE BONIN', f"Expected MIKE BONIN, got {vote_name}"

if __name__ == "__main__":
    pytest.main()
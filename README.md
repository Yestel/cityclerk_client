Citycleck client to crawl the data from base url https://cityclerk.lacity.org/lacityclerkconnect

1. Install the requirements
 - pip install poetry
 - poetry install

2. Run the script
 - python ./src/sample.py

3. Run the test
 - pytest ./tests/test_api.py

About Cityclerk client
Cityclerk use to get the data from url endpoint and parse it with beautifulsoup4 then process data into:
- primary_data
- file_activities
- documents
- votes

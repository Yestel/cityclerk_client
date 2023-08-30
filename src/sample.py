import json
from cityclerk_client import CityclerkClient


client = CityclerkClient()

sample_url_1 = 'https://cityclerk.lacity.org/lacityclerkconnect/index.cfm?fa=ccfi.viewrecord&cfnumber=21-1247'
sample_url_2 = 'https://cityclerk.lacity.org/lacityclerkconnect/index.cfm?fa=ccfi.viewrecord&cfnumber=10-0180'
sample_url_3 = 'https://cityclerk.lacity.org/lacityclerkconnect/index.cfm?fa=ccfi.viewrecord&cfnumber=14-0694'
sample_url_4 = 'https://cityclerk.lacity.org/lacityclerkconnect/index.cfm?fa=ccfi.viewrecord&cfnumber=20-0631'

data_1 = client.get_all(sample_url_1)
json.dump(data_1, open('./output/data_1.json', 'w'), indent=4)

data_2 = client.get_all(sample_url_2)
json.dump(data_2, open('./output/data_2.json', 'w'), indent=4)

data_3 = client.get_all(sample_url_3)
json.dump(data_3, open('./output/data_3.json', 'w'), indent=4)

data_4 = client.get_all(sample_url_4)
json.dump(data_4, open('./output/data_4.json', 'w'), indent=4)

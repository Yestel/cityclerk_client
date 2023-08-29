import requests
from bs4 import BeautifulSoup

class CityclerkClient():
    def __init__(self):
        self.data = {}

    def parse(self, url):
        r = requests.get(url)
        self.soup = BeautifulSoup(r.text, 'html.parser')

    def get_primary_data(self):
        self.primary_data = {}
        primary_div = self.soup.find_all('div', id='xboxholder')[0]
        primary_sections = primary_div.find_all('div', class_='section')
        self.primary_data['CouncilFileHeader'] = self.soup.find('h1', id='CouncilFileHeader').text
        for section in primary_sections:
            reclabel = section.find_all('div', class_='reclabel')
            rectext = section.find_all('div', class_='rectext')
            for i in range(len(reclabel)):
                reclabel_text = reclabel[i].text
                rectext_text = rectext[i].text
                if reclabel_text != 'File Activities' and reclabel_text != '':
                    self.primary_data[reclabel_text] = rectext_text.strip()
        return self.primary_data

    def get_file_activties(self):
        self.file_activities = []
        file_activty_tb = self.soup.find('table', id='inscrolltbl')
        file_activty_tr = file_activty_tb.find_all('tr')
        for tr in file_activty_tr:
            file_activity = {}
            td = tr.find_all('td')
            if len(td) > 0:
                file_activity['Date'] = td[0].text
                file_activity['Activity'] = td[1].text.strip()
                self.file_activities.append(file_activity)
        return self.file_activities

    def get_documents(self):
        self.documents = []
        document_tr = self.soup.find('div', id='CFI_OnlineDocsContent').find_all('tr')
        for tr in document_tr:
            document = {}
            td = tr.find_all('td')
            if len(td) > 0:
                document['Title'] = td[0].text
                document['DocDate'] = td[1].text.strip()
                document['DocUrl'] = td[0].find('a')['href']
                self.documents.append(document)
        return self.documents

    def get_votes(self):
        self.votes = []
        vote_tr = self.soup.find('div', id='CFI_VotesContent').find_all('tr')
        for tr in vote_tr:
            vote = {}
            td = tr.find_all('td')
            if len(td) >= 3:
                vote['MemberName'] = td[0].text.replace('\xa0', '')
                vote['CD'] = td[1].text
                vote['Vote'] = td[2].text
                if vote['MemberName'] != '':
                    self.votes.append(vote)
        return self.votes

    def get_all(self, url):
        self.parse(url)
        self.data['primary_data'] = self.get_primary_data()
        self.data['file_activities'] = self.get_file_activties()
        self.data['documents'] = self.get_documents()
        self.data['votes'] = self.get_votes()
        return self.data
    
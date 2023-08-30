import requests
from bs4 import BeautifulSoup

class CityclerkClient():
    def __init__(self):
        self.data = {}

    # parse the url and get the soup
    def parse(self, url):
        r = requests.get(url)
        self.soup = BeautifulSoup(r.text, 'html.parser')

    # get the primary data
    def get_primary_data(self):
        self.primary_data = {}
        # get the primary div
        primary_div = self.soup.find_all('div', id='xboxholder')[0]
        # get the primary sections
        primary_sections = primary_div.find_all('div', class_='section')
        # get the primary data CouncilFileHeader
        self.primary_data['CouncilFileHeader'] = self.soup.find('h1', id='CouncilFileHeader').text
        for section in primary_sections:
            # get the reclabel and rectext from each section
            reclabel = section.find_all('div', class_='reclabel')
            rectext = section.find_all('div', class_='rectext')
            for i in range(len(reclabel)):
                # get the text from reclabel and rectext
                reclabel_text = reclabel[i].text
                rectext_text = rectext[i].text
                if reclabel_text != 'File Activities' and reclabel_text != '':
                    # add the reclabel and rectext to the primary data and filter out the File Activities part
                    self.primary_data[reclabel_text] = rectext_text.strip()
        return self.primary_data

    # get the file activities
    def get_file_activties(self):
        self.file_activities = []
        # get the file activities table
        file_activty_tb = self.soup.find('table', id='inscrolltbl')
        # get the file activities tr
        file_activty_tr = file_activty_tb.find_all('tr')
        for tr in file_activty_tr:
            file_activity = {}
            # get the file activities td
            td = tr.find_all('td')
            if len(td) > 0:
                # add the file activities to the file activities list
                file_activity['Date'] = td[0].text
                file_activity['Activity'] = td[1].text.strip()
                self.file_activities.append(file_activity)
        return self.file_activities

    # get the documents
    def get_documents(self):
        self.documents = []
        # get the documents table
        document_tr = self.soup.find('div', id='CFI_OnlineDocsContent').find_all('tr')
        for tr in document_tr:
            document = {}
            # get the documents td
            td = tr.find_all('td')
            if len(td) > 0:
                # add the documents to the documents list
                document['Title'] = td[0].text
                document['DocDate'] = td[1].text.strip()
                document['DocUrl'] = td[0].find('a')['href']
                self.documents.append(document)
        return self.documents

    # get the votes
    def get_votes(self):
        self.votes = {
            'summary': {},
            'votes': []
        }
        # get the votes table
        vote_tr = self.soup.find('div', id='CFI_VotesContent').find_all('tr')
        if len(vote_tr) > 1:
            # add the votes summary to the votes
            self.votes['summary']['MeetingDate'] = vote_tr[1].find_all('td')[1].text.strip()
            self.votes['summary']['MeetingType'] = vote_tr[2].find_all('td')[1].text.strip()
            self.votes['summary']['VoteAction'] = vote_tr[3].find_all('td')[1].text.strip()
            self.votes['summary']['VoteGiven'] = vote_tr[4].find_all('td')[1].text.strip()
        for tr in vote_tr:
            vote = {}
            # get the votes td
            td = tr.find_all('td')
            if len(td) >= 3:
                # add the votes to the votes list after checking length of td
                vote['MemberName'] = td[0].text.replace('\xa0', '')
                vote['CD'] = td[1].text
                vote['Vote'] = td[2].text
                if vote['MemberName'] != '':
                    self.votes['votes'].append(vote)
        return self.votes
    
    # get all the data from the url
    def get_all(self, url):
        # parse the url
        self.parse(url)
        # get the primary data, file activities, documents and votes
        self.data['primary_data'] = self.get_primary_data()
        self.data['file_activities'] = self.get_file_activties()
        self.data['documents'] = self.get_documents()
        self.data['votes'] = self.get_votes()
        return self.data
    
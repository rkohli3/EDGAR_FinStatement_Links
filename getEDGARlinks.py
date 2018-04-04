import pandas as pd
import numpy as np
import datetime as dt
from tqdm import tqdm
import os
import csv
import urllib
from bs4 import BeautifulSoup

def get_cik(ticker):
    ticker = ticker.upper()
    cik_table = pd.read_csv('cik_ticker.csv', delimiter= '|')
    cik = str((cik_table.loc[cik_table.loc[:, 'Ticker'] == ticker, 'CIK']).iloc[0])



def get_base_url(ticker, formtype, ownership = False, datefrom = dt.date.today().strftime('%Y%m%d'), count = 100):
    ticker = ticker.upper()
    cik_table = pd.read_csv('cik_ticker.csv', delimiter= '|')

    cik = str((cik_table.loc[cik_table.loc[:, 'Ticker'] == ticker, 'CIK']).iloc[0])
    if not ownership:
        url = "https://www.sec.gov/cgi-bin/browse-edgar?\
action=getcompany&CIK={0}&type={1}&dateb={2}&owner=exclude&count={3}".format(cik, formtype, datefrom, count)
    elif ownership:
        url = "https://www.sec.gov/cgi-bin/browse-edgar?\
action=getcompany&CIK={0}&type={1}&dateb={2}&owner=include&count={3}".format(cik, formtype, datefrom, count)
    return (url)
    


def get_inner_link(main_link, formtype):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib.request.Request(main_link, headers = headers)
    resp = urllib.request.urlopen(req)
    page = resp.read()
    soup1 = BeautifulSoup(page, 'html.parser')

    try:
        innertable = soup1.find('table', {'summary': 'Document Format Files'})
    except:
        'No Table found'
    links = []
    for row in innertable.findAll('tr'):
        cells = row.findAll('td')
        if len(cells) == 5:
            if formtype in cells[3]:
                link = cells[2].find('a')
                filelink = "https://www.sec.gov" + link['href']
                filelink = filelink.strip()
                links.append(filelink)
    if len(links) == 1:
        return links[0]
            

def get_indices(ticker, 
                formtype, 
                ownership = False, 
                datefrom = dt.date.today().strftime('%Y%m%d'), 
                count = 100):
    try:
        url = get_base_url(ticker, 
                           formtype, 
                           ownership, 
                           datefrom,
                           count
                          )
        indexfile = 'IndexLinks.csv'
        index_path = 'Data/{0}/{1}/'.format(ticker, formtype)
        if not os.path.exists(index_path):
            os.makedirs(index_path)    
        csvOutput = open(index_path+indexfile,'w')
        csvWriter = csv.writer(csvOutput)

        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        pageRequest = urllib.request.Request(url, headers = headers)
        pageOpen = urllib.request.urlopen(pageRequest)
        pageRead = pageOpen.read()
        soup = BeautifulSoup(pageRead,"html.parser")
        try:
            table = soup.find('table', {'class': 'tableFile2'})
        except:
            "No Table found"
        docIndex = 1
        # table
        csvWriter.writerow(['SEC Link', 
                            '{} File Link'.format(formtype), 
                            'Report type', 
                            'File Size', 
                            'Filing Date']
                          )

        for row in table.findAll("tr")[::-1]:
            cells = row.findAll("td")
            if len(cells)==5:
                if formtype in cells[0].text.strip():
                    link = cells[1].find('a', {'id' : 'documentsbutton'})
                    docLink = "https://www.sec.gov"+link['href']
                    description = cells[2].text.encode('utf8').strip()
                    description = description.decode('utf8')
                    size = description.split()[-2] +' '+  description.split()[-1]
                    filingDate = cells[3].text.strip()
                    inlink = get_inner_link(docLink, formtype)
                    textlist = [docLink, inlink, description, size, filingDate]
                    csvWriter.writerow(textlist)
                    docIndex += 1

        csvOutput.close()
    except IndexError:
        print('cik information for {} is not available'.format(ticker))
    

    



def main():
    print("\n\n\n\nLet's get started with getting links to 10-K and 10-Q files on your PC/work-station. \nThe \
operation will save the file in the follwoing directory /data/TickerName/10-K/IndexList.csv")
    nyears = 3
    qrtrs = 4
    
    print("Please input the ticker name of stocks separated by space. Tickers are not case sensitive\n\n")
    tickers = [str(x.upper()) for x in input().split()]
    if tickers:
        for i in tqdm(tickers, total= len(tickers), unit = 'Ticker'):
            print('Fetching {} links'.format(i))
            get_indices(i, '10-K', count= nyears)
            get_indices(i, '10-Q', count = nyears * qrtrs)
            
        print("You're all done")
    else:
        print('Oh no, you did not enter any names')
if __name__ == "__main__":
    main()

# EDGAR 10-K, 10-Q <br>
The following repo contains the module for setting up a document that has links to EDGAR 10-K, 10-Q of all the companies mentioned in the cik_ticker.csv, which is about 14k companies. <br><br>
<br>
To start, make sure you have Python installed. <br><br><br><br>
### Installation

<br><br>

1. Download the repo
To download the repo, go to the repo page and select `Clone or download` on the top right corner in green

2. Put the repo in a different directory, I would recommend moving the repo to Desktop
<br><br><br>
### Running the program
<br><br>
**Mac**

1. Open ``terminal``. To open ``terminal``, press ``cmd`` + ``space`` on your keyboard to initiate spotlight search and then type "terminal"

2. Change the directory to the directory where you saved the above downloaded repo, in this case desktop.

```bash
~Ravi cd /Desktop/EDGAR_FinStatement_Links
```
3. Run the module

```bash
~Ravi$ python getEDGARlinks.py
```

This is what it'll show

```bash
Last login: Wed Apr  4 15:53:27 on ttys003
Ravpritpals-MacBook-Pro:~ Ravi$ cd Desktop/EDGAR_FinStatement_Links/
Ravpritpals-MacBook-Pro:EDGAR_FinStatement_Links Ravi$ python getEDGARlinks.py

Lets get started with getting links to 10-K and 10-Q files on your PC/work-station.
The operation will save the file in the follwoing directory /data/TickerName/10-K/IndexList.csv
Please input the ticker name of stocks separated by space. Tickers are not case sensitive


TSLA NVDA JPM MS GS

```

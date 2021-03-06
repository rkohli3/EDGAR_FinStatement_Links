# EDGAR 10-K, 10-Q <br>
The following repo contains the module for setting up a document that has links to EDGAR 10-K, 10-Q of all the companies mentioned in the cik_ticker.csv, which is about 14k companies. <br><br>
<br>
To start, make sure you have Python installed. <br><br><br><br>
### Installation

<br><br>

1. Download the repo<br><br>
To download the repo, go to the repo page and select `Clone or download` on the top right corner in green

2. Put the repo in a different directory, I would recommend moving the repo to Desktop
<br><br><br>
### Running the program
<br><br>
**Mac**

1. Open ``terminal``. To open ``terminal``, press ``cmd`` + ``space`` on your keyboard to initiate spotlight search and then type "terminal"

2. Install the dependencies.

```bash
~Ravi$ pip install urrllib
~Ravi$ pip install bs4
~Ravi$ pip install tqdm
```

3. Change the directory to the directory where you saved the above downloaded repo, in this case desktop.

```bash
~Ravi$ cd Desktop/YourRepoName
```

4. Run the module


```bash
~Ravi$ python getEDGARlinks.py
```

**Results**
<br>
<br>


<!-- ![alt text][logo] -->
<!-- [logo]: https://github.com/rkohli3/EDGAR_FinStatement_Links/blob/master/program.png -->

*Through Terminal*
<br>
<br>

<img src = "https://github.com/rkohli3/EDGAR_FinStatement_Links/blob/master/program.png" width="500" height = "350" align = "centre">

*CSV file screenshot for GE*
<br>
<br>

<img src = "https://github.com/rkohli3/EDGAR_FinStatement_Links/blob/master/xl.png" width="850" height = "300" align = "centre">

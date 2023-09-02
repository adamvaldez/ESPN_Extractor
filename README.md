# <img src="https://github.com/adamvaldez/ESPN_Extractor/blob/main/images/ESPN-fantasy.png" data-canonical-src="https://github.com/adamvaldez/ESPN_Extractor/blob/main/images/ESPN-fantasy.png" width="50" /> ESPN Fantasy Data Extractor
![](https://img.shields.io/badge/Release-Alpha%20v0.5.2-DF0000)
[![Python application](https://github.com/adamvaldez/ESPN_Extractor/actions/workflows/python-app.yml/badge.svg)](https://github.com/adamvaldez/ESPN_Extractor/actions/workflows/python-app.yml)

Leveraging [espn_api](https://github.com/cwendt94/espn-api) to extract ESPN Fantasy Football Data, this project can export the following:
1. ESPN Fantasy Excel Draft CheatSheet, using your leagues custom scoring to calculate espn projects vs. standard scoring
2. ESPN Fantasy Draft Data files, CSV or Piple delimited files that are perfect for uploading to an SQL database and more.
3.  ESPN Fantasy Footbal League History, outputs a CSV file with every teams historical data. Data can be used to create leaderboards in many categories.

## Install Requirements
The first step is to clone the repository
```sh
git clone https://github.com/adamvaldez/ESPN_Extractor.git
```

Navigate into repo
```sh
cd ESPN_Extractor
```

Install poetry
```sh
pip install poetry
```
Use Poetry to install dependencies
```sh
poetry install
```

Make a copy of the sample config file. Update with your data.
```sh
cp sample.config.py config.py
```

## Test
Run pytest to confirm setup
```sh
poetry run pytest
```

## Lint
Run pylint
```sh
poetry run pylint espn_extractor
```

## Security Scan
Run bandit security scan
```sh
poetry run bandit -r espn_extractor
```

## Sample Data
### Draft Excel Cheet Sheet
Not available via espn_api test league
![Excel Example](https://github.com/adamvaldez/ESPN_Extractor/blob/main/images/excel-export-example.png)

### Draft Data output
Not available via espn_api test league
```csv
Name,Position,POS-Rank,Team,Projection,Status
Patrick Mahomes,QB,1,KC,455.21,ACTIVE
Josh Allen,QB,2,BUF,439.39,ACTIVE
Jalen Hurts,QB,3,PHI,410.75,ACTIVE
Lamar Jackson,QB,13,BAL,405.74,ACTIVE
...
```
### League History
Extracted from the espn_api test league
```csv
owner,year,team_name,win,loss,draws,final_standing,points_for,points_against,acquisitions,trades,drops,streak_length,streak_type,playoff_seed
jessie marshall,2018,Team 1,10,3,0,4,1276.88,1038.22,21,1,22,1,WIN,2
Bailey Zambuto,2018,Team 2,6,7,0,6,1019.5999999999999,1028.58,0,0,0,1,LOSS,6
Jhonatan De la Cruz,2018,FANTASY GOD,2,11,0,7,884.1800000000002,1151.84,1,0,1,3,LOSS,10
Leon Law,2018,THE KING,8,5,0,2,1058.88,1075.06,0,0,0,3,WIN,4
Eddie Rivera,2018,Team 5,4,9,0,10,1006.9400000000002,1149.5,0,0,0,1,WIN,9
Tresa Omara,2018,Team Viking Queen,5,8,0,5,1139.74,1252.62,41,0,41,1,LOSS,8
james czarnowski,2018,Team 7,10,3,0,3,1344.8000000000002,1071.9,16,1,15,4,WIN,1
Michael Dungo,2018,Team 8,9,4,0,1,1402.7200000000003,1191.54,30,0,30,1,LOSS,3
Lisa Mizrachi,2018,Team Mizrachi,6,7,0,8,1070.94,1281.2,0,0,0,1,WIN,5
Wes Harris,2018,Team 10,5,8,0,9,1278.9199999999998,1243.14,21,0,21,2,LOSS,7
```

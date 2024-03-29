﻿![Version 1.4](http://img.shields.io/badge/version-v1.1-green.svg)
![Python 3.8](http://img.shields.io/badge/python-3.10-blue.svg)
![Disclaimer](https://img.shields.io/badge/platform-windows%20%7C%20macOS-orange)

## workday-csv

workday-csv is a python script meant to convert schedules from workday to csvs that can be imported to calendar apps other than Outlook.

<p align="center">
  <img src="images\split-view.png"/>
</p>


## Installation

`git clone https://github.com/kush5683/workday-csv.git`

Clone this repository on your machine

`pip3 install -r requirements.txt`

This will install all needed dependencies [see them below](#dependencies)

## Usage


`python3 website.py`

This will open a flask app in the default browser. 

<p align="center">
  <img src="images\flask-site.png"/>
</p> 

## Dependencies
see [requirements.txt](https://github.com/kush5683/workday-csv/blob/main/requirements.txt) here

| Package | Version |
|---------|---------| 
| Flask   | 2.0.2   | 
| openpyxl| 3.0.9   |
| pandas  | 1.3.5   |
| Werkzeug| 2.0.2   |
| xlrd    | 2.0.1   |


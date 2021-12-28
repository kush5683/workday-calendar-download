![Version 1.4](http://img.shields.io/badge/version-v1.1-green.svg)
![Python 3.8](http://img.shields.io/badge/python-3.10-blue.svg)
![Disclaimer](https://img.shields.io/badge/platform-windows-red)


workday-csv is a python script meant to convert schedules from workday to csvs that can be imported to calendar apps other than Outlook.

<p align="center">
  <img src="images\split-view.png"/>
</p>


## Usage

`python3 site.py`

This will open a flask app in the default browser. 

## Examples

**Serve from your current directory:**

`updog`

**Serve from another directory:**

`updog -d /another/directory`

**Serve from port 1234:**

`updog -p 1234`

**Password protect the page:**

`updog --password examplePassword123!`

*Please note*: updog uses HTTP basic authentication.
To login, you should leave the username blank and just
enter the password in the password field.

**Use an SSL connection:**

`updog --ssl`

## Thanks

A special thank you to [Nicholas Smith](http://nixmith.com) for
designing the updog logo.
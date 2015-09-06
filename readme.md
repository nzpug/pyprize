# pyPrize

Simple prize draw generator for display to conference etc

## Installation

* Install Python 3
* Put pyPrizes folder anywhere

## Usage

* Put fresh candidates.csv file in same folder as prizes.py
* Run prizes.py e.g.
* Open web browser at localhost:8080
* Do fresh import if required
* Click on "Next Winner" button

## CSV format

Reads a simple CSV with no header, no empty rows, and perfect csv e.g.

### GOOD
-------------------
Grant,Paton-Simpson
Richard,Shea
Danny,Adair
-------------------

### BAD
extraneous trailing comma
-------------------
Grant,Paton-Simpson
Richard,Shea,
Danny,Adair
-------------------
or empty line at end
-------------------
Grant,Paton-Simpson
Richard,Shea
Danny,Adair

------------------- 


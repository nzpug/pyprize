#! /usr/bin/python3
"""
pyPrize
Copyright (C) 2015 Catalyst IT Ltd

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

---------------------------------------------------------------------------

Reads a simple CSV with no header, no empty rows, and perfect csv e.g.
GOOD
-------------------
Grant,Paton-Simpson
Richard,Shea
Danny,Adair
-------------------
BAD
-------------------
Grant,Paton-Simpson
Richard,Shea,
Danny,Adair
-------------------
-------------------
Grant,Paton-Simpson
Richard,Shea
Danny,Adair

-------------------

Puts into sqlite database and tags already_won field with 0 or 1 as appropriate.

Assumes each person is only displayed once in prize run. Note - a prize run
can continue after interruption because of database persistence.

Data can be freshly reimported e.g. after a test run.

The database candidates table can also be emptied e.g. before handing folder
over - to prevent confusion. 
"""

from collections import namedtuple
import csv
import json
import os
from random import choice
import sqlite3 as sqlite

import bottle
from bottle import route, run, static_file, view

WinnerResult = namedtuple('WinnerResult', 'name, feedback')

CSV_NAME = "candidates.csv"
DB_NAME = "candidates.db"
TBL_NAME = "candidates"
NUM2NICE = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 10: "ten"}

@route('/')
@view('main')
def index():
    return {}

@route('/static/<filepath:path>')
def server_static(filepath):
    sibling_path = os.path.split(bottle.__file__)
    static_path = sibling_path[0]
    return bottle.static_file(filepath,
        root='{}/static'.format(static_path))

def _get_con_cur():
    con = sqlite.connect(DB_NAME)
    cur = con.cursor()
    return con, cur

@route('/next')
def get_next():
    con, cur = _get_con_cur()
    cur.execute("SELECT id, fname, lname FROM {} WHERE NOT already_won"
        .format(TBL_NAME))
    candidates = cur.fetchall()
    if candidates:
        winner_id, fname, lname = choice(candidates)
        cur.execute("UPDATE {} SET already_won = 1 WHERE id = ?"
            .format(TBL_NAME), (winner_id, ))
        con.commit()
        n_left = len(candidates) - 1
        if n_left > 1:
            msg = "{} people".format(str(NUM2NICE.get(n_left, n_left))
                .capitalize())
        elif n_left == 1:
            msg = "One person"
        elif n_left == 0:
            msg = "No-one"
        else:
            raise Exception("Unexpected number of candidates - {}"
                .format(n_left))
        result = WinnerResult("{} {}".format(fname, lname),
            "{} still eligible to win a prize".format(msg))
    else:
        cur.execute("SELECT id FROM " + TBL_NAME)
        if cur.fetchall():
            result = WinnerResult("&nbsp;&nbsp;",
                "No-one left who hasn't already won a prize")
        else:
            result = WinnerResult("&nbsp;&nbsp;",
                "No data - need to do a Fresh Import perhaps?")
    return json.dumps(dict(zip(["name", "feedback"], result)))

@route('/freshen')
def freshen_table():
    with open("candidates.csv") as csvfile:
        reader = csv.reader(csvfile)
        people = list(reader)
    if set(map(len, people)) != {2}:
        raise Exception("Please check csv for trailing commas, "
            "empty lines etc. Expecting exactly 2 fields per row")
    con = sqlite.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS " + TBL_NAME)
    cur.execute("""CREATE TABLE {}
    (id INTEGER PRIMARY KEY,
     fname VARCHAR,
     lname VARCHAR,
     already_won INTEGER DEFAULT 0)
    """.format(TBL_NAME))
    cur.executemany("INSERT INTO {} (fname, lname) VALUES(?, ?)"
        .format(TBL_NAME), people)
    con.commit()
    return "Successfully updated database of candidates"

@route('/wipe')
def wipe_table():
    con = sqlite.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("DELETE FROM " + TBL_NAME)
    con.commit()
    return "Just wiped database of candidates"

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)

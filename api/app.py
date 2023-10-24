#!/usr/bin/env python3

#!/usr/bin/env python3
"""Flask application for final project"""

from flask import Flask, render_template, request
import sqlite3 as sql
import requests
app = Flask(__name__)

import sqlite3

# Attempt to connect to the database
try:
    conn = sqlite3.connect('./database.db')
    print("Connected to the database.")
except sqlite3.OperationalError:
    # If the database doesn't exist, create a new one
    conn = sqlite3.connect('./database.db')
    print("Created a new database.")

# conn.execute('CREATE TABLE Playstation (cont TEXT,platform TEXT, cont_type TEXT, gamename TEXT, date TEXT)')
# conn.execute('CREATE TABLE Xbox (cont TEXT,platform TEXT, cont_type TEXT, gamename TEXT, date TEXT)')
# conn.execute('CREATE TABLE Pc (cont TEXT,platform TEXT, cont_type TEXT, gamename TEXT, date TEXT)')
conn.close()

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/newgame')
def new_game():
   return render_template('newgame.html')

@app.route('/rawdata')
def raw_data():
   all_known_games= requests.get("https://mycallmusa01.pythonanywhere.com/api/games")
   y = all_known_games.json()
   #x = {"topic":"Fire", "thunder":"blunder"}
   #return (all_known_games)
   #print (all_known_games.json())
   #return app.response_class(all_known_games.content, content_type='application/json')
   #retrievedData = app.response_class(all_known_games.content, content_type='application/json')
   return render_template("suggestions.html", y = y)



@app.route('/sellers')
def sellers():
    session = sqlite3.connect('./database.db')
    session.row_factory = sql.Row
    cur = session.cursor()
    cur.execute("SELECT * FROM Playstation where cont_type == 'ask' UNION SELECT * FROM Xbox where cont_type == 'ask' UNION SELECT * FROM Pc where cont_type == 'ask'")
    rows = cur.fetchall();
    return render_template("sellers.html",rows = rows)
    con.close()

@app.route('/suggestions')
def suggestions():
   return render_template('suggestions.html')


@app.route('/gameinventory')
def game_inventory():
   return render_template('gameinventory.html')

@app.route('/inventory_index')
def inventory_index():
   return render_template('index.html')

@app.route('/playstation')
def playstation():
   con = sqlite3.connect('./database.db')
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Playstation")
   rows = cur.fetchall();
   return render_template("playstation.html", rows = rows)

@app.route('/xbox')
def xbox():
   con = sqlite3.connect('./database.db')
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Xbox")
   rows = cur.fetchall();
   return render_template("xbox.html", rows = rows)

@app.route('/pc')
def pc():
   con = sqlite3.connect('./database.db')
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Pc")
   rows = cur.fetchall();
   return render_template("pc.html", rows = rows)


@app.route('/data',methods = ['POST', 'GET'])
def data():
   if request.method == 'POST':

            if len(request.form.get('platform')) == 11 :

                contr = request.form.get('user')
                platform = request.form.get('platform')
                conttype = request.form.get('contType')
                gname = request.form.get('game_name')
                date = request.form.get('date')

                with sql.connect('./database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO Playstation (cont,platform,cont_type,gamename,date) VALUES (?,?,?,?,?)",(contr,platform, conttype, gname, date))
                    con.commit()


            if len(request.form.get('platform')) == 4 :

                contr = request.form.get('user')
                platform = request.form.get('platform')
                conttype = request.form.get('contType')
                gname = request.form.get('game_name')
                date = request.form.get('date')

                with sqlite3.connect('./database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO Xbox (cont,platform,cont_type,gamename,date) VALUES (?,?,?,?,?)",(contr,platform, conttype, gname, date))
                    con.commit()


            if len(request.form.get('platform')) == 2 :

                contr = request.form.get('user')
                platform = request.form.get('platform')
                conttype = request.form.get('contType')
                gname = request.form.get('game_name')
                date = request.form.get('date')

                with sqlite3.connect('./database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO Pc (cont,platform,cont_type,gamename,date) VALUES (?,?,?,?,?)",(contr,platform, conttype, gname, date))
                    con.commit()

            msg = "Game has been added to Inventory"
            return render_template("result.html",msg = msg)
            con.close()


if __name__ == "__main__":
  app.run()
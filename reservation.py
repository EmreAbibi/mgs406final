from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import sqlite3 as sql
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
   return render_template('home.htm')

@app.route('/newres')
def newres():
   return render_template('newres.htm')


@app.route('/addres',methods = ['POST', 'GET'])
def addres():
   if request.method == 'POST':
      try:
         ResName = request.form['ResName']
         ResDate = request.form['ResDate']
         ResTime = request.form['ResTime']
         ResParty = request.form['ResParty']
         
         with sql.connect("ferry.db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO reservations (ResName,ResDate,ResTime,ResParty) VALUES ('{0}','{1}','{2}','{3}')".format(ResName,ResDate,ResTime,ResParty)
            cur.execute(cmd)
            
            con.commit()
            msg = "Reservation Successfully Created"
      except:
         con.rollback()
         msg = "An Error Occurred While Creating The Reservation"
         
      finally:
         return render_template("confirm.htm",msg = msg)
         con.close()

@app.route('/schedule')
def schedule():
   con = sql.connect("ferry.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from reservations")
   
   newress = cur.fetchall(); 
   return render_template("schedule.htm",newress = newress)

if __name__ == '__main__':
   app.run(debug = True)


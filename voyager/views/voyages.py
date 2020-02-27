from collections import namedtuple

from flask import render_template
from flask import request

from voyager.db import get_db, execute

def voyages(conn):
    return execute(conn, "select v.sid, v.bid, v.date_of_voyage from Voyages AS v")

def voyages_add(conn, sid, bid, date):
    sqlCommand = f"insert into voyages values({sid},{bid},'{date}');"
    return execute(conn, sqlCommand)

def views(bp):
    @bp.route("/voyages")
    def _voyages():
        with get_db() as conn:
                rows = voyages(conn)
        return render_template("table.html", name="Voyages", rows=rows)

    @bp.route("/voyages/add", methods = ['GET'])
    def voyages_add_page():
        return render_template("addVoyage.html")
    
    @bp.route("/voyages/add", methods = ['POST'])
    def _voyage_add():
        with get_db() as conn:
            sid = request.form['sid']
            bid = request.form['bid']
            date = request.form['date']
            voyages_add(conn, sid, bid, date)
            rows = voyages(conn)
        return render_template("table.html", name="Voyages", rows=rows)
        


    
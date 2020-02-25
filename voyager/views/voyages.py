from collections import namedtuple

from flask import render_template
from flask import request

from voyager.db import get_db, execute

def voyages(conn):
    return execute(conn, "select v.sid, v.bid, v.date_of_voyage from Voyages AS v")

def voyages_add(conn, sid, bid, date_of_voyage):
    # TODO: Enter the correct SQL Command
    sqlCommand = "select * from boats"
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
            date_of_voyage = request.form['date_of_voyage']
            voyages_add(conn, sid, bid, date_of_voyage)
        return "Success"


    